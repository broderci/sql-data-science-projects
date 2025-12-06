CREATE UNIQUE INDEX idx_menu_unique ON menu (pizzeria_id, pizza_name); -- каждая комбинация pizzeria_id и pizza_name будет уникальной

SET enable_seqscan = off;
EXPLAIN ANALYZE
SELECT *
FROM menu
WHERE pizzeria_id = 2 AND pizza_name = 'cheese pizza';
