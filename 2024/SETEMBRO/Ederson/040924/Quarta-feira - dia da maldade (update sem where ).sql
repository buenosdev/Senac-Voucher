-- ====================
-- UPDATEs para as Tabelas
-- ====================

-- Atualizar o nome da cidade dependendo da primeira letra (A até M e N até Z):
UPDATE cidade
SET cidade = CASE 
    WHEN cidade LIKE '[A-M]%' THEN 'Abaixo de M'
    ELSE 'Acima de M'
END;

-- Atualizar os estados para suas respectivas regiões:
UPDATE estado
SET estado = CASE
    WHEN estado IN ('Mato Grosso do Sul', 'Mato Grosso', 'Goiás', 'Distrito Federal') THEN 'Centro Oeste'
    WHEN estado IN ('São Paulo', 'Rio de Janeiro', 'Espírito Santo', 'Minas Gerais') THEN 'Sudeste'
    WHEN estado IN ('Paraná', 'Santa Catarina', 'Rio Grande do Sul') THEN 'Sul'
    WHEN estado IN ('Bahia', 'Sergipe', 'Alagoas', 'Pernambuco', 'Paraíba', 'Rio Grande do Norte', 'Ceará', 'Piauí', 'Maranhão') THEN 'Nordeste'
    WHEN estado IN ('Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins') THEN 'Norte'
    ELSE estado
END;

-- Atualizar nacionalidade para "Fora do Brasil":
UPDATE nacionalidade
SET nacionalidade = 'Fora do Brasil';

-- Atualizar todas as raças para "Seres Humanos":
UPDATE raca
SET raca = 'Seres Humanos';

-- Atualizar escolaridade para "Ensino Básico" ou "Ensino Avançado" dependendo do nível:
UPDATE escolaridade
SET escolaridade = CASE
    WHEN escolaridade IN ('Ensino Fundamental', 'Ensino Médio') THEN 'Ensino Básico'
    WHEN escolaridade IN ('Graduação', 'Pós-graduação', 'Mestrado', 'Doutorado') THEN 'Ensino Avançado'
    ELSE escolaridade
END;

-- ====================
-- SELECTs conforme solicitado
-- ====================

-- SELECT com nome e cidade:
SELECT c.nome, ci.cidade
FROM cadastro c
JOIN cidade ci ON c.id_cidade = ci.id_cidade;

-- SELECT com nome e estado:
SELECT c.nome, e.estado
FROM cadastro c
JOIN cidade ci ON c.id_cidade = ci.id_cidade
JOIN estado e ON ci.id_estado = e.id_estado;

-- SELECT com nome, CPF e raça:
SELECT c.nome, c.cpf, r.raca
FROM cadastro c
JOIN raca r ON c.id_raca = r.id_raca;

-- SELECT com nome e nacionalidade:
SELECT c.nome, n.nacionalidade
FROM cadastro c
JOIN nacionalidade n ON c.id_nacionalidade = n.id_nacionalidade;

-- SELECT com nome e escolaridade:
SELECT c.nome, es.escolaridade
FROM cadastro c
JOIN escolaridade es ON c.id_escolaridade = es.id_escolaridade;

-- SELECT com nome, cidade e estado:
SELECT c.nome, ci.cidade, e.estado
FROM cadastro c
JOIN cidade ci ON c.id_cidade = ci.id_cidade
JOIN estado e ON ci.id_estado = e.id_estado;

-- SELECT completo com nome, cidade, estado, fone, RG, sexo, nacionalidade, raça, escolaridade:
SELECT c.nome, ci.cidade, e.estado, c.fone, c.rg, s.sexo, n.nacionalidade, r.raca, es.escolaridade
FROM cadastro c
JOIN cidade ci ON c.id_cidade = ci.id_cidade
JOIN estado e ON ci.id_estado = e.id_estado
JOIN sexo s ON c.id_sexo = s.id_sexo
JOIN nacionalidade n ON c.id_nacionalidade = n.id_nacionalidade
JOIN raca r ON c.id_raca = r.id_raca
JOIN escolaridade es ON c.id_escolaridade = es.id_escolaridade;
