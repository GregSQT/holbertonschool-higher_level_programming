-- Creation de DB
SELECT score, COUNT (*) AS "number" FROM second_table GROUP BY score ORDER BY COUNT(*) DESC;
