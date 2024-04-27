# retriever

# Installation

- Install PostgreSQL

```bash
brew install postgresql
```

- Connect to PostgreSQL

```bash
psql -U postgres
```

- Create database

```sql
CREATE DATABASE retriever;
```

- Create user

```bash
create user rag with password 'rag123';
```

- Grant all privileges to the user

```bash
GRANT ALL PRIVILEGES ON database retriever to rag;
```
