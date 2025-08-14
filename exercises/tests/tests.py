import sqlite3
import pandas as pd

def create_conn():
    conn = sqlite3.connect('../biblioteca.db')
    return conn

def aluno_vs_correta(conn, query_aluno, correta):
    df_aluno = pd.read_sql_query(query_aluno, conn)
    df_correta = pd.read_sql_query("SELECT * FROM autores", conn)
    return df_aluno, df_correta

def testa_consulta_autores(query_aluno):
    conn = create_conn()
    df_aluno, df_correta = aluno_vs_correta(conn, query_aluno, "SELECT * FROM autores")
    conn.close()
    try:
        pd.testing.assert_frame_equal(df_aluno.sort_index(axis=1), df_correta.sort_index(axis=1))
        return "Parabéns! Sua consulta está correta e retorna exatamente o esperado."
    except AssertionError:
        return ("Sua consulta não retorna o resultado esperado.\n"
                "Dica: verifique se está selecionando todas as colunas e linhas corretamente.")
