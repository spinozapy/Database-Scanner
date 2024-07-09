import os
import pymysql
import psycopg2
import sqlite3
import colorama

colorama.init()
clear_command = "cls" if os.name == "nt" else "clear"

def clear_screen():
    os.system(clear_command)

def print_info(title, info):
    print(colorama.Fore.GREEN + f"[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + f"{title}")
    print("")
    for key, value in info.items():
        if isinstance(value, list):
            print(colorama.Fore.YELLOW + f"{key}:")
            for item in value:
                print(colorama.Fore.LIGHTWHITE_EX + f"  {item}")
        else:
            print(colorama.Fore.YELLOW + f"{key}: " + colorama.Fore.LIGHTWHITE_EX + f"{value}")
    print("")

def test_sql_injection(cursor):
    print(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Testing for SQL injection vulnerabilities...")
    vulnerable = False
    test_queries = [
        "SELECT 1; DROP TABLE users; --",
        "SELECT * FROM users WHERE id = 1 OR 1=1",
    ]
    for query in test_queries:
        try:
            cursor.execute(query)
            if cursor.fetchall():
                vulnerable = True
        except Exception as e:
            pass
    
    if vulnerable:
        print(colorama.Fore.RED + "[Database Scanner]: " + colorama.Fore.LIGHTWHITE_EX + "SQL Injection vulnerability detected!")
    else:
        print(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTWHITE_EX + "No SQL Injection vulnerability detected.")

def test_weak_passwords(cursor):
    print(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Testing for weak passwords...")
    weak_passwords = ["123456", "password", "admin", "admin123"]
    vulnerable = False
    try:
        cursor.execute("SELECT username, password FROM users")
        users = cursor.fetchall()
        for user in users:
            if user[1] in weak_passwords:
                vulnerable = True
                print(colorama.Fore.RED + f"[Database Scanner]: " + colorama.Fore.LIGHTWHITE_EX + f"Weak password detected for user {user[0]}")
    except Exception as e:
        pass
    
    if not vulnerable:
        print(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTWHITE_EX + "No weak passwords detected.")

def scan_mysql(host, user, password, database):
    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        test_sql_injection(cursor)
        test_weak_passwords(cursor)
        connection.close()
    except Exception as e:
        print(colorama.Fore.RED + f"[Database Scanner]: " + colorama.Fore.LIGHTWHITE_EX + f"Error: {e}")

def scan_postgresql(host, user, password, database):
    try:
        connection = psycopg2.connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        test_sql_injection(cursor)
        test_weak_passwords(cursor)
        connection.close()
    except Exception as e:
        print(colorama.Fore.RED + f"[Database Scanner]: " + colorama.Fore.LIGHTWHITE_EX + f"Error: {e}")

def scan_sqlite(db_file):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        test_sql_injection(cursor)
        test_weak_passwords(cursor)
        connection.close()
    except Exception as e:
        print(colorama.Fore.RED + f"[Database Scanner]: " + colorama.Fore.LIGHTWHITE_EX + f"Error: {e}")

def main():
    while True:
        clear_screen()
        print(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Choose a database type to scan (type 'exit' to quit):")
        print("")
        print(colorama.Fore.YELLOW + "1 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "MySQL")
        print(colorama.Fore.YELLOW + "2 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "PostgreSQL")
        print(colorama.Fore.YELLOW + "3 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "SQLite")
        print("")

        choice = input(colorama.Fore.MAGENTA + "root@scanner:~$ " + colorama.Fore.WHITE).strip()

        if choice == '1':
            host = input(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter MySQL host: " + colorama.Fore.WHITE).strip()
            user = input(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter MySQL user: " + colorama.Fore.WHITE).strip()
            password = input(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter MySQL password: " + colorama.Fore.WHITE).strip()
            database = input(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter MySQL database: " + colorama.Fore.WHITE).strip()
            scan_mysql(host, user, password, database)
        elif choice == '2':
            host = input(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter PostgreSQL host: " + colorama.Fore.WHITE).strip()
            user = input(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter PostgreSQL user: " + colorama.Fore.WHITE).strip()
            password = input(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter PostgreSQL password: " + colorama.Fore.WHITE).strip()
            database = input(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter PostgreSQL database: " + colorama.Fore.WHITE).strip()
            scan_postgresql(host, user, password, database)
        elif choice == '3':
            db_file = input(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter SQLite database file path: " + colorama.Fore.WHITE).strip()
            scan_sqlite(db_file)
        elif choice.lower() == 'exit':
            break
        else:
            print(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.RED + "Invalid choice, please try again.")
        
        input(colorama.Fore.GREEN + "[Database Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Press Enter to continue...")

if __name__ == "__main__":
    main()
