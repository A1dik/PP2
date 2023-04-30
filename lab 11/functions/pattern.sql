CREATE OR REPLACE FUNCTION pattern(w_name VARCHAR, w_surname VARCHAR, w_number VARCHAR)
RETURNS TABLE (id integer, name varchar, surname varchar, number varchar)
AS
$$
BEGIN
RETURN QUERY
SELECT Phonebook.id, Phonebook.name, Phonebook.surname, Phonebook.number 
FROM Phonebook 
WHERE Phonebook.name ILIKE w_name 
AND Phonebook.surname ILIKE w_surname 
AND Phonebook.number ILIKE w_number;
END;
$$
LANGUAGE plpgsql;