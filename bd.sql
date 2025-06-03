CREATE TABLE usuario (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(50),
    cpf VARCHAR(50),
    senha VARCHAR(50)
);

CREATE TABLE desafios (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT
);

CREATE TABLE respostas_desafios (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT(11),
    id_desafio INT(11),
    respostas VARCHAR(250),
    pontuacao INT(11),
    data_resposta DATE,
    status VARCHAR(50),
    valor VARCHAR(250),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_desafio) REFERENCES desafios(id)
);

CREATE TABLE resultados_desafios (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT(11),
    resultado_mensal VARCHAR(250),
    data DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
