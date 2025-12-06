 CREATE FUNCTION func_minimum(VARIADIC arr NUMERIC[ ])
 RETURNS NUMERIC AS
 $$
 SELECT min(i) FROM unnest(arr) n(i);
 $$ LANGUAGE SQL;




 SELECT func_minimum(VARIADIC arr => ARRAY[10.0, -1.0, 5.0, 4.4]);
