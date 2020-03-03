-- List the number of records with the same score
SELECT score, CONT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
