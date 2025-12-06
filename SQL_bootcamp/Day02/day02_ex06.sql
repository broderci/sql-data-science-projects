select m.pizza_name, pz.name as pizzeria_name
from person_order po
join person p on p.id = po.person_id and p.name in ('Denis', 'Anna')
join menu m on po.menu_id = m.id
join pizzeria pz on pz.id = m.pizzeria_id
ORDER BY pizza_name, pizzeria_name;;
