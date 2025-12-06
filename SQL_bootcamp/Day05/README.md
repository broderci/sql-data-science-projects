# Day 05 — SQL: Database Indexing and Performance Optimization

**Topics:** B-Tree indexes, functional indexes, multi-column indexes, unique constraints, index analysis  
**Database:** Pizza demo database (see `../misc/images/schema.png`)

## Database Overview
| Table | Description | Key Columns |
|-------|-------------|-------------|
| `person` | Pizza lovers | id, name, age, gender, address |
| `pizzeria` | Pizza restaurants | id, name, rating |
| `menu` | Pizza menu with prices | id, pizzeria_id, pizza_name, price |
| `person_visits` | Visit records | person_id, pizzeria_id, visit_date |
| `person_order` | Order records | person_id, menu_id, order_date |

---

## Exercises

### Exercise 00 — `day05_ex00.sql`
**Task:** Create B-Tree indexes for all foreign key columns in the database.  
**Naming pattern:** `idx_{table_name}_{column_name}`  
**Examples:** 
- `idx_menu_pizzeria_id` on `menu(pizzeria_id)`
- `idx_person_visits_person_id` on `person_visits(person_id)`
- `idx_person_visits_pizzeria_id` on `person_visits(pizzeria_id)`
- `idx_person_order_person_id` on `person_order(person_id)`
- `idx_person_order_menu_id` on `person_order(menu_id)`

### Exercise 01 — `day05_ex01.sql`
**Task:** Write query joining pizzas with pizzeria names and prove indexes work.  
**Query:** Return pizza_name and pizzeria_name  
**Proof:** Use `EXPLAIN ANALYZE` to show index usage  
**Hint:** Consider why indexes might not work directly and how to enable them.

### Exercise 02 — `day05_ex02.sql`
**Task:** Create functional B-Tree index on person names in uppercase.  
**Index name:** `idx_person_name`  
**Index on:** `person` table, `name` column transformed to uppercase  
**Proof:** Provide SQL query with `EXPLAIN ANALYZE` showing index usage.

### Exercise 03 — `day05_ex03.sql`
**Task:** Create multi-column B-Tree index for specific query pattern.  
**Index name:** `idx_person_order_multi`  
**Columns:** `person_id`, `menu_id`, `order_date` (in optimal order)  
**Target query:** 
```sql
SELECT person_id, menu_id, order_date 
FROM person_order 
WHERE person_id = 8 AND menu_id = 19;