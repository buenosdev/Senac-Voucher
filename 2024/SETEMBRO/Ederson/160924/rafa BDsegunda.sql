select * from nota_fiscal;
select * from ordem_servico;
select * from pecas;
select * from tela_cadastro;

show create table nota_fiscal;

show tables;
show table status;

DESC nota_fiscal;

ALTER TABLE nota_fiscal CHANGE COLUMN prazo_entrega_dias prazo_entrega_dias DATE;
ALTER TABLE tela_cadastro modify column cpf_or_cnpj varchar(30) not null;
ALTER TABLE ordem_servico modify column emissao date not null;
ALTER TABLE ordem_servico modify column quantidade int not null;
ALTER TABLE ordem_servico modify column servico varchar(50) not null;


