-- an sql script that creates a trigger that deceases the quantity of 
-- an item after a new order

DELIMITER $$ ;
CREATE TRIGGER dec_itm AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END
$$
DELIMITER  ; $$
