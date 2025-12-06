 CREATE OR REPLACE FUNCTION fnc_persons(pgender varchar default 'female')
 RETURNS TABLE(id person.id%TYPE,
 name person.name%TYPE,
 age person.age%TYPE,
 gender person.gender%TYPE,
 address person.address%TYPE) AS $$
 SELECT id, name, age, gender, address
 FROM person
 WHERE gender= pgender;
 $$ LANGUAGE SQL;


--SELECT * FROM fnc_persons(pgender := 'male');


--SELECT * FROM fnc_persons();

