# Day 07 — SQL: Data Aggregation and Analytics

**Topics:** Aggregation functions, GROUP BY, HAVING, ranking, data analytics, business metrics  
**Database:** Pizza demo database (see `../misc/images/schema.png`)

## Database Overview
| Table | Description | Key Columns |
|-------|-------------|-------------|
| `person` | Pizza lovers | id, name, age, gender, address |
| `pizzeria` | Pizza restaurants | id, name, rating |
| `menu` | Pizza menu with prices | id, pizzeria_id, pizza_name, price |
| `person_visits` | Visit records | person_id, pizzeria_id, visit_date |
| `person_order` | Order records | person_id, menu_id, order_date |
| `person_discounts` | Personal discounts | person_id, pizzeria_id, discount |

---

## Exercises

### Exercise 00 — `day07_ex00.sql`
**Task:** Count visits per person.  
**Return:** person_id, count_of_visits  
**Sort:** By count_of_visits descending, person_id ascending.

### Exercise 01 — `day07_ex01.sql`
**Task:** Show top 4 people by visit count with their names.  
**Return:** name, count_of_visits  
**Limit:** Top 4 by visit count  
**Sort:** By name.

### Exercise 02 — `day07_ex02.sql`
**Task:** Show top 3 restaurants by visits and top 3 by orders.  
**Return:** restaurant name, count, action_type ('visit' or 'order')  
**Union:** Results from two separate rankings  
**Sort:** By action_type ascending, count descending.

### Exercise 03 — `day07_ex03.sql`
**Task:** Combine visit and order counts per restaurant.  
**Return:** restaurant name, total_count (visits + orders)  
**Note:** Some pizzerias may have only visits or only orders  
**Sort:** By total_count descending, name ascending.

### Exercise 04 — `day07_ex04.sql`
**Task:** Find people with more than 3 visits.  
**Return:** name, count_of_visits  
**Condition:** count_of_visits > 3  
**Restriction:** No WHERE clause (use HAVING instead)  
**Sort:** Not specified.

### Exercise 05 — `day07_ex05.sql`
**Task:** Find unique people who have placed orders.  
**Return:** name  
**Restriction:** No GROUP BY, no set operations (UNION, etc.)  
**Sort:** By name.

### Exercise 06 — `day07_ex06.sql`
**Task:** Calculate restaurant sales metrics.  
**Return:** restaurant name, count_of_orders, average_price, max_price, min_price  
**Round:** average_price to 2 decimal places  
**Sort:** By restaurant name.

### Exercise 07 — `day07_ex07.sql`
**Task:** Calculate global average rating across all restaurants.  
**Return:** global_rating  
**Round:** To 4 decimal places.

### Exercise 08 — `day07_ex08.sql`
**Task:** Combine person addresses with restaurant orders.  
**Assumption:** Person only visits restaurants in their own city  
**Return:** address, restaurant name, count_of_orders  
**Sort:** By address, restaurant name.

### Exercise 09 — `day07_ex09.sql`
**Task:** Calculate address-based age statistics and comparisons.  
**Return:** 
- address
- formula: MAX(age) - (MIN(age) / MAX(age))
- average: AVG(age)
- comparison: formula > average (boolean)  
**Sort:** By address.

---

## Skills Demonstrated
- Data aggregation with COUNT, SUM, AVG, MIN, MAX
- Grouping and filtering with GROUP BY and HAVING
- Ranking and limiting results
- Combining data from multiple sources
- Creating calculated columns with formulas
- Working with UNION operations
- Data rounding and type casting
- Boolean comparisons and conditional logic
- Business metric calculation

---

## Notes
- Database includes all changes from previous days
- Focus on analytical SQL patterns
- Real-world business metrics calculation
- Multiple approaches to data aggregation
- Performance considerations for large datasets