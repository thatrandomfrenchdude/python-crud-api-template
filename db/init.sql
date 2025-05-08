CREATE TABLE IF NOT EXISTS contacts (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

INSERT INTO contacts (id, name, phone_number)
VALUES ('123e4567-e89b-12d3-a456-426614174000', 'John Doe', '123-456-7890'),
       ('123e4567-e89b-12d3-a456-426614174001', 'Jane Doe', '987-654-3210');
