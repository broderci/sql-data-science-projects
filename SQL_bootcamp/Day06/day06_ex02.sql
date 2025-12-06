SELECT
	p.name, 
	m.pizza_name, 
	m.price, 
	ROUND((price - (price* pd.discount/100)),2) AS discount_price,
	pz.name AS pizzeria_name
FROM person p
	JOIN person_order po ON p.id = po.person_id
	JOIN menu m ON m.id = po.menu_id
	JOIN pizzeria pz ON pz.id = m.pizzeria_id
	JOIN person_discounts pd ON p.id = pd.person_id AND pz.id = pd.pizzeria_id
ORDER BY 1, 2;
	
	