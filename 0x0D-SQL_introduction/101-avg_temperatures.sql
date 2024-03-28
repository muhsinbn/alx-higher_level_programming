-- A script that displays the averrage tempreture

SELECT city, AVG(temperature) AS avg_temperature_fahrenheit
FROM table_name
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;
