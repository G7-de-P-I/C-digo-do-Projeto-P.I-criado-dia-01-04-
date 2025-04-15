CREATE TABLE usuario(
	id int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(50) not null,
    email varchar(50) UNIQUE not null,
    cpf int UNIQUE NOT null,
    senha varchar(50) NOT null
)
