-- 1. No MySQL Workbench, crie o banco de dados ‘sprint’:
-- Escreva e execute os comandos para:
-- • Criar a tabela chamada Atleta para conter os dados: idAtleta (int e chave primária da
-- tabela), nome (varchar, tamanho 40), modalidade (varchar, tamanho 40), qtdMedalha
-- (int, representando a quantidade de medalhas que o atleta possui)
-- • Inserir dados na tabela, procurando colocar mais de um atleta para cada modalidade
-- e pelo menos 5 atletas.
-- Escreva e execute os comandos para:
-- • Exibir todos os dados da tabela.
-- • Atualizar a quantidade de medalhas do atleta com id=1;
-- • Atualizar a quantidade de medalhas do atleta com id=2 e com o id=3;
-- • Atualizar o nome do atleta com o id=4;
-- • Adicionar o campo dtNasc na tabela, com a data de nascimento dos atletas, tipo date;
-- • Atualizar a data de nascimento de todos os atletas;
-- • Excluir o atleta com o id=5;
-- • Exibir os atletas onde a modalidade é diferente de natação;
-- • Exibir os dados dos atletas que tem a quantidade de medalhas maior ou igual a 3;
-- • Modificar o campo modalidade do tamanho 40 para o tamanho 60;
-- • Descrever os campos da tabela mostrando a atualização do campo modalidade;
-- • Limpar os dados da tabela;


CREATE DATABASE sprint;


USE sprint;

-- 3. Criar a tabela Atleta
CREATE TABLE Atleta (
    idAtleta INT PRIMARY KEY, -- Chave primária para identificar o atleta
    nome VARCHAR(40), -- Nome do atleta, tamanho máximo de 40 caracteres
    modalidade VARCHAR(40), -- Modalidade esportiva, tamanho máximo de 40 caracteres
    qtdMedalha INT -- Quantidade de medalhas
);

-- 4. Inserir dados na tabela Atleta (pelo menos 5 atletas e mais de um atleta por modalidade)
INSERT INTO Atleta (idAtleta, nome, modalidade, qtdMedalha) VALUES
(1, 'João Silva', 'Natação', 5),
(2, 'Maria Souza', 'Natação', 3),
(3, 'Carlos Mendes', 'Atletismo', 2),
(4, 'Ana Paula', 'Atletismo', 4),
(5, 'Pedro Santos', 'Ciclismo', 1);

-- 5. Exibir todos os dados da tabela Atleta
SELECT * FROM Atleta;

-- 6. Atualizar a quantidade de medalhas do atleta com id=1
UPDATE Atleta
SET qtdMedalha = 6
WHERE idAtleta = 1;

-- 7. Atualizar a quantidade de medalhas dos atletas com id=2 e id=3
UPDATE Atleta
SET qtdMedalha = 4
WHERE idAtleta = 2;

UPDATE Atleta
SET qtdMedalha = 3
WHERE idAtleta = 3;

-- 8. Atualizar o nome do atleta com id=4
UPDATE Atleta
SET nome = 'Ana Paula Santos'
WHERE idAtleta = 4;

-- 9. Adicionar o campo dtNasc (data de nascimento) à tabela Atleta
ALTER TABLE Atleta
ADD dtNasc DATE;

-- 10. Atualizar a data de nascimento de todos os atletas
UPDATE Atleta
SET dtNasc = '1990-05-15'
WHERE idAtleta = 1;

UPDATE Atleta
SET dtNasc = '1992-07-20'
WHERE idAtleta = 2;

UPDATE Atleta
SET dtNasc = '1988-03-22'
WHERE idAtleta = 3;

UPDATE Atleta
SET dtNasc = '1995-10-10'
WHERE idAtleta = 4;

UPDATE Atleta
SET dtNasc = '1991-08-30'
WHERE idAtleta = 5;

-- 11. Excluir o atleta com o id=5
DELETE FROM Atleta
WHERE idAtleta = 5;

-- 12. Exibir os atletas cuja modalidade é diferente de "Natação"
SELECT * FROM Atleta
WHERE modalidade <> 'Natação';

-- 13. Exibir os dados dos atletas que têm quantidade de medalhas maior ou igual a 3
SELECT * FROM Atleta
WHERE qtdMedalha >= 3;

-- 14. Modificar o campo modalidade de tamanho 40 para 60
ALTER TABLE Atleta
MODIFY modalidade VARCHAR(60);

-- 15. Descrever os campos da tabela para verificar a atualização do campo modalidade
DESCRIBE Atleta;

-- 16. Limpar todos os dados da tabela (remover todos os registros)
TRUNCATE TABLE Atleta;
