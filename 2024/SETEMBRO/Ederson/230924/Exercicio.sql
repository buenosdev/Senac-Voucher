CREATE DATABASE Banco;

USE Banco;

-- Tabela Cidade
CREATE TABLE Cidade (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único da cidade
    nome VARCHAR(100) NOT NULL           -- Nome da cidade
);

-- Cidades
INSERT INTO Cidade (nome) VALUES
('Campo Grande'),
('Dourados'),
('Três Lagoas'),
('Corumbá'),
('Ponta Porã'),
('Naviraí'),
('Maracaju'),
('Sidrolândia'),
('Aquidauana'),
('Paranaíba'),
('Coxim'),
('Rio Verde de Mato Grosso'),
('Bataguassu'),
('Glória de Dourados'),
('Selvíria'),
('Eldorado'),
('Japorã'),
('Mundo Novo'),
('Ivinhema'),
('Jardim');


-- Tabela Estado
CREATE TABLE Estado (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único do estado
    nome VARCHAR(100) NOT NULL           -- Nome do estado
);

-- Estados
INSERT INTO Estado (nome) VALUES
('Acre'),
('Alagoas'),
('Amapá'),
('Amazonas'),
('Bahia'),
('Ceará'),
('Distrito Federal'),
('Espírito Santo'),
('Goiás'),
('Maranhão'),
('Mato Grosso'),
('Mato Grosso do Sul'),  -- Incluindo Mato Grosso do Sul
('Minas Gerais'),
('Pará'),
('Paraíba'),
('Paraná'),
('Pernambuco'),
('Piauí'),
('Rio de Janeiro'),
('Rio Grande do Norte'),
('Rio Grande do Sul'),
('Rondônia'),
('Roraima'),
('Santa Catarina'),
('São Paulo'),
('Sergipe'),
('Tocantins');


-- Tabela Genero
CREATE TABLE Genero (
    id INT AUTO_INCREMENT PRIMARY KEY,   -- Identificador único do gênero
    descricao VARCHAR(50) NOT NULL       -- Descrição do gênero
);

-- Generos
INSERT INTO Genero (descricao) VALUES
('Masculino'),
('Feminino');

-- Tabela Raca
CREATE TABLE Raca (
    id INT AUTO_INCREMENT PRIMARY KEY,    -- Identificador único da raça
    descricao VARCHAR(50) NOT NULL        -- Descrição da raça
);

-- Raças
INSERT INTO Raca (descricao) VALUES
('Branca'),
('Preta'),
('Parda'),
('Amarela'),
('Indígena'),
('Outra');


-- Tabela Religiao
CREATE TABLE Religiao (
    id INT AUTO_INCREMENT PRIMARY KEY,     -- Identificador único da religião
    descricao VARCHAR(50) NOT NULL         -- Descrição da religião
);

-- Religião
INSERT INTO Religiao (descricao) VALUES
('Cristianismo'),
('Islamismo'),
('Judaísmo'),
('Budismo'),
('Hinduísmo'),
('Ateísmo'),
('Espiritismo'),
('Umbanda'),
('Candomblé'),
('Outras');

-- Tabela Clientes
CREATE TABLE Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,    -- Identificador único do cliente
    nome VARCHAR(100) NOT NULL,           -- Nome do cliente
    cpf VARCHAR(14) UNIQUE NOT NULL,      -- CPF do cliente (único)
    rg VARCHAR(12) NOT NULL,              -- RG do cliente
    data_nascimento DATE NOT NULL,        -- Data de nascimento do cliente
    fone VARCHAR(15),                     -- Telefone do cliente
    endereco VARCHAR(255),                -- Endereço do cliente
    cidade_id INT,                        -- Referência à tabela Cidade
    estado_id INT,                        -- Referência à tabela Estado
    genero_id INT,                        -- Referência à tabela Genero
    raca_id INT,                          -- Referência à tabela Raca
    religiao_id INT,                      -- Referência à tabela Religiao
    estado_civil VARCHAR(50),             -- Estado civil do cliente
    numero_conta VARCHAR(20) UNIQUE NOT NULL, -- Número da conta (único)
    saldo DECIMAL(10, 2) DEFAULT 0.00,    -- Saldo da conta do cliente
    FOREIGN KEY (cidade_id) REFERENCES Cidade(id),  -- Chave estrangeira
    FOREIGN KEY (estado_id) REFERENCES Estado(id),  -- Chave estrangeira
    FOREIGN KEY (genero_id) REFERENCES Genero(id),  -- Chave estrangeira
    FOREIGN KEY (raca_id) REFERENCES Raca(id),      -- Chave estrangeira
    FOREIGN KEY (religiao_id) REFERENCES Religiao(id) -- Chave estrangeira
);

