SELECT p.name, p.rating
FROM pizzeria p
LEFT JOIN (
    SELECT DISTINCT pizzeria_id
    FROM person_visits
) pv ON p.id = pv.pizzeria_id
WHERE pv.pizzeria_id IS NULL

ORDER BY p.name;
