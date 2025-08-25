-- ================================
-- GABARITO: MANIPULAÇÃO DE DADOS (DML)
-- ================================

-- Habilitando chaves estrangeiras
PRAGMA foreign_keys = ON;

-- ================================
-- EXERCÍCIO 1: UPDATE - Cliente mudou de cidade
-- ================================

-- A empresa 'Verde Agro Ltda' se mudou de Campinas para Piracicaba
UPDATE clientes 
SET cidade = 'Piracicaba' 
WHERE nome = 'Verde Agro Ltda';

-- ================================
-- EXERCÍCIO 2: UPDATE - Ajustar horas trabalhadas
-- ================================

-- Ana Silva trabalhou mais 10 horas no projeto ERP I
-- Ana Silva = consultor_id 1, ERP I = projeto_id 1
UPDATE alocacoes 
SET horas_trabalhadas = horas_trabalhadas + 10 
WHERE consultor_id = 1 AND projeto_id = 1;

-- Alternativa com subquery:
-- UPDATE alocacoes 
-- SET horas_trabalhadas = horas_trabalhadas + 10 
-- WHERE consultor_id = (SELECT id FROM consultores WHERE nome = 'Ana Silva')
--   AND projeto_id = (SELECT id FROM projetos WHERE titulo = 'ERP I');

-- ================================
-- EXERCÍCIO 3: DELETE - Remover feedback
-- ================================

-- Delete o feedback do projeto_id=5
DELETE FROM feedbacks 
WHERE projeto_id = 5;

-- ================================
-- EXERCÍCIO 4: DELETE - Testando Restrição ON DELETE RESTRICT
-- ================================

-- Tente deletar o cliente 'TechCorp Solutions' (id=1)
-- Esta operação deve FALHAR devido à restrição RESTRICT
DELETE FROM clientes WHERE id = 1;
-- Resultado esperado: FOREIGN KEY constraint failed

-- ================================
-- EXERCÍCIO 5: DELETE - Testando ON DELETE CASCADE
-- ================================

-- Delete o projeto onde id=3
-- Isso deve remover automaticamente alocações relacionadas (CASCADE)
DELETE FROM projetos WHERE id = 3;

-- ================================
-- EXERCÍCIO 6: REPLACE - Corrigir nota de feedback
-- ================================

-- Use REPLACE para alterar a nota do feedback do projeto_id=6 para 5
-- Como REPLACE substitui toda a linha, precisamos incluir todas as colunas
REPLACE INTO feedbacks (id, projeto_id, nota, comentario)
VALUES (5, 6, 5, 'Boa execução dentro do prazo');


-- ================================
-- EXERCÍCIO 7: ON UPDATE CASCADE - Atualizar ID de cliente
-- ================================

-- Atualize o id do cliente onde id=4 para 40
-- Os projetos deste cliente devem ter cliente_id atualizado automaticamente
UPDATE clientes 
SET id = 40 
WHERE id = 4;

-- ================================
-- VERIFICAÇÕES FINAIS
-- ================================

-- Verificar resultados das operações
SELECT 'CLIENTES' as tabela, id, nome, cidade FROM clientes ORDER BY id;
SELECT 'PROJETOS' as tabela, id, titulo, cliente_id FROM projetos ORDER BY id;
SELECT 'ALOCACOES' as tabela, id, projeto_id, consultor_id, horas_trabalhadas FROM alocacoes ORDER BY id;
SELECT 'FEEDBACKS' as tabela, id, projeto_id, nota, comentario FROM feedbacks ORDER BY id;

-- Contagem de registros para verificar CASCADE
SELECT 'Contagem Alocações' as info, COUNT(*) as total FROM alocacoes;
SELECT 'Contagem Feedbacks' as info, COUNT(*) as total FROM feedbacks;
SELECT 'Contagem Projetos' as info, COUNT(*) as total FROM projetos;
SELECT 'Contagem Clientes' as info, COUNT(*) as total FROM clientes;
