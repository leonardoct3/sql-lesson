import sqlite3
import pandas as pd

def assert_equal(expected_df, got_df, contexto):
    """Compara DataFrames e mostra mensagens claras de erro ou sucesso"""
    try:
        pd.testing.assert_frame_equal(
            expected_df.sort_index(axis=1).reset_index(drop=True),
            got_df.sort_index(axis=1).reset_index(drop=True),
            check_dtype=False
        )
        print(f"✅ PASSOU: {contexto}")
        return True
    except AssertionError:
        print(f"❌ FALHOU: {contexto}")
        print(f"Esperado:\n{expected_df}")
        print(f"Obtido:\n{got_df}")
        return False

def test_update_cliente(conn):
    """Testa se a cidade do cliente Verde Agro foi atualizada para Piracicaba"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT cidade FROM clientes WHERE nome = 'Verde Agro Ltda'")
        result = cursor.fetchone()
        
        if result and result[0] == 'Piracicaba':
            print("✅ PASSOU: UPDATE cidade do cliente Verde Agro Ltda")
            return True
        else:
            print("❌ FALHOU: UPDATE cidade do cliente Verde Agro Ltda")
            print("Esperado: cidade = 'Piracicaba'")
            print(f"Obtido: cidade = '{result[0] if result else 'None'}'")
            return False
    except Exception as e:
        print(f"❌ FALHOU: UPDATE cidade do cliente - Erro: {str(e)}")
        return False

def test_update_horas(conn):
    """Testa se as horas de Ana Silva no projeto ERP I foram aumentadas em 10"""
    try:
        cursor = conn.cursor()
        # Ana Silva (id=1) no projeto ERP I (id=1) deve ter 130.5 horas (120.5 + 10)
        cursor.execute("""
            SELECT horas_trabalhadas 
            FROM alocacoes 
            WHERE consultor_id = 1 AND projeto_id = 1
        """)
        result = cursor.fetchone()
        
        if result and result[0] == 130.5:
            print("✅ PASSOU: UPDATE horas trabalhadas (+10 para Ana Silva no ERP I)")
            return True
        else:
            print("❌ FALHOU: UPDATE horas trabalhadas")
            print("Esperado: horas_trabalhadas = 130.5 (120.5 + 10)")
            print(f"Obtido: horas_trabalhadas = {result[0] if result else 'None'}")
            return False
    except Exception as e:
        print(f"❌ FALHOU: UPDATE horas trabalhadas - Erro: {str(e)}")
        return False

def test_delete_feedback(conn):
    """Testa se o feedback do projeto VENDAS V foi removido"""
    try:
        cursor = conn.cursor()
        # Verifica se não existe mais feedback para o projeto VENDAS V (id=5)
        cursor.execute("""
            SELECT COUNT(*) 
            FROM feedbacks f
            JOIN projetos p ON f.projeto_id = p.id
            WHERE p.titulo = 'VENDAS V'
        """)
        count = cursor.fetchone()[0]
        
        if count == 0:
            print("✅ PASSOU: DELETE feedback do projeto VENDAS V")
            return True
        else:
            print("❌ FALHOU: DELETE feedback do projeto VENDAS V")
            print("Esperado: 0 feedbacks para VENDAS V")
            print(f"Obtido: {count} feedbacks encontrados")
            return False
    except Exception as e:
        print(f"❌ FALHOU: DELETE feedback - Erro: {str(e)}")
        return False

def test_delete_cliente_restrito(conn):
    """Testa se a tentativa de deletar cliente com projetos falha (RESTRICT)"""
    try:
        cursor = conn.cursor()
        
        # Primeiro verifica se o cliente ainda existe
        cursor.execute("SELECT COUNT(*) FROM clientes WHERE nome = 'TechCorp Solutions'")
        count = cursor.fetchone()[0]
        
        if count == 1:
            print("✅ PASSOU: DELETE cliente restrito - Cliente preservado pela restrição RESTRICT")
            return True
        else:
            print("❌ FALHOU: DELETE cliente restrito")
            print("Esperado: Cliente TechCorp Solutions deve ser preservado (RESTRICT)")
            print(f"Obtido: Cliente não encontrado")
            return False
    except Exception as e:
        print(f"❌ FALHOU: DELETE cliente restrito - Erro: {str(e)}")
        return False

def test_delete_projeto(conn):
    """Testa se o projeto LOGISTICA III foi deletado e se cascateou para alocações"""
    try:
        cursor = conn.cursor()
        
        # Verifica se o projeto foi deletado
        cursor.execute("SELECT COUNT(*) FROM projetos WHERE titulo = 'LOGISTICA III'")
        projeto_count = cursor.fetchone()[0]
        
        # Verifica se as alocações relacionadas também foram deletadas (CASCADE)
        cursor.execute("SELECT COUNT(*) FROM alocacoes WHERE projeto_id = 3")
        alocacao_count = cursor.fetchone()[0]
        
        if projeto_count == 0 and alocacao_count == 0:
            print("✅ PASSOU: DELETE projeto LOGISTICA III com CASCADE")
            return True
        else:
            print("❌ FALHOU: DELETE projeto LOGISTICA III")
            print("Esperado: projeto deletado e alocações em cascade")
            print(f"Obtido: projeto_count={projeto_count}, alocacao_count={alocacao_count}")
            return False
    except Exception as e:
        print(f"❌ FALHOU: DELETE projeto - Erro: {str(e)}")
        return False

def test_replace_feedback(conn):
    """Testa se o feedback do projeto FINANCEIRO VI foi alterado para nota 5"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT f.nota 
            FROM feedbacks f
            JOIN projetos p ON f.projeto_id = p.id
            WHERE p.titulo = 'FINANCEIRO VI'
        """)
        result = cursor.fetchone()
        
        if result and result[0] == 5:
            print("✅ PASSOU: REPLACE feedback do projeto FINANCEIRO VI")
            return True
        else:
            print("❌ FALHOU: REPLACE feedback do projeto FINANCEIRO VI")
            print("Esperado: nota = 5")
            print(f"Obtido: nota = {result[0] if result else 'None'}")
            return False
    except Exception as e:
        print(f"❌ FALHOU: REPLACE feedback - Erro: {str(e)}")
        return False

def test_update_cliente_id(conn):
    """Testa se o ID do cliente EduCare foi alterado para 40 e se cascateou"""
    try:
        cursor = conn.cursor()
        
        # Verifica se o cliente tem ID 40 agora
        cursor.execute("SELECT COUNT(*) FROM clientes WHERE id = 40 AND nome = 'EduCare Ensino'")
        cliente_count = cursor.fetchone()[0]
        
        # Verifica se o projeto EDUCACAO IV agora tem cliente_id = 40
        cursor.execute("""
            SELECT cliente_id 
            FROM projetos 
            WHERE titulo = 'EDUCACAO IV'
        """)
        result = cursor.fetchone()
        projeto_cliente_id = result[0] if result else None
        
        if cliente_count == 1 and projeto_cliente_id == 40:
            print("✅ PASSOU: UPDATE CASCADE cliente ID para 40")
            return True
        else:
            print("❌ FALHOU: UPDATE CASCADE cliente ID")
            print("Esperado: cliente_id=40 e projeto com cliente_id=40")
            print(f"Obtido: cliente_count={cliente_count}, projeto_cliente_id={projeto_cliente_id}")
            return False
    except Exception as e:
        print(f"❌ FALHOU: UPDATE CASCADE cliente ID - Erro: {str(e)}")
        return False
