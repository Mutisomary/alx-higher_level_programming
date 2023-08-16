-- displays the average temperature (Fahrenheit) by city
-- ordered by temperature (descending)
SELECT city, AVG(Value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
