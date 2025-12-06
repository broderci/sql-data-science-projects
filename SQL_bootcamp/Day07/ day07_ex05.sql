SELECT p.name
FROM person_order po
JOIN person p ON po.person_id = p.id
GROUP BY p.name
order by 1;