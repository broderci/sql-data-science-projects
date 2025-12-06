# Day 06 — SQL: Database Design and Business Features

**Topics:** Database modeling, constraints, sequences, business logic implementation, data consistency  
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

### Exercise 00 — `day06_ex00.sql`
**Task:** Create new table for personal discounts feature.  
**Table:** `person_discounts`  
**Columns:**
- `id` - Primary Key (same type as other table IDs)
- `person_id` - Foreign Key to `person(id)`
- `pizzeria_id` - Foreign Key to `pizzeria(id)`
- `discount` - numeric type for percentage values

**Constraints naming:**
- `fk_person_discounts_person_id`
- `fk_person_discounts_pizzeria_id`

### Exercise 01 — `day06_ex01.sql`
**Task:** Populate discounts table based on order history.  
**Logic:** Calculate personal discount per person per pizzeria:
- 1 order → 10.5% discount
- 2 orders → 22% discount
- 3+ orders → 30% discount

**Implementation:** Use INSERT INTO ... SELECT with aggregation and ROW_NUMBER() for ID generation.

### Exercise 02 — `day06_ex02.sql`
**Task:** Show orders with actual price and discounted price.  
**Return:** person name, pizza name, original price, discount price, pizzeria name  
**Sort:** By person name, pizza name.

### Exercise 03 — `day06_ex03.sql`
**Task:** Create unique index to prevent duplicate person-pizzeria pairs.  
**Index name:** `idx_person_discounts_unique`  
**Columns:** `person_id`, `pizzeria_id`  
**Proof:** Provide SQL with EXPLAIN ANALYZE showing index usage.

### Exercise 04 — `day06_ex04.sql`
**Task:** Add constraints to ensure data integrity.  
**Constraints to add:**
1. `person_id` NOT NULL (`ch_nn_person_id`)
2. `pizzeria_id` NOT NULL (`ch_nn_pizzeria_id`)
3. `discount` NOT NULL (`ch_nn_discount`)
4. `discount` DEFAULT 0
5. `discount` between 0 and 100 (`ch_range_discount`)

### Exercise 05 — `day06_ex05.sql`
**Task:** Add comments to table and columns for documentation.  
**To comment:**
- `person_discounts` table (business purpose)
- All columns (purpose and usage)

### Exercise 06 — `day06_ex06.sql`
**Task:** Implement automatic primary key generation.  
**Steps:**
1. Create sequence `seq_person_discounts` starting at 1
2. Set sequence current value to: (number of rows in table) + 1
3. Set default value for `person_discounts.id` column to use sequence

**Restriction:** No hardcoded row counts for sequence adjustment.

---

## Skills Demonstrated
- Database schema design and extension
- Implementing business logic in database layer
- Creating and managing constraints for data integrity
- Working with sequences for automatic ID generation
- Adding documentation through comments
- Designing multi-column unique constraints
- Data validation through check constraints
- Business feature implementation from requirements

---

## Notes
- Database uses incremental changes from previous days
- Focus on practical database design patterns
- All constraints use meaningful names for maintainability
- Sequence management requires careful value setting
- Documentation is important for long-term maintenance
- Business rules implemented directly in database