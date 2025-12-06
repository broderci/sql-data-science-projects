WITH cte AS (
  SELECT DISTINCT 
    id,
    name,
    address
  FROM person
)
SELECT 
  c1.name AS first_person,
  c2.name AS second_person,
  c1.address AS shared_address
FROM cte c1
JOIN cte c2 ON c1.address = c2.address
WHERE c1.id > c2.id
ORDER BY 
  c1.name, 
  c2.name, 
  c1.address;
