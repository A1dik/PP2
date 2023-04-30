CREATE OR REPLACE PROCEDURE update(w_name VARCHAR, w_surname VARCHAR, w_number VARCHAR)
AS
$$
BEGIN
UPDATE phonebook set number = w_number WHERE phonebook.name = w_name AND phonebook.surname = w_surname;
END;
$$
LANGUAGE plpgsql;