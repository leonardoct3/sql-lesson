import pandas as pd
import numpy as np

def test_left_join(sql_query, conn):
    """Valida o LEFT JOIN entre PROJETOS e CONSULTORES via ALOCACOES"""
    try:
        df = pd.read_sql_query(sql_query, conn)
    except Exception as e:
        print(f"❌ Erro ao executar sua query: {e}")
        return False

    # Colunas esperadas: titulo do projeto + nome do consultor
    expected_cols = ["titulo", "nome_consultor"]
    if list(df.columns) != expected_cols:
        print(f"❌ Colunas incorretas.\nEsperado: {expected_cols}\nObtido:  {list(df.columns)}")
        return False

    # Garante que TODOS os projetos estão no resultado (LEFT JOIN garante isso)
    projetos_df = pd.read_sql_query("SELECT COUNT(*) as total FROM projetos", conn)
    total_projetos = projetos_df.iloc[0]['total']

    projetos_no_resultado = df['titulo'].nunique()
    if projetos_no_resultado != total_projetos:
        print(f"❌ LEFT JOIN deve incluir todos os projetos.\nEsperado: {total_projetos} projetos únicos\nObtido: {projetos_no_resultado} projetos únicos")
        return False

    print("✅ LEFT JOIN validado com sucesso! Todos os projetos incluídos, mesmo sem consultores.")
    return True

def test_inner_join(sql_query, conn):
    """Valida o INNER JOIN entre PROJETOS e CLIENTES"""
    try:
        df = pd.read_sql_query(sql_query, conn)
    except Exception as e:
        print(f"❌ Erro ao executar sua query: {e}")
        return False

    # Checa colunas
    expected_cols = ["titulo", "nome_cliente"]
    if list(df.columns) != expected_cols:
        print(f"❌ Colunas incorretas.\nEsperado: {expected_cols}\nObtido:  {list(df.columns)}")
        return False

    # Monta resultado esperado
    expected_data = {
        "titulo": [
            "ERP I",
            "MARKETING II", 
            "LOGISTICA III",
            "EDUCACAO IV",
            "VENDAS V",
            "FINANCEIRO VI",
        ],
        "nome_cliente": [
            "TechCorp Solutions",   # cliente_id=1
            "Verde Agro Ltda",      # cliente_id=2
            "FastLogistic S.A.",    # cliente_id=5
            "EduCare Ensino",       # cliente_id=4
            "MetalMax Indústrias",  # cliente_id=3
            "TechCorp Solutions",   # cliente_id=1
        ],
    }
    expected_df = pd.DataFrame(expected_data)

    # Ordena para comparação estável
    df_sorted = df.sort_values(by=["titulo", "nome_cliente"]).reset_index(drop=True)
    expected_sorted = expected_df.sort_values(by=["titulo", "nome_cliente"]).reset_index(drop=True)

    # Compara
    if not df_sorted.equals(expected_sorted):
        print("❌ Resultado diferente do esperado.\n")
        print("— Obtido:")
        print(df_sorted.to_string(index=False))
        print("\n— Esperado:")
        print(expected_sorted.to_string(index=False))
        return False

    print("✅ INNER JOIN validado com sucesso! Resultado confere com o esperado.")
    return True


import pandas as pd

import pandas as pd

def test_inner_join_medium(sql_query, conn):
    """
    Valida INNER JOIN de projetos × clientes × feedbacks.
    Espera colunas: titulo, nome_cliente, nota
    Ordenado por: nota DESC, titulo ASC
    """
    # 1) Executa a query do aluno
    try:
        df = pd.read_sql_query(sql_query, conn)
    except Exception as e:
        print(f"❌ Erro ao executar sua query: {e}")
        return False

    # 2) Checa colunas
    expected_cols = ["titulo", "nome_cliente", "nota"]
    if list(df.columns) != expected_cols:
        print(f"❌ Colunas incorretas.\nEsperado: {expected_cols}\nObtido:  {list(df.columns)}")
        return False

    # 3) Monta resultado esperado com base nos INSERTs de feedbacks
    # feedbacks: (projeto_id, nota) -> (1,5), (2,4), (4,5), (5,3), (6,4)
    expected_data = [
        ("EDUCACAO IV",  "EduCare Ensino",     5),
        ("ERP I",        "TechCorp Solutions", 5),
        ("FINANCEIRO VI","TechCorp Solutions", 4),
        ("MARKETING II", "Verde Agro Ltda",    4),
        ("VENDAS V",     "MetalMax Indústrias",3),
    ]
    expected_df = pd.DataFrame(expected_data, columns=expected_cols)

    # 4) Confere ordenação e valores exatamente
    if not df.equals(expected_df):
        print("❌ Resultado diferente do esperado.\n")
        print("— Obtido:")
        print(df.to_string(index=False))
        print("\n— Esperado:")
        print(expected_df.to_string(index=False))
        return False

    print("✅ INNER JOIN (médio) validado com sucesso!")
    return True

