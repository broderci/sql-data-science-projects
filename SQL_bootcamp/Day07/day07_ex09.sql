SELECT address,
	ROUND((max(age) - (min(age)/max(age))), 2) as formula,
	ROUND(avg(age),2) as	average,
	round((max(age)- min(age) /max(age::numeric)),2) > round(avg(age), 2) AS comparison
FROM person p

GROUP BY address 
ORDER BY address;