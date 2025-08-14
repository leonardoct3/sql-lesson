# Script to create a sample SQLite database for the lesson
import sqlite3
import os

# Check if the database already exists
if os.path.exists('biblioteca.db'):
    print(100 * '=')
    print('O banco de dados biblioteca.db já existe. Nenhuma ação necessária.')
    print(100 * '=')
    exit()

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nascimento INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    autor_id INTEGER,
    titulo TEXT NOT NULL,
    ano_publicacao INTEGER,
    FOREIGN KEY(autor_id) REFERENCES autores(id)
);
''')

# Inserir dados de exemplo
cursor.executemany('INSERT INTO autores (nome, nascimento) VALUES (?, ?);', [
    ('Machado de Assis', 1839),
    ('Clarice Lispector', 1920),
    ('Jorge Amado', 1912),
    ('Graciliano Ramos', 1892),
    ('Cecília Meireles', 1901),
    ('Monteiro Lobato', 1882),
    ('Carlos Drummond de Andrade', 1902),
    ('Manuel Bandeira', 1886),
    ('João Cabral de Melo Neto', 1920),
    ('Guimarães Rosa', 1908)
])

cursor.executemany('INSERT INTO livros (autor_id, titulo, ano_publicacao) VALUES (?, ?, ?);', [
    (1, 'Dom Casmurro', 1899),
    (1, 'Memórias Póstumas de Brás Cubas', 1881),
    (1, 'Quincas Borba', 1891),
    (2, 'A Hora da Estrela', 1977),
    (2, 'Laços de Família', 1960),
    (3, 'Capitães da Areia', 1937),
    (3, 'Gabriela, Cravo e Canela', 1958),
    (3, 'Dona Flor e Seus Dois Maridos', 1966),
    (4, 'Vidas Secas', 1938),
    (4, 'São Bernardo', 1934),
    (5, 'Romanceiro da Inconfidência', 1953),
    (5, 'Mar Absoluto', 1945),
    (6, 'O Sítio do Picapau Amarelo', 1920),
    (6, 'Reinações de Narizinho', 1931),
    (6, 'Caçadas de Pedrinho', 1933),
    (7, 'Sentimento do Mundo', 1940),
    (7, 'A Rosa do Povo', 1945),
    (7, 'Claro Enigma', 1951),
    (8, 'Libertinagem', 1930),
    (8, 'Estrela da Manhã', 1936),
    (9, 'Morte e Vida Severina', 1955),
    (9, 'O Rio', 1953),
    (10, 'Grande Sertão: Veredas', 1956),
    (10, 'Sagarana', 1946)
])

conn.commit()
conn.close()
print(100 * '=')
print('Banco de dados criado como biblioteca.db ✔️')
print(100 * '=')