def test_inner_join_hard(sql_query, conn):
    """
    Hard sem HAVING:
      - INNER JOIN: clientes, projetos, alocacoes, consultores, feedbacks
      - WHERE: somente feedbacks com nota >= 4
      - GROUP BY: cliente, frente
      - ORDER BY: total_horas DESC, nome_cliente ASC

    Colunas esperadas (nessa ordem):
      nome_cliente, frente, total_horas, media_nota, qtd_projetos
    """
    # 1) Executa a query do aluno
    try:
        df = pd.read_sql_query(sql_query, conn)
    except Exception as e:
        print(f"❌ Erro ao executar sua query: {e}")
        return False

    # 2) Valida colunas
    expected_cols = ["nome_cliente", "frente", "total_horas", "media_nota", "qtd_projetos"]
    if list(df.columns) != expected_cols:
        print(f"❌ Colunas incorretas.\nEsperado: {expected_cols}\nObtido:  {list(df.columns)}")
        return False

    # 3) Resultado esperado com seus dados (nota >= 4; sem filtrar por soma de horas)
    # Grupos esperados:
    # - TechCorp Solutions, ENG: 210.5 horas, média nota 4.5, 2 projetos (1 e 6)
    # - TechCorp Solutions, DIR:  80.0 horas, média nota 5.0, 1 projeto  (1)
    # - Verde Agro Ltda, BUS:    205.5 horas, média nota 4.0, 1 projeto  (2)
    # - EduCare Ensino, BUS:     200.0 horas, média nota 5.0, 1 projeto  (4)
    expected = pd.DataFrame(
        [
            ("TechCorp Solutions", "ENG", 210.5, 4.5, 2),
            ("Verde Agro Ltda",    "BUS", 205.5, 4.0, 1),
            ("EduCare Ensino",     "BUS", 200.0, 5.0, 1),
            ("TechCorp Solutions", "DIR",  80.0, 5.0, 1),
        ],
        columns=expected_cols
    )

    # 4) Normaliza tipos e ordena para verificação
    df_norm = df.copy()
    df_norm["total_horas"]  = df_norm["total_horas"].astype(float)
    df_norm["media_nota"]   = df_norm["media_nota"].astype(float)
    df_norm["qtd_projetos"] = df_norm["qtd_projetos"].astype(int)
    df_norm = df_norm.sort_values(
        by=["total_horas", "nome_cliente"], ascending=[False, True]
    ).reset_index(drop=True)

    expected_norm = expected.sort_values(
        by=["total_horas", "nome_cliente"], ascending=[False, True]
    ).reset_index(drop=True)

    same_shape = df_norm.shape == expected_norm.shape
    same_cols  = list(df_norm.columns) == list(expected_norm.columns)
    floats_ok  = (
        np.allclose(df_norm["total_horas"], expected_norm["total_horas"], rtol=1e-6, atol=1e-6)
        and np.allclose(df_norm["media_nota"], expected_norm["media_nota"], rtol=1e-6, atol=1e-6)
    )
    strings_ok = df_norm[["nome_cliente","frente"]].equals(expected_norm[["nome_cliente","frente"]])
    ints_ok    = (df_norm["qtd_projetos"] == expected_norm["qtd_projetos"]).all()

    if not (same_shape and same_cols and floats_ok and strings_ok and ints_ok):
        print("❌ Resultado diferente do esperado.\n")
        print("— Obtido:")
        print(df_norm.to_string(index=False))
        print("\n— Esperado:")
        print(expected_norm.to_string(index=False))
        return False

    print("✅ INNER JOIN (hard, sem HAVING) validado com sucesso!")
    return True

import pandas as pd

