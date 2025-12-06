SELECT visits.name,
	coalesce(visits.count,0) + coalesce(orders.count,0) as total_count
FROM(
	(SELECT 
        pz.name,
        COUNT(*) AS count
    FROM person_visits pv
    JOIN pizzeria pz ON pv.pizzeria_id = pz.id
    GROUP BY pz.name) as visits
FULL JOIN
    (SELECT 
        pz.name,
        COUNT(*) AS count
    FROM person_order po
    JOIN menu m ON po.menu_id = m.id
    JOIN pizzeria pz ON m.pizzeria_id = pz.id
    GROUP BY pz.name
) as orders ON visits.name = orders.name)

ORDER BY 
    total_count DESC,
    name ASC;