-- CRIAÇÃO DO BANCO DE DADOS E TABELAS

-- Tabela cadastro de clientes (CPF, nome, RG, Id_cidade, id_Sexo, Id_Nacionalidade, Fone, Id_raca, Id_escolaridade)
-- Tabela estado (Id_estado, Estado)
-- Tabela cidade (Id_cidade, Cidade, Id_estado,)
-- Tabela Sexo (Id_sexo, Sexo)
-- Tabela Nacionalidade (Id_nacionalidade, Nacionalidade)
-- Tabela  Raça(Id_raca, raca)
-- Tabela Escolaridade (Id_escolaridade, Escolaridade)



create database cadastro;

use cadastro;

create table cadastro_cliente (
    cpf varchar(14) primary key, -- Fiz o cpf pensando que fosse 14 unicamente
    nome varchar(100),
    rg varchar(15), -- Mesma coisa com o rg
    id_cidade int,
    id_sexo int,
    id_nacionalidade int,
    fone varchar(15), -- E com o fone (numero de telefone)
    id_raca int,
    id_escolaridade int,
    foreign key (id_cidade) references cidade(id_cidade), -- Nesses todos de baixo fiz as chaves estrangeiras
    foreign key (id_sexo) references sexo(id_sexo),
    foreign key (id_nacionalidade) references nacionalidade(id_nacionalidade),
    foreign key (id_raca) references raca(id_raca),
    foreign key (id_escolaridade) references escolaridade(id_escolaridade)
);

create table cidade (
    id_cidade int primary key,
    cidade varchar(100),
    id_estado int,
    foreign key (id_estado) references estado(id_estado)
);

create table estado (
    id_estado int primary key,
    estado varchar(100)
);

create table sexo (
    id_sexo int primary key,
    sexo varchar(12) -- Coloquei 12 pois vou pensar no que colocar como 3º sexo
);

create table nacionalidade (
    id_nacionalidade int primary key,
    nacionalidade varchar(50)
);

create table raca (
    id_raca int primary key,
    raca varchar(50)
);

create table escolaridade (
    id_escolaridade int primary key,
    escolaridade varchar(50)
);

-- ADICIONANDO VALORES

-- Incluir no mínimo 20 cadastros;
-- Incluir todos os Estados do Brasil;
-- Incluir pelo menos 5 cidades de cada estado;
-- Incluir no mínimo 3 sexos;
-- Incluir nacionalidade (brasileira e estrangeira)
-- Incluir no mínimo 5 raças
-- Incluir no mínimo 8 tipos de escolaridades

-- Inserir Estados do Brasil
insert into estado (id_estado, estado) values
(1, 'Bahia'),
(2, 'Goiás'),
(3, 'Rio de Janeiro'),
(4, 'São Paulo'),
(5, 'Rio Grande do Sul'),
(6, 'Minas Gerais'),
(7, 'Paraná'),
(8, 'Santa Catarina'),
(9, 'Amazonas'),
(10, 'Pará'),
(11, 'Pernambuco'),
(12, 'Mato Grosso'),
(13, 'Maranhão'),
(14, 'Mato Grosso do Sul'),
(15, 'Sergipe'),
(16, 'Espírito Santo'),
(17, 'Rio Grande do Norte'),
(18, 'Piauí'),
(19, 'Tocantins'),
(20, 'Paraíba'),
(21, 'Alagoas'),
(22, 'Rondônia'),
(23, 'Roraima'),
(24, 'Amapá'),
(25, 'Acre');

-- Inserir Cidades (5 por estado)
-- Exemplo para o estado de São Paulo (id_estado = 23)
insert into cidade (id_cidade, cidade, id_estado) values
(1, 'São Paulo', 4),
(2, 'Campinas', 4),
(3, 'Santos', 4),
(4, 'São Bernardo do Campo', 4),
(5, 'São José dos Campos', 4);

-- Inserir Sexos
insert into sexo (id_sexo, sexo) values
(1, 'Masculino'),
(2, 'Feminino'),
(3, 'Outros');

-- Inserir Nacionalidades
insert into nacionalidade (id_nacionalidade, nacionalidade) values
(1, 'Brasileira'),
(2, 'Estrangeira');

-- Inserir Raças
insert into raca (id_raca, raca) values
(1, 'Branca'),
(2, 'Parda'),
(3, 'Preta'),
(4, 'Amarela'),
(5, 'Indígena');

-- Inserir Escolaridades
insert into escolaridade (id_escolaridade, escolaridade) values
(1, 'Ensino Fundamental Incompleto'),
(2, 'Ensino Fundamental Completo'),
(3, 'Ensino Médio Incompleto'),
(4, 'Ensino Médio Completo'),
(5, 'Ensino Superior Incompleto'),
(6, 'Ensino Superior Completo'),
(7, 'Pós-Graduação Incompleta'),
(8, 'Pós-Graduação Completa');

-- Inserir Cadastros de Clientes
insert into cadastro_cliente (cpf, nome, rg, id_cidade, id_sexo, id_nacionalidade, fone, id_raca, id_escolaridade) values
('123.456.789-00', 'João Silva', 'MG1234567', 1, 1, 1, '1234-5678', 1, 6), -- Nesse eu inventei o RG, CPF e Fone
('234.567.890-11', 'Maria Oliveira', 'SP2345678', 2, 2, 1, '2345-6789', 2, 4),
('345.678.901-22', 'Pedro Santos', 'RJ3456789', 3, 1, 1, '3456-7890', 3, 7),
('456.789.012-33', 'Ana Costa', 'RS4567890', 4, 2, 2, '4567-8901', 4, 2),
('567.890.123-44', 'Lucas Almeida', 'PR5678901', 5, 1, 1, '5678-9012', 5, 6),
('678.901.234-55', 'Beatriz Lima', 'BA6789012', 1, 2, 2, '6789-0123', 1, 4),
('789.012.345-66', 'Carlos Pereira', 'CE7890123', 2, 1, 1, '7890-1234', 2, 5),
('890.123.456-77', 'Juliana Souza', 'MG8901234', 3, 2, 1, '8901-2345', 3, 8),
('901.234.567-88', 'Roberto Ferreira', 'SP9012345', 4, 1, 2, '9012-3456', 3,8);

-- Visualizar tudo isso (W.I.P)

SELECT cadastro_cliente.nome, cidade.nome
FROM cadastro_cliente 
JOIN cidade ON cadastro_cliente.id_cidade = cidade.id_cidade;

select * from cidade;
select * from cadastro_cliente;

describe cidade;



