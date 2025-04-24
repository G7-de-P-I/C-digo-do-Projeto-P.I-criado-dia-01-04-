CREATE TABLE usuario(
	id int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(50) not null,
    email varchar(50) UNIQUE not null,
    cpf int UNIQUE NOT null,
    senha varchar(50) NOT null
)

CREATE TABLE desafios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT
);


CREATE TABLE respostas_desafios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_desafio INT NOT NULL,
    respostas VARCHAR(250),   
    pontuacao INT,          
    data_resposta DATE,    
    status VARCHAR(50),     
    FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE,
    FOREIGN KEY (id_desafio) REFERENCES desafios(id) ON DELETE CASCADE
);