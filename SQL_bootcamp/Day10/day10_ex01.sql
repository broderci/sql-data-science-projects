DROP TABLE IF EXISTS destination;

CREATE TABLE destination (
    id SERIAL PRIMARY KEY,
    point1 VARCHAR(10) NOT NULL, -- гарантирует, что всегда будет задано значение
    point2 VARCHAR(10) NOT NULL,
    cost INTEGER NOT NULL
);

INSERT INTO destination (point1, point2, cost)
VALUES
    ('a', 'b', 10),
    ('b', 'a', 10),
    ('a', 'c', 15),
    ('c', 'a', 15),
    ('a', 'd', 20),
    ('d', 'a', 20),
    ('b', 'c', 35),
    ('c', 'b', 35),
    ('b', 'd', 25),
    ('d', 'b', 25),
    ('c', 'd', 30),
    ('d', 'c', 30);

WITH RECURSIVE tours AS (
    SELECT
        point1 AS start_point,
        point2 AS next_point,
        cost AS total_cost,
        ARRAY[point1, point2]::VARCHAR[] AS tour
    FROM destination
    WHERE point1 = 'a'
    
    UNION ALL
    
    SELECT
        t.start_point,
        d.point2,
        t.total_cost + d.cost,
        t.tour || d.point2
    FROM tours t
    JOIN destination d
        ON t.next_point = d.point1
    WHERE NOT (d.point2 = ANY(t.tour))
),

all_cities AS
(SELECT
    total_cost + d.cost AS total_cost,
    tour || d.point2 AS tour
FROM tours t
JOIN destination d
    ON t.next_point = d.point1
WHERE d.point2 = t.start_point
    AND array_length(tour || d.point2, 1) = 5
)

SELECT total_cost, tour
FROM all_cities
WHERE total_cost = (
	SELECT MIN(total_cost)
	FROM all_cities
    )
UNION
SELECT total_cost, tour
FROM all_cities
WHERE total_cost = (
	SELECT MAX(total_cost)
	FROM all_cities
    )
ORDER BY total_cost, tour;