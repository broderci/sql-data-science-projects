# Day 08 — SQL: Transaction Isolation and Concurrency

**Topics:** ACID properties, transaction isolation levels, database anomalies, concurrency control  
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

### Exercise 00 — `day08_ex00.sql`
**Task:** Demonstrate basic transaction behavior with COMMIT.  
**Scenario:** Update Pizza Hut rating in Session #1, check visibility in Session #2.  
**Files to submit:**
- SQL script with comments for both sessions
- Screenshot of psql output for Session #1
- Screenshot of psql output for Session #2

### Exercise 01 — `day08_ex01.sql`
**Task:** Reproduce Lost Update Anomaly under READ COMMITTED isolation.  
**Scenario:** Two sessions concurrently update Pizza Hut rating.  
**Isolation:** READ COMMITTED (default)  
**Files to submit:** Same as Exercise 00.

### Exercise 02 — `day08_ex02.sql`
**Task:** Test Lost Update Anomaly under REPEATABLE READ isolation.  
**Scenario:** Two sessions concurrently update Pizza Hut rating.  
**Isolation:** REPEATABLE READ  
**Files to submit:** Same as Exercise 00.

### Exercise 03 — `day08_ex03.sql`
**Task:** Demonstrate Non-Repeatable Reads Anomaly under READ COMMITTED.  
**Scenario:** Session #1 reads rating, Session #2 updates it, Session #1 reads again.  
**Isolation:** READ COMMITTED  
**Files to submit:** Same as Exercise 00.

### Exercise 04 — `day08_ex04.sql`
**Task:** Test Non-Repeatable Reads under SERIALIZABLE isolation.  
**Scenario:** Session #1 reads rating, Session #2 updates it.  
**Isolation:** SERIALIZABLE  
**Files to submit:** Same as Exercise 00.

### Exercise 05 — `day08_ex05.sql`
**Task:** Demonstrate Phantom Reads Anomaly under READ COMMITTED.  
**Scenario:** Session #1 aggregates ratings, Session #2 inserts new pizzeria.  
**Isolation:** READ COMMITTED  
**Files to submit:** Same as Exercise 00.

### Exercise 06 — `day08_ex06.sql`
**Task:** Test Phantom Reads under REPEATABLE READ isolation.  
**Scenario:** Session #1 aggregates ratings, Session #2 inserts new pizzeria.  
**Isolation:** REPEATABLE READ  
**Files to submit:** Same as Exercise 00.

### Exercise 07 — `day08_ex07.sql`
**Task:** Reproduce deadlock situation between two sessions.  
**Scenario:** Create "Christ-lock" deadlock with two transactions.  
**Isolation:** Any level (default acceptable)  
**Files to submit:** Same as Exercise 00.

---

## Skills Demonstrated
- Understanding ACID properties of transactions
- Working with different isolation levels:
  - READ COMMITTED
  - REPEATABLE READ  
  - SERIALIZABLE
- Reproducing database anomalies:
  - Lost Update
  - Non-Repeatable Reads
  - Phantom Reads
- Handling deadlock situations
- Using psql command line for concurrent sessions
- Transaction management with COMMIT
- Understanding concurrency control mechanisms

---

## Notes
- All exercises require practical execution in psql
- Default PostgreSQL isolation level is READ COMMITTED
- REPEATABLE READ prevents some anomalies but not all
- SERIALIZABLE provides strongest isolation
- Deadlocks are automatically detected and resolved by database
- Screenshots must show actual execution results