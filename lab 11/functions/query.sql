CREATE OR REPLACE FUNCTION query(how_many INT, how_far INT)
RETURNS TABLE(id integer, name varchar, surname varchar, number varchar)
AS
$$
BEGIN
RETURN QUERY
SELECT Phonebook.id, Phonebook.name, Phonebook.surname, Phonebook.number 
FROM Phonebook 
ORDER BY Phonebook.id
LIMIT how_many
OFFSET how_far;
END;
$$
LANGUAGE plpgsql;