SELECT id, name FROM states WHERE state_id = (
    SELECT id,
    SELECT states
    WHERE name = 'California'
)
ORDER BY id ASC;
