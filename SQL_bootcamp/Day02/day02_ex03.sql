WITH date_range AS (
    SELECT generate_series('2022-01-01'::date, '2022-01-10'::date, '1 day'::interval) AS visit_date
)
SELECT dr.visit_date::date AS missing_date
FROM date_range dr
LEFT JOIN person_visits pv ON dr.visit_date = pv.visit_date 
                          AND (pv.person_id = 1 OR pv.person_id = 2)
WHERE pv.visit_date IS NULL
ORDER BY dr.visit_date;
