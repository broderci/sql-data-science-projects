SELECT p.name, COUNT(*) AS count
FROM person_visits pv
JOIN person p ON pv.person_id = p.id
GROUP BY p.name
HAVING count(*) > 3;