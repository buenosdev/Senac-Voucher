-- 6. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
-- Você vai criar uma tabela para armazenar os dados de revistas (como por ex: Veja, Isto é,
-- Epoca, Quatro Rodas, Claudia, etc).
-- Escreva e execute os comandos para:
-- • Criar a tabela chamada Revista para conter os campos: idRevista (int e chave
-- primária da tabela), nome (varchar, tamanho 40), categoria (varchar, tamanho 30). Os
-- valores de idRevista devem iniciar com o valor 1 e ser incrementado automaticamente
-- pelo sistema.
-- • Inserir 4 registros na tabela, mas sem informar a categoria.
-- Escreva e execute os comandos para:
-- • Exibir todos os dados da tabela.
-- • Atualize os dados das categorias das 3 revistas inseridas. Exibir os dados da tabela
-- novamente para verificar se atualizou corretamente.
-- • Insira mais 3 registros completos.
-- • Exibir novamente os dados da tabela.
-- • Exibir a descrição da estrutura da tabela.
-- • Alterar a tabela para que a coluna categoria possa ter no máximo 40 caracteres.
-- • Exibir novamente a descrição da estrutura da tabela, para verificar se alterou o
-- tamanho da coluna categoria
-- • Acrescentar a coluna periodicidade à tabela, que é varchar(15).
-- • Exibir os dados da tabela.
-- • Excluir a coluna periodicidade da tabela.

-- 1. Criar a tabela Revista com idRevista auto-incrementado
CREATE TABLE Revista (
    idRevista INT AUTO_INCREMENT PRIMARY KEY, -- idRevista auto-incrementado, chave primária
    nome VARCHAR(40), -- Nome da revista, tamanho máximo de 40 caracteres
    categoria VARCHAR(30) -- Categoria da revista, tamanho máximo de 30 caracteres
);

-- 2. Inserir 4 registros na tabela sem informar a categoria
INSERT INTO Revista (nome) VALUES
('Veja'),
('Isto É'),
('Época'),
('Quatro Rodas');

-- 3. Exibir todos os dados da tabela Revista
SELECT * FROM Revista;

-- 4. Atualizar os dados das categorias das 3 revistas inseridas e exibir novamente os dados
UPDATE Revista
SET categoria = 'Notícias'
WHERE idRevista = 1;

UPDATE Revista
SET categoria = 'Política'
WHERE idRevista = 2;

UPDATE Revista
SET categoria = 'Atualidades'
WHERE idRevista = 3;

-- Exibir novamente os dados para verificar se a atualização foi feita corretamente
SELECT * FROM Revista;

-- 5. Inserir mais 3 registros completos (com nome e categoria)
INSERT INTO Revista (nome, categoria) VALUES
('Claudia', 'Moda'),
('Superinteressante', 'Ciência'),
('Caras', 'Entretenimento');

-- 6. Exibir novamente os dados da tabela
SELECT * FROM Revista;

-- 7. Exibir a descrição da estrutura da tabela
DESCRIBE Revista;

-- 8. Alterar a tabela para que a coluna categoria tenha no máximo 40 caracteres
ALTER TABLE Revista
MODIFY categoria VARCHAR(40);

-- 9. Exibir novamente a descrição da estrutura da tabela para verificar a alteração
DESCRIBE Revista;

-- 10. Acrescentar a coluna periodicidade à tabela, que é do tipo varchar(15)
ALTER TABLE Revista
ADD periodicidade VARCHAR(15);

-- 11. Exibir os dados da tabela para verificar a nova coluna
SELECT * FROM Revista;

-- 12. Excluir a coluna periodicidade da tabela
ALTER TABLE Revista
DROP COLUMN periodicidade;

-- 13. Exibir os dados da tabela para confirmar que a coluna foi removida
SELECT * FROM Revista;
