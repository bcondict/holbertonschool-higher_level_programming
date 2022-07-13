-- lists all records of the table
SELECT `score`, `name` FROM `second_table`
WHERE EXISTS `name`
ORDER BY `score` DESC;