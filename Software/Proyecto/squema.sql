-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS gestion_usuarios;
USE gestion_usuarios;

-- Crear la tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombres_apellidos VARCHAR(255) NOT NULL,
    numero_identificacion VARCHAR(50) UNIQUE NOT NULL,
    tipo_identificacion ENUM('Cédula', 'Tarjeta de Identidad', 'PPT') NOT NULL,
    correo_electronico VARCHAR(255) UNIQUE NOT NULL,
    edad INT NOT NULL,
    genero ENUM('Masculino', 'Femenino') NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear la tabla de historial de modificaciones
CREATE TABLE IF NOT EXISTS historial_modificaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_modificado INT NOT NULL,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    descripcion VARCHAR(255) NOT NULL,
    FOREIGN KEY (usuario_modificado) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Crear el usuario y otorgarle permisos de acceso remoto
CREATE USER IF NOT EXISTS 'politecnico'@'192.168.20.24' IDENTIFIED BY 'politecnico';
GRANT ALL PRIVILEGES ON gestion_usuarios.* TO 'politecnico'@'192.168.20.24';
FLUSH PRIVILEGES;

-- Permitir conexiones remotas en MySQL (esto se hace en la configuración del servidor)
-- Editar /etc/mysql/mysql.conf.d/mysqld.cnf y cambiar:
-- bind-address = 0.0.0.0
