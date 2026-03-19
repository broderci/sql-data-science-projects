# Day 00 — Basic SQL Practice

**Topics:** SELECT, WHERE, ORDER BY, BETWEEN, subqueries, string formatting  
**Database:** Pizza demo database (see `../Materials/er_diagram.png`)

## Database Overview
| Table | Description |
|-------|-------------|
| `person` | People who love pizza |
| `pizzeria` | Available pizzerias |
| `menu` | Pizzas and prices for each pizzeria |
| `person_visits` | Visits of pizzerias |
| `person_order` | Orders made by people |

---

## Exercises

### Exercise 00 — `day00_ex00.sql`
Select names and ages of all people living in Kazan.

### Exercise 01 — `day00_ex01.sql`
Select names and ages of all women from Kazan, ordered by name.

### Exercise 02 — `day00_ex02.sql`
Return names and ratings of pizzerias with rating 3.5-5.0 using:
1. Comparison operators (>=, <=)
2. BETWEEN operator

### Exercise 03 — `day00_ex03.sql`
Find distinct person IDs who visited any pizzeria between Jan 6-9, 2022 OR visited pizzeria id=2.  
Sort by person id descending.

### Exercise 04 — `day00_ex04.sql`
Build formatted string: "Name (age:X,gender:'Y',address:'Z')" for all people.  
Sort by this formatted column.

### Exercise 05 — `day00_ex05.sql`
Return names of people who ordered menu items 13, 14, 18 on Jan 7, 2022.  
Use subquery in SELECT, no IN or JOIN.

### Exercise 06 — `day00_ex06.sql`
Extend previous: add boolean column check_name (true if name='Denis').  
Still no IN or JOIN.

### Exercise 07 — `day00_ex07.sql`
Select person id, name, and interval_info based on age:
- 'interval #1' for age 10-20
- 'interval #2' for age 21-23  
- 'interval #3' for other ages  
Sort by interval_info.

### Exercise 08 — `day00_ex08.sql`
Select all columns from person_order where id is even.  
Order by id.

### Exercise 09 — `day00_ex09.sql`
Using subquery in FROM to filter visits by dates Jan 7-9, 2022, return person and pizzeria names.  
Resolve names via subqueries in SELECT.  
Sort by person name ASC, pizzeria name DESC.

---

## Skills Demonstrated
- Basic SELECT queries with filtering
- Using BETWEEN and comparison operators
- String concatenation and formatting
- Subqueries in SELECT and FROM clauses
- Conditional logic with CASE/boolean columns
- Working with dates and ranges

---

## Notes
- Database created by `../Materials/pizza_demo_db.sql`
- Focus on foundational SQL patterns