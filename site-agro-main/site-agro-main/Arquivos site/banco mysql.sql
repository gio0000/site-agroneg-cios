-- Criando o banco de dados
CREATE DATABASE agro;

-- Usando o banco de dados
USE agro;

-- Criando a tabela usuario
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único do usuário
    usuario VARCHAR(50) NOT NULL,     -- Nome do usuário
    senha VARCHAR(255) NOT NULL       -- Senha do usuário (criptografada é recomendável)
);