def test_left_join_medium(sql_query, conn):
    """
    LEFT JOIN (clientes × projetos).
    Espera colunas: nome_cliente, titulo
    Ordenação: nome_cliente ASC, titulo ASC
    """
    try:
        df = pd.read_sql_query(sql_query, conn)
    except Exception as e:
        print(f"❌ Erro ao executar sua query: {e}")
        return False

    expected_cols = ["nome_cliente", "titulo"]
    if list(df.columns) != expected_cols:
        print(f"❌ Colunas incorretas.\nEsperado: {expected_cols}\nObtido: {list(df.columns)}")
        return False

    # Resultado esperado com base nos INSERTs que você fez
    expected_data = [
        ("EduCare Ensino",     "EDUCACAO IV"),
        ("FastLogistic S.A.",  "LOGISTICA III"),
        ("MetalMax Indústrias","VENDAS V"),
        ("TechCorp Solutions", "ERP I"),
        ("TechCorp Solutions", "FINANCEIRO VI"),
        ("Verde Agro Ltda",    "MARKETING II"),
    ]
    expected_df = pd.DataFrame(expected_data, columns=expected_cols)

    # Como é LEFT JOIN, pode haver clientes sem projetos (nesse caso, todos têm)
    df_sorted = df.sort_values(by=["nome_cliente", "titulo"], na_position="last").reset_index(drop=True)
    expected_sorted = expected_df.sort_values(by=["nome_cliente", "titulo"], na_position="last").reset_index(drop=True)

    if not df_sorted.equals(expected_sorted):
        print("❌ Resultado diferente do esperado.\n")
        print("— Obtido:")
        print(df_sorted.to_string(index=False))
        print("\n— Esperado:")
        print(expected_sorted.to_string(index=False))
        return False

    print("✅ LEFT JOIN (médio) validado com sucesso!")
    return True



def test_left_join_hard(sql_query, conn):
    """
    LEFT JOIN difícil:
      - Base: clientes
      - LEFT JOIN projetos, feedbacks, alocacoes
      - GROUP BY cliente
      - ORDER BY nome_cliente ASC
    Colunas:
      nome_cliente, projetos_total, projetos_com_feedback, projetos_nota_ge_4, media_nota, total_horas
    """
    # 1) Executa a query do aluno
    try:
        df = pd.read_sql_query(sql_query, conn)
    except Exception as e:
        print(f"❌ Erro ao executar sua query: {e}")
        return False

    # 2) Valida colunas
    expected_cols = [
        "nome_cliente",
        "projetos_total",
        "projetos_com_feedback",
        "projetos_nota_ge_4",
        "media_nota",
        "total_horas",
    ]
    if list(df.columns) != expected_cols:
        print(f"❌ Colunas incorretas.\nEsperado: {expected_cols}\nObtido:  {list(df.columns)}")
        return False

    # 3) Resultado esperado com base nos seus inserts
    # ATENÇÃO: Com a subquery, a média para TechCorp Solutions agora é 4.5 (correto)
    expected = pd.DataFrame(
        [
            ("EduCare Ensino",      1, 1, 1, 5.0, 200.0),
            ("FastLogistic S.A.",   1, 0, 0, np.nan, 225.5),
            ("MetalMax Indústrias", 1, 1, 0, 3.0, 145.5),
            ("TechCorp Solutions",  2, 2, 2, 4.5, 290.5),  # Média correta com subquery
            ("Verde Agro Ltda",     1, 1, 1, 4.0, 205.5),
        ],
        columns=expected_cols
    )

    # 4) Normaliza tipos e ordena
    df_norm = df.copy()
    for col in ["projetos_total", "projetos_com_feedback", "projetos_nota_ge_4"]:
        df_norm[col] = df_norm[col].astype(int)
    df_norm["total_horas"] = df_norm["total_horas"].astype(float)
    # media_nota pode ter NaN
    df_norm = df_norm.sort_values(by=["nome_cliente"]).reset_index(drop=True)
    expected_norm = expected.sort_values(by=["nome_cliente"]).reset_index(drop=True)

    # 5) Compara (com tolerância p/ floats e NaN em media_nota)
    same_shape = df_norm.shape == expected_norm.shape
    same_cols  = list(df_norm.columns) == list(expected_norm.columns)
    ints_ok = (df_norm[["projetos_total","projetos_com_feedback","projetos_nota_ge_4"]]
               .equals(expected_norm[["projetos_total","projetos_com_feedback","projetos_nota_ge_4"]]))
    horas_ok = np.allclose(df_norm["total_horas"], expected_norm["total_horas"], rtol=1e-6, atol=1e-6)
    nomes_ok = df_norm["nome_cliente"].equals(expected_norm["nome_cliente"])

    # compara media_nota com NaN permitido
    medias_a = df_norm["media_nota"].astype(float).to_numpy()
    medias_b = expected_norm["media_nota"].astype(float).to_numpy()
    medias_ok = np.all((np.isclose(medias_a, medias_b, rtol=1e-6, atol=1e-6)) | (np.isnan(medias_a) & np.isnan(medias_b)))

    if not (same_shape and same_cols and ints_ok and horas_ok and nomes_ok and medias_ok):
        print("❌ Resultado diferente do esperado.\n")
        print("— Obtido:")
        print(df_norm.to_string(index=False))
        print("\n— Esperado:")
        print(expected_norm.to_string(index=False))
        return False

    print("✅ LEFT JOIN (difícil) validado com sucesso!")
    return True
