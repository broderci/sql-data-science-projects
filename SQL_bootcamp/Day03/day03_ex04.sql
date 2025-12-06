WITH male_only AS (
	SELECT DISTINCT pizzeria_id
	FROM person_order po 
	JOIN menu m on m.id = po.menu_id
	JOIN person p ON p.id = po.person_id
	WHERE p.gender = 'male'
	EXCEPT ALL
	SELECT DISTINCT pizzeria_id
	FROM person_order po 
	JOIN menu m on m.id = po.menu_id
	JOIN person p ON p.id = po.person_id
	WHERE p.gender = 'female'
),
female_only AS (
	SELECT DISTINCT pizzeria_id
	FROM person_order po 
	JOIN menu m on m.id = po.menu_id
	JOIN person p ON p.id = po.person_id
	WHERE p.gender = 'female'
	EXCEPT ALL
	SELECT DISTINCT pizzeria_id
	FROM person_order po 
	JOIN menu m on m.id = po.menu_id
	JOIN person p ON p.id = po.person_id
	WHERE p.gender = 'male'
)
SELECT pizzeria.name AS pizzeria_name
FROM pizzeria
WHERE pizzeria.id IN (
    SELECT DISTINCT pizzeria_id 
    FROM male_only UNION ALL 
    SELECT DISTINCT pizzeria_id 
    FROM female_only
)
ORDER BY pizzeria_name;