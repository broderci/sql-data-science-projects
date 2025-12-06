CREATE OR REPLACE FUNCTION fnc_fibonacci(pstop integer default 10)
 RETURNS TABLE(x BIGINT) AS $$
 WITH RECURSIVE f (x,y) AS
 	(SELECT 0 AS x, 1 AS y
 	UNION ALL
 	SELECT y, x+y FROM f WHERE y<pstop)
 SELECT x
 FROM f;
 $$ LANGUAGE SQL;

 --select * from fnc_fibonacci(100);


 --select * from fnc_fibonacci();