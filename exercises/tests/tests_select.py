import sqlite3
import pandas as pd

def test_select_scu_clientes(conn, query):
    """Testa a query SELECT - setor, cidade e uf dos clientes"""
    expected_data = {
        'setor': ['Tecnologia', 'Agronegócio', 'Metalurgia', 'Educação', 'Logística'],
        'cidade': ['São Paulo', 'Campinas', 'Santos', 'Ribeirão Preto', 'São José dos Campos'],
        'uf': ['SP', 'SP', 'SP', 'SP', 'SP']
    }
    expected_df = pd.DataFrame(expected_data)
    
    try:
        # Usar a query do usuário se fornecida, caso contrário usar a query do gabarito
        query_to_test = query if query else """
            SELECT setor, cidade uf 
            FROM clientes
        """
        resultado = pd.read_sql_query(query_to_test, conn)
        
        # Sempre mostrar os dois DataFrames para comparação
        print("\nRESULTADO ESPERADO:")
        print("=" * 50)
        print(expected_df.to_string(index=False))
        print("\n📊 SEU RESULTADO:")
        print("=" * 50)
        print(resultado.to_string(index=False))
        print("\n")
        
        # Agora fazer a validação
        try:
            pd.testing.assert_frame_equal(
                expected_df.sort_index(axis=1).reset_index(drop=True),
                resultado.sort_index(axis=1).reset_index(drop=True),
                check_dtype=False
            )
            print("✅ PASSOU: SELECT - setor, cidade e uf dos clientes")
            return True
        except AssertionError:
            print("❌ FALHOU: Os resultados não são iguais")
            print("💡 Dica: Verifique se você selecionou apenas as colunas pedidas na ordem correta")
            return False
            
    except Exception as e:
        print(f"❌ FALHOU: Erro ao executar query - {str(e)}")
        return False
