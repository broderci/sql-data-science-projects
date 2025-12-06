SELECT 
    pz.name,
    COUNT(*) AS count,
	'visit' AS action_type
FROM person_visits pv
	JOIN pizzeria pz ON pz.id = pv.pizzeria_id 
GROUP BY 
    pz.name

UNION

SELECT 
    pz.name,
    COUNT(*) AS count,
	'order' AS action_type
FROM person_order po
	JOIN menu m ON po.menu_id = m.id
	JOIN pizzeria pz ON m.pizzeria_id = pz.id
group by pz.name

order by action_type, count DESC
;
