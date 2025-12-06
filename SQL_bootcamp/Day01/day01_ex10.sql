SELECT person.name as person_name,
	menu.pizza_name AS pizza_name,
	pizzeria.name as pizzeria_name
FROM person_order  inner join person ON person.id = person_order.person_id
 join menu ON menu.id = person_order.menu_id
 join pizzeria ON pizzeria.id = menu.pizzeria_id
ORDER BY 1, 2, 3;


