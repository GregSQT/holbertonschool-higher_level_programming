-- Creation de DB
SELECT score, COUNT (*) "number" FROM second_table GROUP BY score ORDER BY COUNT(*) DESC;
