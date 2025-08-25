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

-- Delete o feedback do projeto 'VENDAS V'
DELETE FROM feedbacks 
WHERE projeto_id = (SELECT id FROM projetos WHERE titulo = 'VENDAS V');

-- Alternativa com JOIN:
-- DELETE f FROM feedbacks f
-- JOIN projetos p ON f.projeto_id = p.id
-- WHERE p.titulo = 'VENDAS V';

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

-- Delete o projeto 'LOGISTICA III'
-- Isso deve remover automaticamente alocações relacionadas (CASCADE)
DELETE FROM projetos WHERE titulo = 'LOGISTICA III';

-- ================================
-- EXERCÍCIO 6: REPLACE - Corrigir nota de feedback
-- ================================

-- Use REPLACE para alterar a nota do feedback do projeto 'FINANCEIRO VI' para 5
-- Primeiro precisamos obter todos os dados do feedback existente
REPLACE INTO feedbacks (
    id, 
    projeto_id, 
    nota, 
    comentario
)
SELECT 
    f.id,
    f.projeto_id,
    5,  -- Nova nota
    f.comentario
FROM feedbacks f
JOIN projetos p ON f.projeto_id = p.id
WHERE p.titulo = 'FINANCEIRO VI';

-- Alternativa mais simples se soubermos o ID:
-- REPLACE INTO feedbacks (id, projeto_id, nota, comentario)
-- VALUES (5, 6, 5, 'Boa execução dentro do prazo');

-- ================================
-- EXERCÍCIO 7: ON UPDATE CASCADE - Atualizar ID de cliente
-- ================================

-- Atualize o id do cliente 'EduCare Ensino' de 4 para 40
-- Os projetos deste cliente devem ter cliente_id atualizado automaticamente
UPDATE clientes 
SET id = 40 
WHERE nome = 'EduCare Ensino';

-- ================================
-- VERIFICAÇÕES FINAIS
-- ================================

-- Verificar resultados das operações
SELECT 'CLIENTES' as tabela, id, nome, cidade FROM clientes ORDER BY id;
SELECT 'PROJETOS' as tabela, id, titulo, cliente_id FROM projetos ORDER BY id;
SELECT 'ALOCACOES' as tabela, id, projeto_id, consultor_id, horas_trabalhadas FROM alocacoes ORDER BY id;
SELECT 'FEEDBACKS' as tabela, f.id, p.titulo, f.nota FROM feedbacks f JOIN projetos p ON f.projeto_id = p.id ORDER BY f.id;

-- Contagem de registros para verificar CASCADE
SELECT 'Contagem Alocações' as info, COUNT(*) as total FROM alocacoes;
SELECT 'Contagem Feedbacks' as info, COUNT(*) as total FROM feedbacks;
SELECT 'Contagem Projetos' as info, COUNT(*) as total FROM projetos;
SELECT 'Contagem Clientes' as info, COUNT(*) as total FROM clientes;
