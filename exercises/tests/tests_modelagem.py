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

def test_create_clientes(conn):
    """Testa se a tabela clientes foi criada corretamente"""
    try:
        cursor = conn.cursor()
        # Verifica se a tabela existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clientes'")
        table_exists = cursor.fetchone()
        
        if not table_exists:
            print("❌ FALHOU: Criação da tabela clientes")
            print("Esperado: Tabela 'clientes' criada")
            print("Obtido: Tabela não encontrada")
            return False
        
        # Verifica as colunas
        cursor.execute("PRAGMA table_info(clientes)")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        expected_columns = ['id', 'nome', 'setor', 'cidade', 'uf']
        
        if set(column_names) != set(expected_columns):
            print("❌ FALHOU: Criação da tabela clientes")
            print(f"Esperado: Colunas {expected_columns}")
            print(f"Obtido: Colunas {column_names}")
            return False
        
        print("✅ PASSOU: Criação da tabela clientes")
        return True
    except Exception as e:
        print(f"❌ FALHOU: Criação da tabela clientes - Erro: {str(e)}")
        return False

def test_create_projetos(conn):
    """Testa se a tabela projetos foi criada corretamente"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projetos'")
        table_exists = cursor.fetchone()
        
        if not table_exists:
            print("❌ FALHOU: Criação da tabela projetos")
            print("Esperado: Tabela 'projetos' criada")
            print("Obtido: Tabela não encontrada")
            return False
        
        cursor.execute("PRAGMA table_info(projetos)")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        expected_columns = ['id', 'titulo', 'escopo', 'data_inicio', 'data_fim', 'cliente_id']
        
        if set(column_names) != set(expected_columns):
            print("❌ FALHOU: Criação da tabela projetos")
            print(f"Esperado: Colunas {expected_columns}")
            print(f"Obtido: Colunas {column_names}")
            return False
        
        print("✅ PASSOU: Criação da tabela projetos")
        return True
    except Exception as e:
        print(f"❌ FALHOU: Criação da tabela projetos - Erro: {str(e)}")
        return False

def test_create_consultores(conn):
    """Testa se a tabela consultores foi criada corretamente"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='consultores'")
        table_exists = cursor.fetchone()
        
        if not table_exists:
            print("❌ FALHOU: Criação da tabela consultores")
            print("Esperado: Tabela 'consultores' criada")
            print("Obtido: Tabela não encontrada")
            return False
        
        cursor.execute("PRAGMA table_info(consultores)")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        expected_columns = ['id', 'nome', 'frente']
        
        if set(column_names) != set(expected_columns):
            print("❌ FALHOU: Criação da tabela consultores")
            print(f"Esperado: Colunas {expected_columns}")
            print(f"Obtido: Colunas {column_names}")
            return False
        
        print("✅ PASSOU: Criação da tabela consultores")
        return True
    except Exception as e:
        print(f"❌ FALHOU: Criação da tabela consultores - Erro: {str(e)}")
        return False

def test_create_alocacoes(conn):
    """Testa se a tabela alocacoes foi criada corretamente"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='alocacoes'")
        table_exists = cursor.fetchone()
        
        if not table_exists:
            print("❌ FALHOU: Criação da tabela alocacoes")
            print("Esperado: Tabela 'alocacoes' criada")
            print("Obtido: Tabela não encontrada")
            return False
        
        cursor.execute("PRAGMA table_info(alocacoes)")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        expected_columns = ['id', 'projeto_id', 'consultor_id', 'horas_trabalhadas']
        
        if set(column_names) != set(expected_columns):
            print("❌ FALHOU: Criação da tabela alocacoes")
            print(f"Esperado: Colunas {expected_columns}")
            print(f"Obtido: Colunas {column_names}")
            return False
        
        print("✅ PASSOU: Criação da tabela alocacoes")
        return True
    except Exception as e:
        print(f"❌ FALHOU: Criação da tabela alocacoes - Erro: {str(e)}")
        return False

def test_create_feedbacks(conn):
    """Testa se a tabela feedbacks foi criada corretamente"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='feedbacks'")
        table_exists = cursor.fetchone()
        
        if not table_exists:
            print("❌ FALHOU: Criação da tabela feedbacks")
            print("Esperado: Tabela 'feedbacks' criada")
            print("Obtido: Tabela não encontrada")
            return False
        
        cursor.execute("PRAGMA table_info(feedbacks)")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        expected_columns = ['id', 'projeto_id', 'nota', 'comentario']
        
        if set(column_names) != set(expected_columns):
            print("❌ FALHOU: Criação da tabela feedbacks")
            print(f"Esperado: Colunas {expected_columns}")
            print(f"Obtido: Colunas {column_names}")
            return False
        
        print("✅ PASSOU: Criação da tabela feedbacks")
        return True
    except Exception as e:
        print(f"❌ FALHOU: Criação da tabela feedbacks - Erro: {str(e)}")
        return False

