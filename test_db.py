
import psycopg2


hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = '@Blature'
port_id = 5432

conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
)

print(conn)

conn.close()