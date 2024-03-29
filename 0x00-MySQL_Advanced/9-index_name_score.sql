-- indices
-- creates an index on the table names
-- first letter of the name
CREATE INDEX idx_name_first ON names(name(1));
