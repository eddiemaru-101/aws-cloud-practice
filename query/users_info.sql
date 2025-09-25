-- Create database and use it
CREATE DATABASE IF NOT EXISTS sesac;
USE sesac;

-- Drop table if exists and create new one
DROP TABLE IF EXISTS users_info;

-- Create users_info table
CREATE TABLE users_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(30) NOT NULL UNIQUE,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample user data
INSERT INTO users_info (user_id, username, password) VALUES
('admin001', 'admin', 'admin123!'),
('user001', 'john_doe', 'password456'),
('user002', 'alice_kim', 'mypassword789'),
('user003', 'bob_lee', 'securepass123'),
('user004', 'sarah_park', 'userpass456');

-- Select all users
SELECT * FROM users_info;
