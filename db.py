import psycopg2
from psycopg2.extras import RealDictCursor

def connect_to_postgres():
    try:
        conn = psycopg2.connect(host='localhost', database='postgres', user='postgres',
                            password='Cytel.123', cursor_factory=RealDictCursor)
        return conn
    except Exception as err:
        print(err)
        return None

