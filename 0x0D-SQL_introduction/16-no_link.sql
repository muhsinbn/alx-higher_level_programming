-- A script that lists all records of the second_table

SELECT score, name
FROM hbtn_0c_0.second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
