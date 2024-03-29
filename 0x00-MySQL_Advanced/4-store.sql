-- script that creates a trigger that decreases the quantity of an item after a new order
-- Quantity in the table `items` can be negative

DROP TRIGGER IF EXISTS reduce_quantity_order
DELIMITER //
CREATE TRIGGER reduce_quantity_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN 
	UPDATE items
		SET quantity = quantity - NEW.quantity_ordered
		WHERE name = NEW.item_name;
END;
//

DELIMITER ;
