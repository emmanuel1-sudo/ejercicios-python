CREATE DATABASE IF NOT EXISTS ejercicios_python;
USE ejercicios_python;
CREATE TABLE IF NOT EXISTS tablas_multiplicar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero INT NOT NULL,
    multiplicador INT NOT NULL,
    resultado INT NOT NULL
)

SELECT * FROM tablas_multiplicar;