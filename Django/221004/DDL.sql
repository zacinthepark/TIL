-- Create a table
CREATE TABLE contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- 1. Rename a table
ALTER TABLE contacts
RENAME TO new_contacts;

-- 2. Rename a column
ALTER TABLE new_contacts
RENAME COLUMN name TO last_name;

-- 3. Add a new column to a table
ALTER TABLE new_contacts
ADD COLUMN address TEXT NOT NULL;

-- 4. Delete a column
ALTER TABLE new_contacts
DROP COLUMN address;

-- Delete a table
DROP TABLE new_contacts;