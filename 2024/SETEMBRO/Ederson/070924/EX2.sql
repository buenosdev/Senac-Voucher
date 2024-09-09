-- 2. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
-- Criar a tabela chamada Musica para conter os dados: idMusica, titulo (tamanho 40), artista
-- (tamanho 40), genero (tamanho 40), sendo que idMusica é a chave primária da tabela.
-- Inserir dados na tabela, procurando colocar um gênero de música que tenha mais de uma
-- música, e um artista, que tenha mais de uma música cadastrada. Procure inserir pelo
-- menos umas 7 músicas.
-- Execute os comandos para:
-- a) Exibir todos os dados da tabela.
-- b) Adicionar o campo curtidas do tipo int na tabela;
-- c) Atualizar o campo curtidas de todas as músicas inseridas;
-- d) Modificar o campo artista do tamanho 40 para o tamanho 80;
-- e) Atualizar a quantidade de curtidas da música com id=1;
-- f) Atualizar a quantidade de curtidas das músicas com id=2 e com o id=3;
-- g) Atualizar o nome da música com o id=5;
-- h) Excluir a música com o id=4;
-- i) Exibir as músicas onde o gênero é diferente de funk;
-- j) Exibir os dados das músicas que tem curtidas maior ou igual a 20;
-- k) Descrever os campos da tabela mostrando a atualização do campo artista;
-- l) Limpar os dados da tabela;

-- 1. Criar a tabela Musica
CREATE TABLE Musica (
    idMusica INT PRIMARY KEY, -- Chave primária para identificar a música
    titulo VARCHAR(40), -- Título da música, tamanho máximo de 40 caracteres
    artista VARCHAR(40), -- Nome do artista, tamanho máximo de 40 caracteres
    genero VARCHAR(40) -- Gênero da música, tamanho máximo de 40 caracteres
);

-- 2. Inserir dados na tabela Musica
-- Inserindo 7 músicas com pelo menos um gênero repetido e um artista repetido
INSERT INTO Musica (idMusica, titulo, artista, genero) VALUES
(1, 'Blinding Lights', 'The Weeknd', 'Pop'),
(2, 'Levitating', 'Dua Lipa', 'Pop'),
(3, 'Save Your Tears', 'The Weeknd', 'Pop'),
(4, 'Shape of You', 'Ed Sheeran', 'Pop'),
(5, 'Bohemian Rhapsody', 'Queen', 'Rock'),
(6, 'Smells Like Teen Spirit', 'Nirvana', 'Rock'),
(7, 'Bad Habits', 'Ed Sheeran', 'Pop');

-- a) Exibir todos os dados da tabela Musica
SELECT * FROM Musica;

-- b) Adicionar o campo curtidas do tipo int na tabela Musica
ALTER TABLE Musica
ADD curtidas INT;

-- c) Atualizar o campo curtidas de todas as músicas inseridas
UPDATE Musica
SET curtidas = 50
WHERE idMusica = 1;

UPDATE Musica
SET curtidas = 45
WHERE idMusica = 2;

UPDATE Musica
SET curtidas = 40
WHERE idMusica = 3;

UPDATE Musica
SET curtidas = 55
WHERE idMusica = 4;

UPDATE Musica
SET curtidas = 70
WHERE idMusica = 5;

UPDATE Musica
SET curtidas = 65
WHERE idMusica = 6;

UPDATE Musica
SET curtidas = 35
WHERE idMusica = 7;

-- d) Modificar o campo artista para aumentar o tamanho de 40 para 80 caracteres
ALTER TABLE Musica
MODIFY artista VARCHAR(80);

-- e) Atualizar a quantidade de curtidas da música com id=1
UPDATE Musica
SET curtidas = 60
WHERE idMusica = 1;

-- f) Atualizar a quantidade de curtidas das músicas com id=2 e id=3
UPDATE Musica
SET curtidas = 50
WHERE idMusica = 2;

UPDATE Musica
SET curtidas = 45
WHERE idMusica = 3;

-- g) Atualizar o nome da música com id=5
UPDATE Musica
SET titulo = 'Bohemian Rhapsody (Remastered)'
WHERE idMusica = 5;

-- h) Excluir a música com id=4
DELETE FROM Musica
WHERE idMusica = 4;

-- i) Exibir as músicas onde o gênero é diferente de funk
SELECT * FROM Musica
WHERE genero <> 'Funk';

-- j) Exibir os dados das músicas que têm curtidas maior ou igual a 20
SELECT * FROM Musica
WHERE curtidas >= 20;

-- k) Descrever os campos da tabela, mostrando a atualização do campo artista
DESCRIBE Musica;

-- l) Limpar os dados da tabela (remover todos os registros)
TRUNCATE TABLE Musica;
