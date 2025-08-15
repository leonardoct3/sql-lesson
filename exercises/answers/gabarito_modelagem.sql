-- ================================
-- GABARITO: MODELAGEM DE BANCO DE DADOS
-- ================================

-- Habilitando chaves estrangeiras
PRAGMA foreign_keys = ON;

-- ================================
-- DDL - CRIAÇÃO DAS TABELAS  
-- ================================

-- 1. Tabela CLIENTES
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    setor TEXT NOT NULL,
    cidade TEXT NOT NULL,
    uf CHAR(2) NOT NULL
);

-- 2. Tabela PROJETOS
CREATE TABLE projetos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    escopo TEXT,
    data_inicio DATE NOT NULL,
    data_fim DATE,
    cliente_id INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) 
        ON DELETE RESTRICT ON UPDATE CASCADE
);

-- 3. Tabela CONSULTORES
CREATE TABLE consultores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    frente TEXT NOT NULL
);

-- 4. Tabela ALOCACOES
CREATE TABLE alocacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    projeto_id INTEGER NOT NULL,
    consultor_id INTEGER NOT NULL,
    horas_trabalhadas REAL NOT NULL CHECK (horas_trabalhadas >= 0),
    FOREIGN KEY (projeto_id) REFERENCES projetos(id) 
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (consultor_id) REFERENCES consultores(id) 
        ON DELETE RESTRICT ON UPDATE CASCADE,
    UNIQUE(projeto_id, consultor_id)
);

-- 5. Tabela FEEDBACKS
CREATE TABLE feedbacks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    projeto_id INTEGER NOT NULL,
    nota INTEGER NOT NULL CHECK (nota >= 1 AND nota <= 5),
    comentario TEXT,
    FOREIGN KEY (projeto_id) REFERENCES projetos(id) 
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- ================================
-- DML - INSERÇÃO DE DADOS
-- ================================

-- 1. Inserindo CLIENTES
INSERT INTO clientes (nome, setor, cidade, uf) VALUES 
('TechCorp Solutions', 'Tecnologia', 'São Paulo', 'SP'),
('Verde Agro Ltda', 'Agronegócio', 'Campinas', 'SP'),
('MetalMax Indústrias', 'Metalurgia', 'Santos', 'SP'),
('EduCare Ensino', 'Educação', 'Ribeirão Preto', 'SP'),
('FastLogistic S.A.', 'Logística', 'São José dos Campos', 'SP');

-- 2. Inserindo CONSULTORES
INSERT INTO consultores (nome, frente) VALUES 
('Ana Silva', 'ENG'),
('Carlos Santos', 'BUS'),
('Maria Oliveira', 'DIR'),
('João Costa', 'ENG'),
('Fernanda Lima', 'BUS');

-- 3. Inserindo PROJETOS
INSERT INTO projetos (titulo, escopo, data_inicio, data_fim, cliente_id) VALUES 
('ERP I', 'Implementação de sistema ERP', '2024-01-15', '2024-06-15', 1),
('MARKETING II', 'Estratégia de marketing digital', '2024-02-01', '2024-08-01', 2),
('LOGISTICA III', 'Otimização de processos logísticos', '2024-03-10', NULL, 5),
('EDUCACAO IV', 'Plataforma de ensino online', '2024-04-05', '2024-10-05', 4),
('VENDAS V', 'Automação de vendas', '2024-05-20', NULL, 3),
('FINANCEIRO VI', 'Sistema financeiro integrado', '2024-06-15', NULL, 1);

-- 4. Inserindo ALOCACOES
INSERT INTO alocacoes (projeto_id, consultor_id, horas_trabalhadas) VALUES 
(1, 1, 120.5),
(1, 3, 80.0),
(2, 2, 95.5),
(2, 5, 110.0),
(3, 1, 150.0),
(3, 4, 75.5),
(4, 5, 200.0),
(5, 2, 60.0),
(5, 3, 85.5),
(6, 1, 90.0);

-- 5. Inserindo FEEDBACKS
INSERT INTO feedbacks (projeto_id, nota, comentario) VALUES 
(1, 5, 'Excelente trabalho, superou expectativas'),
(2, 4, 'Bom resultado, algumas melhorias necessárias'),
(4, 5, 'Projeto entregue com qualidade excepcional'),
(5, 3, 'Resultado satisfatório, pode melhorar'),
(6, 4, 'Boa execução dentro do prazo');