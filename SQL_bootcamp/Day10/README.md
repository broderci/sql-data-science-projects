# Day 10 — SQL: Traveling Salesman Problem (TSP)

**Topics:** Graph theory, recursive queries, combinatorial optimization, path finding algorithms  
**Challenge:** Implement TSP solution using SQL recursive queries

---

## Exercises

### Exercise 00 — `day10_ex01.sql.sql`
**Task:** Solve Classical Traveling Salesman Problem for 4 cities.  
**Problem:** Find cheapest Hamiltonian cycle starting and ending at city 'a'.

**Graph Structure:**
- Cities: a, b, c, d
- Symmetric costs between cities
- Need to visit all cities exactly once and return to start

**Steps:**
1. Create table `travel_costs` with columns: point1, point2, cost
2. Insert all symmetric paths based on provided graph
3. Write recursive SQL query to find all possible tours
4. Calculate total cost for each tour
5. Return tours with minimum total cost

**Output format:**
- total_cost
- tour (array path like {a,b,c,d,a})

**Sort:** By total_cost, then by tour

### Exercise 01 — `day10_ex01.sql`
**Task:** Extend solution to show both cheapest AND most expensive tours.  
**Extension:** Modify previous query to include maximum cost tours

**Output format:** Same as Exercise 00 but including both min and max cost routes

**Sort:** By total_cost, then by tour

---

## Graph Data (based on image)
Create table with following symmetric paths:

| point1 | point2 | cost |
|--------|--------|------|
| a      | b      | 10   |
| a      | c      | 15   |
| a      | d      | 20   |
| b      | c      | 35   |
| b      | d      | 25   |
| c      | d      | 30   |

**Note:** Add reverse paths since graph is undirected:
- b-a = 10, c-a = 15, d-a = 20, etc.

---

## Skills Demonstrated
- Recursive SQL queries (WITH RECURSIVE)
- Graph traversal algorithms in SQL
- Hamiltonian cycle finding
- Combinatorial problem solving
- Symmetric path handling
- Cost aggregation and optimization
- Array manipulation for path representation

---

## Notes
- TSP is NP-hard combinatorial optimization problem
- SQL recursive queries can solve small instances
- Solution uses brute-force enumeration of all permutations
- For n cities: (n-1)! possible tours
- Symmetric TSP assumes cost(i,j) = cost(j,i)
- Start and end at same city 'a'