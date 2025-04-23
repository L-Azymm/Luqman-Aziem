# MySQL

  The MySQL command-line tool.
  More information: <https://www.mysql.com/>.

- Connect to a database:

```sql
      mysql database_name
```

- Connect to a database, user will be prompted for a password:

```sh
      mysql -u user --password database_name
```

- Connect to a database on another host:

```sql
mysql -h database_host database_name
```

- Connect to a database through a Unix socket:

```sql
      mysql --socket path/to/socket.sock
```

- Execute SQL statements in a script file (batch file):

```sql
      mysql -e "source filename.sql" database_name
```

- Restore a database from a backup created with `mysqldump` (user will be prompted for a password):

```sql
      mysql --user user --password database_name < path/to/backup.sql
```

- Restore all databases from a backup (user will be prompted for a password):

```sql
      mysql --user user --password < path/to/backup.sql
```
