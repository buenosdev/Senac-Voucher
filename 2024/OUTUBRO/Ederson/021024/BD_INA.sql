use e2_database;
-- 19
create table perfil (
    id_cliente_perfil integer primary key,  
    foto_perfil varchar(200) not null default 'default_profile_picture.jpg',  -- endereço da foto de perfil com valor padrão
    banner_perfil varchar(200) not null default 'default_banner_picture.jpg',  -- endereço da foto de banner com valor padrão
    descricao_perfil varchar(500),  
    tiktok_perfil varchar(50),
    linkedin_perfil varchar(50),
    facebook_perfil varchar(50),
    youtube_perfil varchar(50),
    instagram_perfil varchar(50),
    foreign key (id_cliente_perfil) references cliente(id_cliente)  
);
-- 21
create table cidade (
    id_cidade integer auto_increment primary key, 
    nome_cidade varchar(50) not null, 
    id_estado integer not null,  
    foreign key (id_estado) references estado(id_estado)  
);


-- 23
create table anuncio (
    index_anuncio integer unique primary key, 
    endereco_imagem_anuncio varchar(200) not null  
);
