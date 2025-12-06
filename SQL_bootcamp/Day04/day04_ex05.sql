CREATE VIEW v_price_with_discount AS
 select p.name, m.pizza_name, m.price, CAST(m.price - m.price*0.1 AS INTEGER) as discount_price
 FROM person p
 JOIN person_order po ON p.id = po.person_id
 JOIN menu m ON m.id = po.menu_id
ORDER BY 1, 2;