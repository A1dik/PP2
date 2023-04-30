CREATE OR REPLACE PROCEDURE insert(w_name VARCHAR, w_surname VARCHAR, w_number VARCHAR)
AS
$$
BEGIN
INSERT INTO phonebook(name, surname, number) VALUES(w_name, w_surname, w_number);
END;
$$
LANGUAGE plpgsql;