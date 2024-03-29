-- A script that displays the top 3 cities tempreture during July and Aug

SELECT city, AVG(temperature) AS avg_temperature
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temperature DESC
LIMIT 3;
