# Day 04 — SQL: Views and Materialized Views

**Topics:** Database Views, Materialized Views, date generation, symmetric difference, data abstraction  
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

### Exercise 00 — `day04_ex00.sql`
**Task:** Create two database views for filtering persons by gender.  
**Views to create:** 
- `v_persons_female` (for female persons)
- `v_persons_male` (for male persons)  
**Note:** Views should have same attributes as original `person` table.

### Exercise 01 — `day04_ex01.sql`
**Task:** Use the two views from Exercise 00 to get combined list of all person names.  
**Return:** name  
**Sort:** By name.

### Exercise 02 — `day04_ex02.sql`
**Task:** Create view that "stores" generated dates for January 2022.  
**View to create:** `v_generated_dates`  
**Allowed:** `generate_series()` for date generation  
**Date range:** January 1 to January 31, 2022  
**Sort:** By generated_date.

### Exercise 03 — `day04_ex03.sql`
**Task:** Find dates in January 2022 when NO visits occurred.  
**Return:** missing_date  
**Use:** `v_generated_dates` view  
**Sort:** By missing_date.

### Exercise 04 — `day04_ex04.sql`
**Task:** Calculate symmetric difference (R - S) ∪ (S - R) and create view.  
**View to create:** `v_symmetric_union`  
**R:** person_visits on January 2, 2022  
**S:** person_visits on January 6, 2022  
**Return:** person_id only  
**Sort:** By person_id.

### Exercise 05 — `day04_ex05.sql`
**Task:** Create view showing orders with 10% discount calculation.  
**View to create:** `v_price_with_discount`  
**Return:** person name, pizza name, price, discount_price (integer, 10% off)  
**Sort:** By person name, pizza name.

### Exercise 06 — `day04_ex06.sql`
**Task:** Create materialized view based on Day 02 Exercise 07 query.  
**Materialized View:** `mv_dmitriy_visits_and_eats` (with data included)  
**Logic:** Pizzerias where Dmitriy visited on Jan 8, 2022 with pizza < 800 rubles.

### Exercise 07 — `day04_ex07.sql`
**Task:** Refresh materialized view after adding new Dmitriy visit.  
**Steps:**
1. Add new Dmitriy visit to different pizzeria meeting price criteria
2. Refresh `mv_dmitriy_visits_and_eats`  
**Restriction:** No hardcoded IDs for primary key, person, or pizzeria.

### Exercise 08 — `day04_ex08.sql`
**Task:** Clean up database by dropping all created views and materialized views.  
**To drop:** All views and materialized views created in previous exercises.

---

## Skills Demonstrated
- Creating and using Database Views for data abstraction
- Working with Materialized Views for performance optimization
- Date generation and range analysis with views
- Implementing set operations (symmetric difference)
- Calculating derived columns with formulas
- View refresh operations for data consistency
- Database object management (create/drop)

---

## Notes
- Database uses incremental changes from Day 03 exercises
- All exercises use ANSI SQL
- Focus on data abstraction and performance patterns
- Views provide logical data separation
- Materialized Views offer query performance benefits