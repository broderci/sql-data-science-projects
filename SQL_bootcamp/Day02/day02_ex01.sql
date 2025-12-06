SELECT 
    day.visit_date::date AS missing_date
FROM 
    generate_series('2022-01-01'::date, '2022-01-10'::date, '1 day'::interval) AS day(visit_date)
LEFT JOIN 
    person_visits pv 
ON 
    day.visit_date = pv.visit_date AND (pv.person_id = 1 OR pv.person_id = 2)
WHERE 
    pv.visit_date IS NULL
ORDER BY day.visit_date;