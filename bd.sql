CREATE TABLE usuario(
	id int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(50) not null,
    email varchar(50) UNIQUE not null,
    cpf int UNIQUE NOT null,
    senha varchar(50) NOT null
)

CREATE TABLE tabela_desafios (
    id INT NOT NULL AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    desa_agua VARCHAR(250) NOT NULL,
    desa_residuos VARCHAR(250) NOT NULL,
    desa_enrgia VARCHAR(250) NOT NULL,
    desa_transporte VARCHAR(250) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE
);