-- Clientes
INSERT INTO Clientes (nome, cpf, rg, data_nascimento, fone, endereco, cidade_id, estado_id, genero_id, raca_id, religiao_id, estado_civil, numero_conta, saldo) VALUES
('Ana Luiza', '999.888.777-66', '99.888.777-2', '1991-06-14', '(67) 90000-0010', 'Rua J, 444', 10, 12, 1, 1, 1, 'Solteiro', '0010', 1500.00),
('Rafaela Vergotti', '444.333.222-11', '44.333.222-3', '1986-01-30', '(67) 89999-0011', 'Avenida K, 555', 11, 12, 2, 2, 2, 'Casada', '0011', 2600.00),
('Luís Cunha', '111.222.333-44', '11.222.333-5', '1989-05-12', '(67) 88888-0012', 'Travessa L, 666', 12, 12, 1, 3, 3, 'Solteiro', '0012', 3200.75),
('Davi Bueno', '777.888.999-00', '77.888.999-6', '1994-03-22', '(67) 87777-0013', 'Rua M, 777', 1, 12, 2, 4, 4, 'Divorciada', '0013', 1800.50),
('Elias Neto', '555.666.777-88', '55.666.777-9', '1987-08-08', '(67) 86666-0014', 'Avenida N, 888', 2, 12, 1, 1, 5, 'Casado', '0014', 2100.00),
('Ederson Roberto', '333.444.555-66', '33.444.555-7', '1990-11-19', '(67) 85555-0015', 'Travessa O, 999', 3, 12, 2, 2, 6, 'Solteira', '0015', 1600.25),
('Édini Zanlucas', '222.333.444-55', '22.333.444-8', '1985-04-27', '(67) 84444-0016', 'Rua P, 101', 4, 12, 1, 3, 7, 'Viúvo', '0016', 2700.00);


-- Tabela Agencias
CREATE TABLE Agencias (
    id INT AUTO_INCREMENT PRIMARY KEY,     -- Identificador único da agência
    numero_agencia VARCHAR(20) NOT NULL UNIQUE, -- Número da agência (único)
    endereco VARCHAR(255),                 -- Endereço da agência
    cidade_id INT,                         -- Referência à tabela Cidade
    estado_id INT,                         -- Referência à tabela Estado
    FOREIGN KEY (cidade_id) REFERENCES Cidade(id), -- Chave estrangeira
    FOREIGN KEY (estado_id) REFERENCES Estado(id)  -- Chave estrangeira
);

-- Agencias
INSERT INTO Agencias (numero_agencia, endereco, cidade_id, estado_id) VALUES
('0001', 'Rua Central, 100', 1, 12),  -- Campo Grande
('0002', 'Avenida Brasil, 200', 2, 12), -- Dourados
('0003', 'Rua do Comércio, 300', 3, 12), -- Três Lagoas
('0004', 'Avenida 14 de Julho, 400', 4, 12), -- Corumbá
('0005', 'Rua da Paz, 500', 5, 12), -- Ponta Porã
('0006', 'Avenida da Integração, 600', 6, 12), -- Naviraí
('0007', 'Rua da Liberdade, 700', 7, 12); -- Maracaju


-- Tabela Saque
CREATE TABLE Saque (
    id INT AUTO_INCREMENT PRIMARY KEY,     -- Identificador único da operação de saque
    agencia_id INT,                        -- Referência à tabela Agencias
    cliente_id INT,                        -- Referência à tabela Clientes
    valor DECIMAL(10, 2) NOT NULL,        -- Valor do saque
    FOREIGN KEY (agencia_id) REFERENCES Agencias(id), -- Chave estrangeira
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)  -- Chave estrangeira
);

-- Tabela Deposito
CREATE TABLE Deposito (
    id INT AUTO_INCREMENT PRIMARY KEY,     -- Identificador único da operação de depósito
    agencia_id INT,                        -- Referência à tabela Agencias
    cliente_id INT,                        -- Referência à tabela Clientes
    valor DECIMAL(10, 2) NOT NULL,        -- Valor do depósito
    FOREIGN KEY (agencia_id) REFERENCES Agencias(id), -- Chave estrangeira
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)  -- Chave estrangeira
);

-- Criação da Trigger para Saque
DELIMITER //

CREATE TRIGGER antes_saque
BEFORE INSERT ON Saque
FOR EACH ROW
BEGIN
    DECLARE saldo_atual DECIMAL(10, 2);  -- Variável para armazenar o saldo atual
    
    -- Obtém o saldo atual do cliente
    SELECT saldo INTO saldo_atual FROM Clientes WHERE id = NEW.cliente_id;
    
    -- Verifica se o saldo é suficiente para o saque
    IF saldo_atual < NEW.valor THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Saldo insuficiente para saque';  -- Mensagem de erro
    ELSE
        -- Atualiza o saldo do cliente subtraindo o valor do saque
        UPDATE Clientes SET saldo = saldo - NEW.valor WHERE id = NEW.cliente_id;
    END IF;
END; //

-- Criação da Trigger para Depósito
CREATE TRIGGER antes_deposito
BEFORE INSERT ON Deposito
FOR EACH ROW
BEGIN
    -- Atualiza o saldo do cliente adicionando o valor do depósito
    UPDATE Clientes SET saldo = saldo + NEW.valor WHERE id = NEW.cliente_id;
END; //

DELIMITER ;
