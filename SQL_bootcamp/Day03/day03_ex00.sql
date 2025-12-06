SELECT m.pizza_name, m.price, pz.name AS pizzeria_name, pv.visit_date
FROM menu m
	JOIN pizzeria pz ON pz.id = m.pizzeria_id
	JOIN person_visits pv ON pz.id = pv.pizzeria_id
	JOIN person p on p.id = pv.person_id
WHERE p.name = 'Kate' AND m.price BETWEEN 800 AND 1000
ORDER BY pizza_name, price, pizzeria_name;