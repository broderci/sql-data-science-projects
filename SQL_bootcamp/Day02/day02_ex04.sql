with menu_pizza AS (select * 
from menu 
where pizza_name = 'mushroom pizza' or pizza_name ='pepperoni pizza'
)

select mp.pizza_name, pz.name, mp.price
from menu_pizza mp join pizzeria pz ON mp.pizzeria_id = pz.id
order by 1,2,3; 
