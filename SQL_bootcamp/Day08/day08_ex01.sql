-- Session #1
SHOW TRANSACTION ISOLATION LEVEL;

-- Session #2
SHOW TRANSACTION ISOLATION LEVEL;

-- Session #1
BEGIN;
SELECT * FROM pizzeria WHERE name = 'Pizza Hut';

-- Session #2
BEGIN;
SELECT * FROM pizzeria WHERE name = 'Pizza Hut';

-- Session #1
UPDATE pizzeria SET rating = 4 WHERE name = 'Pizza Hut';
-- Session #2
UPDATE pizzeria SET rating = 3.5 WHERE name = 'Pizza Hut';

-- Session #1
commit;
-- Session #2
commit;

-- Session #1
SELECT * 
FROM pizzeria 
WHERE name = 'Pizza Hut';

-- Session #2
SELECT * 
FROM pizzeria 
WHERE name = 'Pizza Hut';

