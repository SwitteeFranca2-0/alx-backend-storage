--  creates a trigger that resets the attribut valid-email
-- wgen the email has been changed

DELIMITER $$ ;
CREATE TRIGGER validate BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
IF OLD.email != NEW.email THEN
    SET NEW.valid_email = 0;
END IF;
END$$ 

DELIMITER ; $$
