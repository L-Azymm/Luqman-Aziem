# 📦 Most Used Database Commands

## 🔐 Accessing the Database

```sql
mysql -u root -p           -- Login to MySQL
psql -U postgres           -- Login to PostgreSQL
sqlite3 mydb.db            -- Open SQLite database
```

## Database Management

- Create new database

```sql
CREATE DATABASE dbname;    
```

- List databases

```sql
SHOW DATABASES;            
```

```sql
USE dbname;                -- Switch to database
```

```sql
DROP DATABASE dbname;      -- Delete a database
```

## Table Management

```sql
CREATE TABLE tablename (
  id INT PRIMARY KEY,
  name VARCHAR(50)
);                         -- Create table
```

```sql
SHOW TABLES;               -- List tables
```

```sql
DESCRIBE tablename;        -- Show table structure
```

```sql
DROP TABLE tablename;      -- Delete table
```

## Data Operations

```sql
INSERT INTO tablename (id, name) VALUES (1, 'Alice');  -- Add data
```

```
SELECT * FROM tablename;                               -- Get all data
```

```
UPDATE tablename SET name = 'Bob' WHERE id = 1;        -- Edit data
DELETE FROM tablename WHERE id = 1;                    -- Remove data
```

## Query Helpers

```sql
SELECT * FROM tablename WHERE name LIKE 'A%';   -- Search by pattern
ORDER BY name ASC;                              -- Sort results
LIMIT 10;                                       -- Limit results
```

## User Management (MySQL)

```sql
CREATE USER 'user'@'localhost' IDENTIFIED BY 'pass';
```

```sql
GRANT ALL PRIVILEGES ON dbname.* TO 'user'@'localhost';
```

```sql
FLUSH PRIVILEGES;
```

## Others

```sql
SHOW COLUMNS FROM tablename;   -- Show column details
ALTER TABLE tablename ADD COLUMN age INT;
ALTER TABLE tablename DROP COLUMN age;

```