def test_insert_clientes(conn):
    """Testa se os dados foram inseridos corretamente na tabela clientes"""
    expected_data = {
        'id': [1, 2, 3, 4, 5],
        'nome': ['TechCorp Solutions', 'Verde Agro Ltda', 'MetalMax Indústrias', 'EduCare Ensino', 'FastLogistic S.A.'],
        'setor': ['Tecnologia', 'Agronegócio', 'Metalurgia', 'Educação', 'Logística'],
        'cidade': ['São Paulo', 'Campinas', 'Santos', 'Ribeirão Preto', 'São José dos Campos'],
        'uf': ['SP', 'SP', 'SP', 'SP', 'SP']
    }
    expected_df = pd.DataFrame(expected_data)
    
    try:
        got_df = pd.read_sql_query("SELECT * FROM clientes ORDER BY id", conn)
        return assert_equal(expected_df, got_df, "Inserção de dados na tabela clientes")
    except Exception as e:
        print(f"❌ FALHOU: Inserção de dados na tabela clientes - Erro: {str(e)}")
        return False

def test_insert_consultores(conn):
    """Testa se os dados foram inseridos corretamente na tabela consultores"""
    expected_data = {
        'id': [1, 2, 3, 4, 5],
        'nome': ['Ana Silva', 'Carlos Santos', 'Maria Oliveira', 'João Costa', 'Fernanda Lima'],
        'frente': ['ENG', 'BUS', 'DIR', 'ENG', 'BUS']
    }
    expected_df = pd.DataFrame(expected_data)
    
    try:
        got_df = pd.read_sql_query("SELECT * FROM consultores ORDER BY id", conn)
        return assert_equal(expected_df, got_df, "Inserção de dados na tabela consultores")
    except Exception as e:
        print(f"❌ FALHOU: Inserção de dados na tabela consultores - Erro: {str(e)}")
        return False

def test_insert_projetos(conn):
    """Testa se os dados foram inseridos corretamente na tabela projetos"""
    expected_data = {
        'id': [1, 2, 3, 4, 5, 6],
        'titulo': ['ERP I', 'MARKETING II', 'LOGISTICA III', 'EDUCACAO IV', 'VENDAS V', 'FINANCEIRO VI'],
        'escopo': ['Implementação de sistema ERP', 'Estratégia de marketing digital', 'Otimização de processos logísticos', 'Plataforma de ensino online', 'Automação de vendas', 'Sistema financeiro integrado'],
        'data_inicio': ['2024-01-15', '2024-02-01', '2024-03-10', '2024-04-05', '2024-05-20', '2024-06-15'],
        'data_fim': ['2024-06-15', '2024-08-01', None, '2024-10-05', None, None],
        'cliente_id': [1, 2, 5, 4, 3, 1]
    }
    expected_df = pd.DataFrame(expected_data)
    
    try:
        got_df = pd.read_sql_query("SELECT * FROM projetos ORDER BY id", conn)
        return assert_equal(expected_df, got_df, "Inserção de dados na tabela projetos")
    except Exception as e:
        print(f"❌ FALHOU: Inserção de dados na tabela projetos - Erro: {str(e)}")
        return False

def test_insert_alocacoes(conn):
    """Testa se os dados foram inseridos corretamente na tabela alocacoes"""
    expected_data = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'projeto_id': [1, 1, 2, 2, 3, 3, 4, 5, 5, 6],
        'consultor_id': [1, 3, 2, 5, 1, 4, 5, 2, 3, 1],
        'horas_trabalhadas': [120.5, 80.0, 95.5, 110.0, 150.0, 75.5, 200.0, 60.0, 85.5, 90.0]
    }
    expected_df = pd.DataFrame(expected_data)
    
    try:
        got_df = pd.read_sql_query("SELECT * FROM alocacoes ORDER BY id", conn)
        return assert_equal(expected_df, got_df, "Inserção de dados na tabela alocacoes")
    except Exception as e:
        print(f"❌ FALHOU: Inserção de dados na tabela alocacoes - Erro: {str(e)}")
        return False

def test_insert_feedbacks(conn):
    """Testa se os dados foram inseridos corretamente na tabela feedbacks"""
    expected_data = {
        'id': [1, 2, 3, 4, 5],
        'projeto_id': [1, 2, 4, 5, 6],
        'nota': [5, 4, 5, 3, 4],
        'comentario': ['Excelente trabalho, superou expectativas', 'Bom resultado, algumas melhorias necessárias', 'Projeto entregue com qualidade excepcional', 'Resultado satisfatório, pode melhorar', 'Boa execução dentro do prazo']
    }
    expected_df = pd.DataFrame(expected_data)
    
    try:
        got_df = pd.read_sql_query("SELECT * FROM feedbacks ORDER BY id", conn)
        return assert_equal(expected_df, got_df, "Inserção de dados na tabela feedbacks")
    except Exception as e:
        print(f"❌ FALHOU: Inserção de dados na tabela feedbacks - Erro: {str(e)}")
        return False
