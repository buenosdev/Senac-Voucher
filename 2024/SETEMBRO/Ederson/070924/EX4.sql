-- 4. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
-- Criar a tabela chamada Professor para conter os dados: idProfessor, nome (tamanho 50),
-- especialidade (tamanho 40), dtNasc (date), sendo que idProfessor é a chave primária da
-- tabela.
-- Exemplo do campo data: ‘AAAA-MM-DD’, ‘1983-10-13’.
-- Inserir dados na tabela, procurando colocar uma especialista para mais de um professor.
-- Procure inserir pelo menos uns 6 professores.
-- Execute os comandos para:
-- a) Exibir todos os dados da tabela.
-- b) Adicionar o campo funcao do tipo varchar(50), onde a função só pode ser ‘monitor’,
-- ‘assistente’ ou ‘titular’;
-- c) Atualizar os professores inseridos e suas respectivas funções;
-- d) Inserir um novo professor;
-- e) Excluir o professor onde o idProfessor é igual a 5;
-- f) Exibir apenas os nomes dos professores titulares;
-- g) Exibir apenas as especialidades e as datas de nascimento dos professores monitores;
-- h) Atualizar a data de nascimento do idProfessor igual a 3;
-- i) Limpar a tabela Professor;

-- 1. Criar a tabela Professor
CREATE TABLE Professor (
    idProfessor INT PRIMARY KEY, -- Chave primária para identificar o professor
    nome VARCHAR(50), -- Nome do professor, tamanho máximo de 50 caracteres
    especialidade VARCHAR(40), -- Especialidade do professor, tamanho máximo de 40 caracteres
    dtNasc DATE -- Data de nascimento do professor no formato 'AAAA-MM-DD'
);

-- 2. Inserir dados na tabela Professor
-- Inserindo 6 professores, com mais de um professor por especialidade
INSERT INTO Professor (idProfessor, nome, especialidade, dtNasc) VALUES
(1, 'João Silva', 'Matemática', '1983-10-13'),
(2, 'Ana Costa', 'Física', '1975-06-21'),
(3, 'Carlos Souza', 'Matemática', '1990-01-12'),
(4, 'Mariana Oliveira', 'Química', '1988-03-25'),
(5, 'Fernanda Lima', 'Física', '1985-07-14'),
(6, 'Pedro Santos', 'Química', '1982-09-10');

-- a) Exibir todos os dados da tabela Professor
SELECT * FROM Professor;

-- b) Adicionar o campo funcao do tipo VARCHAR(50), onde a função só pode ser 'monitor', 'assistente' ou 'titular'
ALTER TABLE Professor
ADD funcao VARCHAR(50) CHECK (funcao IN ('monitor', 'assistente', 'titular'));

-- c) Atualizar os professores inseridos e suas respectivas funções
UPDATE Professor
SET funcao = 'titular'
WHERE idProfessor = 1;

UPDATE Professor
SET funcao = 'assistente'
WHERE idProfessor = 2;

UPDATE Professor
SET funcao = 'monitor'
WHERE idProfessor = 3;

UPDATE Professor
SET funcao = 'titular'
WHERE idProfessor = 4;

UPDATE Professor
SET funcao = 'assistente'
WHERE idProfessor = 5;

UPDATE Professor
SET funcao = 'monitor'
WHERE idProfessor = 6;

-- d) Inserir um novo professor
INSERT INTO Professor (idProfessor, nome, especialidade, dtNasc, funcao) 
VALUES (7, 'Lucas Martins', 'Biologia', '1987-02-11', 'monitor');

-- e) Excluir o professor onde o idProfessor é igual a 5
DELETE FROM Professor
WHERE idProfessor = 5;

-- f) Exibir apenas os nomes dos professores titulares
SELECT nome
FROM Professor
WHERE funcao = 'titular';

-- g) Exibir apenas as especialidades e as datas de nascimento dos professores monitores
SELECT especialidade, dtNasc
FROM Professor
WHERE funcao = 'monitor';

-- h) Atualizar a data de nascimento do professor com idProfessor igual a 3
UPDATE Professor
SET dtNasc = '1992-04-15'
WHERE idProfessor = 3;

-- i) Limpar a tabela Professor (remover todos os registros)
TRUNCATE TABLE Professor;
