-- A script that displays the averrage tempreture

SELECT city, AVG(temperature) AS avg_temperature_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;
