# Day11 01 — SQL: Data Warehousing Concepts

**Topics:** Data warehousing, ETL processes, temporal data, data consistency, currency conversion  
**Challenge:** Implement data integration and transformation for DWH scenario

---

## Exercises

### Exercise 00 — `day11_ex00.sql`
**Task:** Aggregate balance transactions with currency conversion to USD.

**Scenario:**
- Three independent microservice databases (Green, Red, Blue)
- Data inconsistencies and anomalies present
- Need to integrate data into DWH format
- Handle NULL values and missing references

**Data Sources:**
1. `User` table (Green DB) - users with possible NULL names
2. `Currency` table (Red DB) - temporal currency rates with updates
3. `Balance` table (Blue DB) - transaction history with currency references

**Requirements:**
- Calculate total volume per user per balance type
- Convert to USD using latest currency rate
- Handle NULL values with 'not defined' placeholders
- Include all data despite inconsistencies

**Output columns:**
- `name`: user name (or 'not defined' if NULL)
- `lastname`: user lastname (or 'not defined' if NULL)
- `type`: balance type
- `volume`: sum of money per user/type
- `currency_name`: currency name (or 'not defined' if NULL)
- `last_rate_to_usd`: latest rate (or 1 if NULL)
- `total_volume_in_usd`: volume × last_rate_to_usd

**Sort:** By name DESC, lastname ASC, type ASC

### Exercise 01 — `day11_ex01.sql`
**Task:** Show all balance transactions with nearest currency rate in time.

**Prerequisite:** Execute provided INSERT statements for additional currency rates.

**Requirements:**
- Join users with their balance transactions
- Find nearest currency rate in time for each transaction:
  1. Look for rate before transaction date (t1)
  2. If not found, look for rate after transaction date (t2)
- Calculate USD value using found rate
- Ignore currencies without rate data

**Time matching logic:**
For each transaction at time `balance.updated`:
- Find currency rate with `currency.updated` ≤ `balance.updated` (past)
- If none, find rate with `currency.updated` > `balance.updated` (future)
- Use that rate for conversion

**Output columns:**
- `name`: user name (or 'not defined' if NULL)
- `lastname`: user lastname (or 'not defined' if NULL)
- `currency_name`: currency name
- `currency_in_usd`: money × applicable rate_to_usd

**Sort:** By name DESC, lastname ASC, currency_name ASC

---

## Data Anomalies to Handle
1. **Referential inconsistencies:** Users/currencies may exist without balances, and vice versa
2. **NULL values:** User names and lastnames can be NULL
3. **Temporal data:** Currency rates change over time
4. **Missing rates:** Some currencies may have no rate data

---

## Skills Demonstrated
- Data integration from multiple sources
- Handling temporal data with versioning
- Dealing with data inconsistencies
- Currency conversion with time-based rates
- NULL value handling and default values
- Complex JOIN operations with conditions
- Subquery optimization for nearest-neighbor lookups
- Data aggregation and transformation

---

## Notes
- Exercise simulates real-world DWH challenges
- Temporal model requires careful time-based joins
- Nearest-neighbor search is common in financial systems
- Data quality issues must be handled gracefully
- Performance considerations for large datasets