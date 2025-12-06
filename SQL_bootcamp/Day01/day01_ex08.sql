SELECT order_date, name || ' (age:'|| age|| ')' AS person_information
FROM person_order NATURAL JOIN person 
ORDER BY 1 ,2;