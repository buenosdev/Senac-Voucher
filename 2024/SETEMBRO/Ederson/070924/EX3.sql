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


-- 1. Usar o banco de dados 'sprint'
USE sprint;

-- 2. Criar a tabela Filme
CREATE TABLE Filme (
    idFilme INT PRIMARY KEY, -- Chave primária para identificar o filme
    titulo VARCHAR(50), -- Título do filme, tamanho máximo de 50 caracteres
    genero VARCHAR(40), -- Gênero do filme, tamanho máximo de 40 caracteres
    diretor VARCHAR(40) -- Nome do diretor, tamanho máximo de 40 caracteres
);

-- 3. Inserir dados na tabela Filme
-- Pelo menos 7 filmes, com um gênero repetido e um diretor repetido
INSERT INTO Filme (idFilme, titulo, genero, diretor) VALUES
(1, 'Inception', 'Ficção Científica', 'Christopher Nolan'),
(2, 'Interstellar', 'Ficção Científica', 'Christopher Nolan'),
(3, 'The Dark Knight', 'Ação', 'Christopher Nolan'),
(4, 'Pulp Fiction', 'Crime', 'Quentin Tarantino'),
(5, 'Django Unchained', 'Western', 'Quentin Tarantino'),
(6, 'The Matrix', 'Ficção Científica', 'Lana Wachowski, Lilly Wachowski'),
(7, 'Kill Bill: Vol. 1', 'Ação', 'Quentin Tarantino');


-- 1. Exibir todos os dados da tabela Filme
SELECT * FROM Filme;

-- 2. Adicionar o campo protagonista do tipo VARCHAR(50) na tabela Filme
ALTER TABLE Filme
ADD protagonista VARCHAR(50);

-- 3. Atualizar o campo protagonista de todos os filmes inseridos
UPDATE Filme
SET protagonista = 'Leonardo DiCaprio'
WHERE idFilme = 1;

UPDATE Filme
SET protagonista = 'Matthew McConaughey'
WHERE idFilme = 2;

UPDATE Filme
SET protagonista = 'Christian Bale'
WHERE idFilme = 3;

UPDATE Filme
SET protagonista = 'John Travolta'
WHERE idFilme = 4;

UPDATE Filme
SET protagonista = 'Jamie Foxx'
WHERE idFilme = 5;

UPDATE Filme
SET protagonista = 'Keanu Reeves'
WHERE idFilme = 6;

UPDATE Filme
SET protagonista = 'Uma Thurman'
WHERE idFilme = 7;

-- 4. Modificar o campo diretor para aumentar o tamanho de 40 para 150 caracteres
ALTER TABLE Filme
MODIFY diretor VARCHAR(150);

-- 5. Atualizar o diretor do filme com id=5
UPDATE Filme
SET diretor = 'Lana Wachowski, Lilly Wachowski'
WHERE idFilme = 5;

-- 6. Atualizar o diretor dos filmes com id=2 e id=7
UPDATE Filme
SET diretor = 'Denis Villeneuve'
WHERE idFilme = 2;

UPDATE Filme
SET diretor = 'Guillermo del Toro'
WHERE idFilme = 7;

-- 7. Atualizar o título do filme com o id=6
UPDATE Filme
SET titulo = 'The Matrix Resurrections'
WHERE idFilme = 6;

-- 8. Excluir o filme com o id=3
DELETE FROM Filme
WHERE idFilme = 3;

-- 9. Exibir os filmes em que o gênero é diferente de "Drama"
SELECT * FROM Filme
WHERE genero <> 'Drama';

-- 10. Exibir os dados dos filmes cujo gênero é igual a "Suspense"
SELECT * FROM Filme
WHERE genero = 'Suspense';

-- 11. Descrever os campos da tabela, mostrando as atualizações feitas nos campos protagonista e diretor
DESCRIBE Filme;

-- 12. Limpar todos os dados da tabela (remover todos os registros)
TRUNCATE TABLE Filme;
