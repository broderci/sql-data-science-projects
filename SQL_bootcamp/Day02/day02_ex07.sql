select pz.name as pizzeria_name
from person_visits pv
join person p on p.id = pv.person_id and p.name  = 'Dmitriy'
join pizzeria pz on pz.id = pv.pizzeria_id
join menu m on pz.id = m.pizzeria_id and m.price < 800
where visit_date = '2022-01-08'
ORDER BY pizzeria_name;
