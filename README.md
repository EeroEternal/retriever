# retriever

# Installation

## PostgreSQL

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

# Configuration

## Poetry

- Install dependencies

```bash
poetry install
```

- Activate virtual environment

```bash
poetry shell
```

- Get the path of the virtual environment

```bash
poetry env info --path
```

Output:

```bash
Virtualenv
Python:         3.11.4
Implementation: CPython
Path:           /Users/lipi/Library/Caches/pypoetry/virtualenvs/retriever-JKRSsXxj-py3.11
Executable:     /Users/lipi/Library/Caches/pypoetry/virtualenvs/retriever-JKRSsXxj-py3.11/bin/python
Valid:          True
```

- Set the path of the virtual environment in the `.env` file

```bash
echo "VIRTUAL_ENV_PATH=/Users/lipi/Library/Caches/pypoetry/virtualenvs/retriever-JKRSsXxj-py3.11" > .env
```

- Add env variables to pyrightconfig.json

```json
{
  "venvPath": "/Users/lipi/Library/Caches/pypoetry/virtualenvs",
  "venv": "retriever-JKRSsXxj-py3.11"
}
```
