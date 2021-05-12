CREATE TABLE students(id serial, name text, address text, age int);

INSERT INTO students(name, address, age) VALUES
    ('luis', 'cucuta', 23);
INSERT INTO students(name, address, age) VALUES
    ('Ernesto', 'lopez', 24);

select * from students;
    