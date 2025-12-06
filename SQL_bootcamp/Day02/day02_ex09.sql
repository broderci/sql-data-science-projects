select p.name
from person_order po
join person p on p.id = po.person_id and gender = 'female'
join menu m on po.menu_id = m.id and pizza_name in ('pepperoni pizza', 'cheese pizza')
group by p.name
having count(m.pizza_name) = 2
ORDER BY p.name DESC;
