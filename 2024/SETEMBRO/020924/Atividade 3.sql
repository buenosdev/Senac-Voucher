create table fornecedores(
    cod_forne varchar(20) primary key,
    nome varchar(255),
    cidade_sede varchar(255),
    grupo_cod_fornecedor varchar(20)
);

create table material (
    cod_material int primary key,
    cod_fornecedor varchar(20),
    nome varchar(255),
    descricao text,
    foreign key (cod_fornecedor) references fornecedores(cod_forne)
);



insert into fornecedores (cod_forne, nome, cidade_sede, grupo_cod_fornecedor)
values
('ABC', 'ABC Materiais Eletricos', 'Vitoria', NULL),
('XYZ', 'XYZ Materiais de Escritorio', 'Rio de Janeiro', 'HiX'),
('Hidra', 'Hidra Materiais Hidraulicos', 'Sao Paulo', 'HiX'),
('HiX', 'HidraX Materiais Elétricos e Hidraulicos', 'Sao Paulo', NULL);


insert into material (cod_material, cod_fornecedor, nome, descricao)
values
(123, 'ABC', 'Tomada eletrica 10A Nova', 'Tomada eletrica 10A padrao novo'),
(234, 'ABC', 'Disjuntor 25A', 'Disjuntor eletrico 25A'),
(345, 'XYZ', 'Resma Papel A4', 'Resma papel branco A4'),
(456, 'XYZ', 'Toner Imp HR5522', 'Toner impressora HR5522'),
(678, 'Hidra', 'Cano PVC 1/2', 'Cano PVC 1/2 pol'),
(679, 'Hidra', 'Cano PVC 3/4', 'Cano PVC 3/4 pol'),
(680, 'Hidra', 'Medidor hidr 1/2', 'Medidor hidraulico 1/2 pol'),
(681, 'Hidra', 'Joelho 1/2', 'Conector Joelho 1/2 pol'),
(682, 'Hidra', 'Junta 1/2', 'Cano PVC 1/2 pol'),
(1234, 'ABC', 'Tomada eletrica 20A Nova', 'Tomada eletrica 20A padrao novo'),
(2345, 'XYZ', 'Caneta Azul', 'Caneta esferografica azul'),
(4567, 'XYZ', 'Grampeador', 'Grampeador mesa pequeno'),
(4568, 'XYZ', 'Caneta Marca Texto Amarela', 'Caneta Marca Texto Amarela'),
(4569, 'XYZ', 'Lapis HB', 'Lapis Preto HB');


select
    material.cod_material,
    material.nome as nome_material,
    material.descricao,
    fornecedores.nome as nome_fornecedor,
    fornecedores.cidade_sede
from
    material
join
    fornecedores on material.cod_fornecedor = fornecedores.cod_forne;
