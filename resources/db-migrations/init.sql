DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    age INT NOT NULL,
    address VARCHAR(255),
    joining_date DATE NOT NULL,
    is_registered BOOLEAN NOT NULL
);

INSERT INTO users (first_name, last_name, email, age, address, joining_date, is_registered) VALUES
('Alice', 'Smith', 'alice.smith@example.com', 25, '123 Main St, Springfield, IL', '2021-06-15', TRUE),
('Bob', 'Johnson', 'bob.johnson@example.com', 30, '456 Oak St, Shelbyville, IL', '2020-09-12', FALSE),
('Charlie', 'Brown', 'charlie.brown@example.com', 22, '789 Pine St, Capital City, NY', '2022-01-05', TRUE),
('Diana', 'Prince', 'diana.prince@example.com', 28, '101 Amazon Ln, Themyscira', '2023-04-20', TRUE),
('Eve', 'Davis', 'eve.davis@example.com', 35, '55 Broadway, New York, NY', '2019-11-08', FALSE),
('Frank', 'Miller', 'frank.miller@example.com', 45, '78 Elm St, Smalltown, CA', '2021-02-14', TRUE),
('Grace', 'Hopper', 'grace.hopper@example.com', 29, '999 Tech Blvd, Silicon Valley, CA', '2018-07-21', TRUE),
('Henry', 'Ford', 'henry.ford@example.com', 60, '12 Industrial Ave, Detroit, MI', '2015-03-10', TRUE),
('Ivy', 'Green', 'ivy.green@example.com', 18, '432 Maple Rd, Oakwood, TX', '2023-01-28', FALSE),
('Jack', 'White', 'jack.white@example.com', 34, '222 Sunset Blvd, Los Angeles, CA', '2022-12-02', TRUE);
