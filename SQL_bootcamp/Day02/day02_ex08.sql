select p.name
from person_order po
join person p on p.id = po.person_id and p.address in ('Moscow', 'Samara') and gender = 'male'
join menu m on po.menu_id = m.id and m.pizza_name in ('pepperoni pizza', 'mushroom pizza')
ORDER BY name DESC;
