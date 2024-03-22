-- script that creates a trigger that decreases the quantity of an item after a new order
-- Quantity in the table `items` can be negative

CREATE TRIGGER decrease_quantity AFTER INSERT ON items
FOR EACH ROW SET @items = @items - New.item