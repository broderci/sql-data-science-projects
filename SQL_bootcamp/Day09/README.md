# Day 09 — SQL: Functions, Procedures and Triggers

**Topics:** Database triggers, audit patterns, SQL functions, PL/pgSQL, parameterized functions  
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

### Exercise 00 — `day09_ex00.sql`
**Task:** Create audit system for INSERT operations on person table.  
**Steps:**
1. Create `person_audit` table with audit columns
2. Create trigger function `fnc_trg_person_insert_audit`
3. Create trigger `trg_person_insert_audit` (AFTER INSERT, FOR EACH ROW)
4. Test with INSERT statement

### Exercise 01 — `day09_ex01.sql`
**Task:** Extend audit system for UPDATE operations.  
**Steps:**
1. Create trigger function `fnc_trg_person_update_audit`
2. Create trigger `trg_person_update_audit` (AFTER UPDATE, FOR EACH ROW)
3. Test with UPDATE statements

### Exercise 02 — `day09_ex02.sql`
**Task:** Extend audit system for DELETE operations.  
**Steps:**
1. Create trigger function `fnc_trg_person_delete_audit`
2. Create trigger `trg_person_delete_audit` (AFTER DELETE, FOR EACH ROW)
3. Test with DELETE statement

### Exercise 03 — `day09_ex03.sql`
**Task:** Consolidate all audit triggers into one generic trigger.  
**Steps:**
1. Create single trigger function `fnc_trg_person_audit` handling I/U/D
2. Create single trigger `trg_person_audit`
3. Remove old triggers and functions
4. Clear `person_audit` table
5. Test with full DML sequence

### Exercise 04 — `day09_ex04.sql`
**Task:** Create SQL functions to replace gender-based views.  
**Functions to create:**
- `fnc_persons_female()` - returns female persons
- `fnc_persons_male()` - returns male persons  
**Type:** Pure SQL functions (not PL/pgSQL)

### Exercise 05 — `day09_ex05.sql`
**Task:** Create parameterized SQL function for gender filtering.  
**Function:** `fnc_persons(pgender varchar DEFAULT 'female')`  
**Steps:**
1. Remove previous functions from Exercise 04
2. Create single parameterized function
3. Test with and without parameters

### Exercise 06 — `day09_ex06.sql`
**Task:** Create PL/pgSQL function for complex query logic.  
**Function:** `fnc_person_visits_and_eats_on_date()`  
**Parameters:**
- `pperson` (default 'Dmitriy')
- `pprice` (default 500)
- `pdate` (default '2022-01-08')  
**Logic:** Find pizzerias visited by person with pizza < price on date

### Exercise 07 — `day09_ex07.sql`
**Task:** Create function to find minimum value in array.  
**Function:** `func_minimum(VARIADIC arr numeric[])`  
**Type:** SQL or PL/pgSQL  
**Returns:** Minimum value from input array

### Exercise 08 — `day09_ex08.sql`
**Task:** Create function to generate Fibonacci sequence.  
**Function:** `fnc_fibonacci(pstop integer DEFAULT 10)`  
**Returns:** Table of Fibonacci numbers less than pstop  
**Type:** SQL or PL/pgSQL

---

## Skills Demonstrated
- Database trigger creation and management
- Audit pattern implementation for data changes
- SQL function development with parameters
- PL/pgSQL programming for complex logic
- Function overloading and consolidation
- Array parameter handling
- Mathematical sequence generation
- Data validation through triggers
- Event-driven database programming

---

## Notes
- Database includes all changes from previous days
- Exercises progress from simple to complex patterns
- Mix of pure SQL and PL/pgSQL approaches
- Real-world audit system implementation
- Function parameterization for reusability
- Mathematical algorithms in database layer