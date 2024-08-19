USE banco_2;

CREATE TABLE ex2_cliente (
    codcliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    cpf VARCHAR(255) UNIQUE NOT NULL
);


CREATE TABLE ex2_pedido (
    codpedido INT AUTO_INCREMENT PRIMARY KEY,
    codcliente INT,
    data_pedido DATE NOT NULL,
    nf VARCHAR(25),
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (codcliente) REFERENCES ex2_cliente(codcliente)
);

CREATE TABLE ex2_produto (
	codproduto INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255),
    quantidade INT
);

CREATE TABLE ex2_itempedido (
    codproduto INT,
	codpedido INT,
    numeroitem INT,
    valorunitario INT,
    quantidade INT,
    FOREIGN KEY (codpedido) REFERENCES ex2_pedido(codcliente),
	FOREIGN KEY (codproduto) REFERENCES ex2_produto(codproduto)
    
);

CREATE TABLE ex2_log (
	codlog INT AUTO_INCREMENT PRIMARY KEY,
	data DATE NOT NULL,
	descricao VARCHAR(255)
    
);

CREATE TABLE ex2_requisicao_compra(
	codrequisicaocompra INT AUTO_INCREMENT PRIMARY KEY,
	codproduto INT,
	data DATE NOT NULL,
	quantidade INT,
	FOREIGN KEY (codproduto) REFERENCES ex2_produto(codproduto),
	FOREIGN KEY (quantidade) REFERENCES ex2_produto(quantidade)
);


USE escola;

CREATE TABLE alunos (
matricula int(4) AUTO_INCREMENT,
nome varchar(30) not null,
email varchar (50),
primary key (matricula)

);

insert into alunos(matricula,nome,email) values (null,"Davi","davibuenocgd@gmail.com");



INSERT INTO ex2_cliente (nome, data_nascimento, cpf) VALUES
('João da Silva', '1985-03-15', '123.456.789-00'),
('Maria Oliveira', '1990-07-22', '234.567.890-11'),
('Carlos Santos', '1982-11-05', '345.678.901-22'),
('Ana Pereira', '1995-02-28', '456.789.012-33'),
('Pedro Costa', '1988-12-13', '567.890.123-44'),
('Laura Fernandes', '2000-09-17', '678.901.234-55'),
('Roberto Almeida', '1975-04-30', '789.012.345-66'),
('Juliana Souza', '1989-10-11', '890.123.456-77'),
('Ricardo Lima', '1992-05-19', '901.234.567-88'),
('Fernanda Martins', '1987-06-25', '012.345.678-99');


INSERT INTO ex2_produto (descricao, quantidade) VALUES
('Cadeira de Escritório', 15),
('Mesa de Jantar', 10),
('Teclado Mecânico', 25),
('Monitor LED 24"', 20),
('Impressora Multifuncional', 12),
('Mouse Óptico', 30),
('Lâmpada LED', 50),
('Caderno Universitário', 40);

INSERT INTO ex2_pedido (data_pedido, nf, valor_total) VALUES
('2024-08-01', 'NF123456', 150.75),
('2024-08-02', 'NF123457', 320.40),
('2024-08-03', 'NF123458', 45.90),
('2024-08-04', 'NF123459', 250.00),
('2024-08-05', 'NF123460', 89.99),
('2024-08-06', 'NF123461', 120.00),
('2024-08-07', 'NF123462', 55.25),
('2024-08-08', 'NF123463', 300.10);


INSERT INTO ex2_itempedido (numeroitem, valorunitario, quantidade) VALUES
(1, 25.00, 2),   
(2, 150.75, 1),   
(3, 45.90, 3),    
(4, 89.99, 5),    
(5, 120.00, 1),   
(6, 55.25, 4),   
(7, 300.10, 2),   
(8, 75.00, 6);   
