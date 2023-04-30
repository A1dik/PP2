CREATE OR REPLACE FUNCTION checks(w_name VARCHAR, w_surname VARCHAR)
RETURNS INT
AS
$$
BEGIN
RETURN(SELECT count(*) FROM phonebook WHERE phonebook.name = w_name AND phonebook.surname = w_surname);
END;
$$
LANGUAGE plpgsql;