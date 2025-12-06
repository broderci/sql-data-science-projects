WITH balance_aggregated AS (
    SELECT 
        user_id, 
        type,
        currency_id,
        SUM(money) AS value
    FROM 
        balance
    GROUP BY 
        user_id, type, currency_id
)

SELECT 
    COALESCE(u.name, 'not defined') AS name,
    COALESCE(u.lastname, 'not defined') AS lastname,
    b.type,
    ba.value,
    COALESCE(c.name, 'not defined') AS currency_name,
    COALESCE(latest.rate_to_usd, 1) AS last_rate_to_usd,
    ba.value * COALESCE(latest.rate_to_usd, 1) AS total_volume_in_usd
FROM 
    balance AS b
JOIN balance_aggregated ba ON ba.user_id = b.user_id AND ba.type = b.type
FULL JOIN 
    "user" AS u ON b.user_id = u.id
LEFT JOIN LATERAL (
    SELECT rate_to_usd 
    FROM currency AS c1 
    WHERE c1.id = b.currency_id 
    ORDER BY c1.updated DESC 
    LIMIT 1
) AS latest ON TRUE
LEFT JOIN 
    currency AS c ON b.currency_id = c.id
GROUP BY 
    u.name, u.lastname, b.type, ba.value, c.name, latest.rate_to_usd
ORDER BY 
    name DESC, lastname, b.type;
