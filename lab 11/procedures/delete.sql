CREATE OR REPLACE PROCEDURE delete(w_name VARCHAR, w_surname VARCHAR)
AS
$$
BEGIN
DELETE FROM phonebook WHERE phonebook.name = w_name AND phonebook.surname = w_surname;
END;
$$
LANGUAGE plpgsql;