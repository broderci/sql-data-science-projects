# Day 03 — SQL: Data Modification and Complex Analysis

**Topics:** DML operations (INSERT, UPDATE, DELETE), complex filtering, price analysis, data modification patterns  
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

### Exercise 00 — `day03_ex00.sql`
**Task:** Find pizza details for Kate with prices 800-1000 rubles.  
**Return:** pizza_name, price, pizzeria_name, visit_date  
**Sort:** By pizza_name, price, pizzeria_name.

### Exercise 01 — `day03_ex01.sql`
**Task:** Find menu IDs that have never been ordered.  
**Return:** menu_id  
**Restriction:** No `JOIN` operations  
**Sort:** By menu_id.

### Exercise 02 — `day03_ex02.sql`
**Task:** Find pizzas (with prices and pizzeria names) that have never been ordered.  
**Return:** pizza_name, price, pizzeria_name  
**Sort:** By pizza_name, price.

### Exercise 03 — `day03_ex03.sql`
**Task:** Find pizzerias visited more often by women OR more often by men.  
**Return:** pizzeria_name  
**Note:** Use set operations with ALL (keep duplicates)  
**Sort:** By pizzeria_name.

### Exercise 04 — `day03_ex04.sql`
**Task:** Find pizzerias ordered ONLY by women UNION pizzerias ordered ONLY by men.  
**Return:** pizzeria_name  
**Note:** Use set operations without duplicates  
**Sort:** By pizzeria_name.

### Exercise 05 — `day03_ex05.sql`
**Task:** Find pizzerias that Andrey visited but never ordered from.  
**Return:** pizzeria_name  
**Sort:** By pizzeria_name.

### Exercise 06 — `day03_ex06.sql`
**Task:** Find same pizza names with same price in different pizzerias.  
**Return:** pizza_name, pizzeria_name_1, pizzeria_name_2, price  
**Sort:** By pizza_name.

### Exercise 07 — `day03_ex07.sql`
**Task:** INSERT new pizza "greek pizza" (id=19) priced 800 rubles in "Dominos" (pizzeria_id=2).  
**Note:** Modifies data - can restore from `../materials/model.sql`.

### Exercise 08 — `day03_ex08.sql`
**Task:** INSERT new pizza "sicilian pizza" with auto-calculated ID (max+1) priced 900 rubles in "Dominos".  
**Restriction:** No hardcoded IDs for primary key or pizzeria  
**Note:** Modifies data.

### Exercise 09 — `day03_ex09.sql`
**Task:** INSERT new visits to Dominos by Denis and Irina on Feb 24, 2022.  
**Restriction:** No hardcoded IDs  
**Note:** Modifies data.

### Exercise 10 — `day03_ex10.sql`
**Task:** INSERT new orders from Denis and Irina on Feb 24, 2022 for "sicilian pizza".  
**Restriction:** No hardcoded IDs  
**Note:** Modifies data.

### Exercise 11 — `day03_ex11.sql`
**Task:** UPDATE price of "greek pizza" to -10% of current value.  
**Note:** Modifies data.

### Exercise 12 — `day03_ex12.sql`
**Task:** INSERT orders for ALL persons for "greek pizza" on Feb 25, 2022.  
**Allowed:** `generate_series()`, INSERT-SELECT pattern  
**Restriction:** No hardcoded IDs, no window functions, no atomic INSERT statements  
**Note:** Modifies data.

### Exercise 13 — `day03_ex13.sql`
**Task:** Two DML statements:  
1. DELETE all orders from Exercise 12 (by date)  
2. DELETE "greek pizza" from menu  
**Note:** Modifies data.

---

## Skills Demonstrated
- DML operations: INSERT, UPDATE, DELETE
- Complex data analysis with multiple conditions
- Working with un-ordered menu items
- Gender-based analysis of visits and orders
- Price comparison across different pizzerias
- Dynamic data insertion with calculated IDs
- Bulk data operations using INSERT-SELECT pattern
- Data cleanup and maintenance operations

---

## Notes
- Database created by `../materials/model.sql`
- All exercises use ANSI SQL
- Exercises 07-13 modify database data
- Original data can be restored from model script
- Focus on practical data manipulation scenarios