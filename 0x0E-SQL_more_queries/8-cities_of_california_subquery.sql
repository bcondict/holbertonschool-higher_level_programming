-- lists all the cities of califionia that can be found in the database
SELECT `id`, `name` FROM cities
WHERE `state_id`=(
    SELECT `id` FROM states WHERE `name`='California'
);