-- displays the top 3 of cities temperature during July and August
-- Ordered by temperature (descending)
SELECT city, temperature
FROM temperatures
WHERE (month = 7 OR month = 8)
ORDER BY temperature DESC
LIMIT 3;
