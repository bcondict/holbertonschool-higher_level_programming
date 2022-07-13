-- LISTS ALL RECORDS WITH SCORE >= 10 INT TABLE
SELECT `score`, `name` FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;