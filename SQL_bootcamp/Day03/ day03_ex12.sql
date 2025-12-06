INSERT INTO person_order (id, person_id, menu_id, order_date)
SELECT 
    (SELECT MAX(id) FROM person_order) + p.id AS new_id,
    p.id, 
    (SELECT id FROM menu WHERE pizza_name = 'greek pizza'),
    '2022-02-25'
FROM 
    person p
WHERE 
    (
        SELECT id 
        FROM menu 
        WHERE pizza_name = 'greek pizza'
    ) IS NOT NULL;