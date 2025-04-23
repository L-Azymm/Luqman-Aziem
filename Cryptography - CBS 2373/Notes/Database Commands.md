# 📦 Most Used Database Commands

## 🔐 Accessing the Database

- Login to MySQL

```sh
mysql -u root -p           
```

- Login to PostgreSQL

```sh
psql -U postgres           
```

- Open SQLite database

```sh
sqlite3 mydb.db            
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

- Switch to database

```sql
USE dbname;                
```

- Delete a database

```sql
DROP DATABASE dbname;      
```

## Table Management

- Create table

```sql
CREATE TABLE tablename (
  id INT PRIMARY KEY,
  name VARCHAR(50)
);                         
```

- List tables

```sql
SHOW TABLES;              
```

- Show table structure

```sql
DESCRIBE tablename;       
```

- Delete table

```sql
DROP TABLE tablename;      
```

## Data Operations

- Add data

```sql
INSERT INTO tablename (id, name) VALUES (1, 'Alice');  
```

- Get all data

```sql
SELECT * FROM tablename;                               
```

- Edit data

```sql
UPDATE tablename SET name = 'Bob' WHERE id = 1;        
```

- Remove data

```sql
DELETE FROM tablename WHERE id = 1;                    
```

## Query Helpers

- Search by pattern

```sql
SELECT * FROM tablename WHERE name LIKE 'A%';   
```

- Sort results

```sql
ORDER BY name ASC;                              
```

- Limit results

```sql
LIMIT 10;                                       
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

- Show column details

```sql
SHOW COLUMNS FROM tablename;  
```

- Adding Column

```sql
ALTER TABLE tablename ADD COLUMN age INT;
```

- Removing a column

```sql
ALTER TABLE tablename DROP COLUMN age;
```
