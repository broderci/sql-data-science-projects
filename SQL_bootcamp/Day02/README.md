# Day 02 — SQL: Advanced JOIN Operations

**Topics:** LEFT/RIGHT/FULL JOIN, CTE, date generation, complex filtering, self-joins  
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

### Exercise 00 — `day02_ex00.sql`
**Task:** Find pizzerias that have never been visited by people.  
**Return:** pizzeria name and rating  
**Restriction:** No `NOT IN`, `IN`, `NOT EXISTS`, `EXISTS`, `UNION`, `EXCEPT`, `INTERSECT`.

### Exercise 01 — `day02_ex01.sql`
**Task:** Find missing days from Jan 1-10, 2022 where people with IDs 1 or 2 did NOT visit any pizzeria.  
**Return:** missing_date  
**Allowed:** `generate_series()` for date generation  
**Restriction:** Same as Exercise 00  
**Sort:** By missing_date ascending.

### Exercise 02 — `day02_ex02.sql`
**Task:** Create full combination of all people and all pizzerias for Jan 1-3, 2022, showing visits where they occurred.  
**Return:** person_name, visit_date, pizzeria_name (with '-' for NULL names)  
**Restriction:** Same as Exercise 00  
**Sort:** By person_name, visit_date, pizzeria_name.

### Exercise 03 — `day02_ex03.sql`
**Task:** Rewrite Exercise 01 using CTE (Common Table Expression) for date generation.  
**Return:** missing_date  
**Allowed:** `generate_series()` in CTE  
**Restriction:** Same as Exercise 00.

### Exercise 04 — `day02_ex04.sql`
**Task:** Find all pizzerias and prices for mushroom OR pepperoni pizza.  
**Return:** pizza_name, pizzeria_name, price  
**Sort:** By pizza_name, pizzeria_name.

### Exercise 05 — `day02_ex05.sql`
**Task:** Find names of all females over age 25.  
**Return:** name  
**Sort:** By name.

### Exercise 06 — `day02_ex06.sql`
**Task:** Find all pizzas (and corresponding pizzerias) ordered by Denis OR Anna.  
**Return:** pizza_name, pizzeria_name  
**Sort:** By both columns.

### Exercise 07 — `day02_ex07.sql`
**Task:** Find pizzeria that Dmitriy visited on Jan 8, 2022 where he could eat pizza for < 800 rubles.  
**Return:** pizzeria name.

### Exercise 08 — `day02_ex08.sql`
**Task:** Find men from Moscow or Samara who ordered pepperoni OR mushroom pizza.  
**Return:** person name  
**Sort:** By name descending.

### Exercise 09 — `day02_ex09.sql`
**Task:** Find women who ordered BOTH pepperoni AND cheese pizzas (at any time).  
**Return:** person name  
**Sort:** By name.

### Exercise 10 — `day02_ex10.sql`
**Task:** Find people who live at the same address.  
**Return:** person_name1, person_name2, common_address  
**Sort:** By person_name1, person_name2, common_address.

---

## Skills Demonstrated
- Advanced JOIN operations (LEFT, RIGHT, FULL)
- Working with CTEs (Common Table Expressions)
- Date generation and range analysis
- Complex filtering with multiple conditions
- Self-joins for finding relationships within same table
- Handling NULL values with COALESCE
- Set operations with complex logic (AND/OR conditions)

---

## Notes
- Database created by `../materials/model.sql`
- All exercises use ANSI SQL
- Solutions adhere to specified restrictions
- Focus on practical data analysis scenarios