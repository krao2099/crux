import psycopg2

def db_insert(query, record):
    conn = psycopg2.connect(host="localhost",dbname="crux_db", user="postgres", password="test1234")
    cursor = conn.cursor()
    cursor.execute(query, record)
    conn.commit()
    conn.close()
    print("Query success")