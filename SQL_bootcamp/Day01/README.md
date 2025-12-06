# Day 01 — SQL: Set Operations and JOINs

**Topics:** UNION, INTERSECT, EXCEPT, various JOIN types, Cartesian product, IN vs EXISTS  
**Database:** Pizza demo database (see `../misc/images/schema.png`)

## Database Overview
| Table | Description | Key Columns |
|-------|-------------|-------------|
| `person` | Pizza lovers | id, name, age, address |
| `pizzeria` | Pizza restaurants | id, name, rating |
| `menu` | Pizza menu with prices | id, pizzeria_id, pizza_name, price |
| `person_visits` | Visit records | person_id, pizzeria_id, visit_date |
| `person_order` | Order records | person_id, menu_id, order_date |

---

## Exercises

### Exercise 00 — `day01_ex00.sql`
**Task:** Combine pizza names from `menu` with person names from `person` into a single list.  
**Columns:** object_id, object_name  
**Sort:** By object_id, then object_name.

### Exercise 01 — `day01_ex01.sql`
**Task:** Modify previous query: remove object_id column, sort person names first, then pizza names.  
**Columns:** object_name only  
**Note:** Keep duplicate rows.

### Exercise 02 — `day01_ex02.sql`
**Task:** Get unique pizza names in descending order.  
**Restriction:** No `DISTINCT`, `GROUP BY`, `HAVING`, or `JOIN`.

### Exercise 03 — `day01_ex03.sql`
**Task:** Find days when people both visited a pizzeria AND placed an order (same date).  
**Columns:** action_date, person_id  
**Restriction:** No `JOIN`.  
**Sort:** By action_date ascending, person_id descending.

### Exercise 04 — `day01_ex04.sql`
**Task:** Find difference between person_id values from orders and visits on Jan 7, 2022.  
**Return:** person_id with duplicates preserved.  
**Restriction:** No `JOIN`.

### Exercise 05 — `day01_ex05.sql`
**Task:** Generate all possible combinations of `person` and `pizzeria` records (Cartesian product).  
**Sort:** By person.id, then pizzeria.id.

### Exercise 06 — `day01_ex06.sql`
**Task:** Find days when people both visited and ordered, returning person names instead of IDs.  
**Columns:** action_date, person_name  
**Sort:** By action_date ascending, person_name descending.

### Exercise 07 — `day01_ex07.sql`
**Task:** Return order dates with formatted person info "Name (age:X)".  
**Columns:** order_date, person_information  
**Sort:** By both columns ascending.

### Exercise 08 — `day01_ex08.sql`
**Task:** Rewrite Exercise 07 using NATURAL JOIN.  
**Restriction:** Use only NATURAL JOIN.  
**Note:** Result must match Exercise 07.

### Exercise 09 — `day01_ex09.sql`
**Task:** Find pizzerias that have never been visited, using two approaches:
1. Using `IN` operator
2. Using `EXISTS` operator

### Exercise 10 — `day01_ex10.sql`
**Task:** Return list of people, pizzas they ordered, and pizzerias where ordered.  
**Columns:** person_name, pizza_name, pizzeria_name  
**Sort:** By person_name, pizza_name, pizzeria_name ascending.

---

## Skills Demonstrated
- Combining datasets with set operations (UNION, INTERSECT, EXCEPT)
- Joining tables with different JOIN types
- Working with duplicates and unique values
- Comparing IN vs EXISTS approaches
- Cartesian product implementation
- Complex multi-column sorting
- Data formatting and concatenation

---

## Notes
- Database created by `../materials/model.sql`
- All exercises use ANSI SQL
- Solutions adhere to specified restrictions
- Results ordered as required by each task