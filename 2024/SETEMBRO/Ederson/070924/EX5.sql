-- 5. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
-- Criar a tabela chamada Curso para conter os dados: idCurso, nome (tamanho 50), sigla
-- (tamanho 3), coordenador, sendo que idCurso é a chave primária da tabela.
-- Inserir dados na tabela, procure inserir pelo menos 3 cursos.
-- Execute os comandos para:
-- a) Exibir todos os dados da tabela.
-- b) Exibir apenas os coordenadores dos cursos.
-- c) Exibir apenas os dados dos cursos de uma determinada sigla.
-- d) Exibir os dados da tabela ordenados pelo nome do curso.
-- e) Exibir os dados da tabela ordenados pelo nome do coordenador em ordem
-- decrescente.
-- f) Exibir os dados da tabela, dos cursos cujo nome comece com uma determinada letra.
-- g) Exibir os dados da tabela, dos cursos cujo nome termine com uma determinada letra.
-- h) Exibir os dados da tabela, dos cursos cujo nome tenha como segunda letra uma
-- determinada letra.
-- i) Exibir os dados da tabela, dos cursos cujo nome tenha como penúltima letra uma
-- determinada letra.
-- j) Elimine a tabela.

-- 1. Criar a tabela Curso
CREATE TABLE Curso (
    idCurso INT PRIMARY KEY, -- Chave primária para identificar o curso
    nome VARCHAR(50), -- Nome do curso, tamanho máximo de 50 caracteres
    sigla VARCHAR(3), -- Sigla do curso, tamanho máximo de 3 caracteres
    coordenador VARCHAR(50) -- Nome do coordenador, tamanho máximo de 50 caracteres
);

-- 2. Inserir dados na tabela Curso
-- Inserindo 3 cursos com seus respectivos coordenadores
INSERT INTO Curso (idCurso, nome, sigla, coordenador) VALUES
(1, 'Ciência da Computação', 'CPC', 'Dr. João Silva'),
(2, 'Engenharia Civil', 'ENC', 'Dra. Maria Santos'),
(3, 'Administração', 'ADM', 'Dr. Carlos Oliveira');

-- a) Exibir todos os dados da tabela Curso
SELECT * FROM Curso;

-- b) Exibir apenas os coordenadores dos cursos
SELECT coordenador FROM Curso;

-- c) Exibir apenas os dados dos cursos de uma determinada sigla (Exemplo: sigla = 'CPC')
SELECT * FROM Curso
WHERE sigla = 'CPC';

-- d) Exibir os dados da tabela ordenados pelo nome do curso
SELECT * FROM Curso
ORDER BY nome;

-- e) Exibir os dados da tabela ordenados pelo nome do coordenador em ordem decrescente
SELECT * FROM Curso
ORDER BY coordenador DESC;

-- f) Exibir os dados da tabela dos cursos cujo nome comece com uma determinada letra (Exemplo: 'C')
SELECT * FROM Curso
WHERE nome LIKE 'C%';

-- g) Exibir os dados da tabela dos cursos cujo nome termine com uma determinada letra (Exemplo: 'a')
SELECT * FROM Curso
WHERE nome LIKE '%a';

-- h) Exibir os dados da tabela dos cursos cujo nome tenha como segunda letra uma determinada letra (Exemplo: 'i')
SELECT * FROM Curso
WHERE nome LIKE '_i%';

-- i) Exibir os dados da tabela dos cursos cujo nome tenha como penúltima letra uma determinada letra (Exemplo: 'ã')
SELECT * FROM Curso
WHERE nome LIKE '%ã_';

-- j) Eliminar a tabela Curso
DROP TABLE Curso;
