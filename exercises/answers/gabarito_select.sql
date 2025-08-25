-- ================================
-- GABARITO: SELECT NO BANCO DE DADOS
-- ================================

-- Habilitando chaves estrangeiras
PRAGMA foreign_keys = ON;

-- ================================
-- SELECT - MANIPULAÇÃO DAS TABELAS  
-- ================================

-- 1. Select setor, cidade e uf
SELECT setor, cidade, uf FROM clientes
