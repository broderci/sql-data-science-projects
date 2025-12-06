WITH nearest_rate AS (
    SELECT 
        b.user_id,
        b.money,
        b.type,
        b.currency_id,
        b.updated AS balance_updated,
        COALESCE(
            (SELECT rate_to_usd
             FROM currency c1
             WHERE c1.id = b.currency_id AND c1.updated <= b.updated
             ORDER BY c1.updated DESC
             LIMIT 1),
            (SELECT rate_to_usd
             FROM currency c2
             WHERE c2.id = b.currency_id AND c2.updated > b.updated
             ORDER BY c2.updated ASC
             LIMIT 1)
        ) AS rate_to_usd
    FROM balance b
    WHERE EXISTS (
        SELECT 1 
		FROM currency c 
		WHERE c.id = b.currency_id
    )
)

SELECT 
    COALESCE(u.name, 'not defined') AS name,
    COALESCE(u.lastname, 'not defined') AS lastname,
    currency_dist.name AS currency_name,
    nr.money * nr.rate_to_usd AS currency_in_usd
FROM nearest_rate nr
LEFT JOIN "user" u ON nr.user_id = u.id
JOIN 
    (
    SELECT DISTINCT id, name
    FROM currency
    ) AS currency_dist ON nr.currency_id = currency_dist.id
ORDER BY name DESC, lastname ASC, currency_name ASC;