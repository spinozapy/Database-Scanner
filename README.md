# Database Scanner

**Database Scanner** is a professional Python tool designed to evaluate the security of databases. This tool performs various tests to identify SQL injection vulnerabilities, weak passwords, and other security issues.

## Requirements

- Python 3.x
- `pymysql` library (Install using `pip install pymysql`)
- `psycopg2` library (Install using `pip install psycopg2`)
- `colorama` library (Install using `pip install colorama`)

## Installation

1. Clone the repository.
2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file includes the following dependencies:

    ```
    pymysql
    psycopg2
    colorama
    ```

3. Run the tool:

    ```bash
    python main.py
    ```

## Usage

1. Start the Database Scanner:

    ```bash
    python main.py
    ```

2. Choose a database type:

    - `1` = MySQL
    - `2` = PostgreSQL
    - `3` = SQLite

3. Enter the database information:

    - **MySQL:** Host, username, password, and database name.
    - **PostgreSQL:** Host, username, password, and database name.
    - **SQLite:** Path to the database file.

4. The tool will perform the following tests:

    - Check for SQL injection vulnerabilities.
    - Test for weak passwords.

## Features

- **SQL Injection Testing:** Detects SQL injection vulnerabilities in the database.
- **Weak Password Testing:** Checks for weak passwords used by database users.
- **Support for Multiple Databases:** Allows scanning of MySQL, PostgreSQL, and SQLite databases.

## Example

```bash
Database Scanner
=================

Choose a database type to scan (type 'exit' to quit):

1  = MySQL
2  = PostgreSQL
3  = SQLite

root@you:~$ 1
[Database Scanner]: Enter MySQL host: localhost
[Database Scanner]: Enter MySQL user: root
[Database Scanner]: Enter MySQL password: mypassword
[Database Scanner]: Enter MySQL database: testdb

[Database Scanner]: Testing for SQL injection vulnerabilities...
[Database Scanner]: Testing for weak passwords...

```
## Usage Caution

- For educational or testing purposes only.
- Do not use for malicious activities.
- Follow ethical standards while using this tool.
