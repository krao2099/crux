import psycopg2

def get_conn():
    return psycopg2.connect(host="localhost",dbname="crux_db", user="postgres", password="test1234")

def execute(query, params):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.commit()
    conn.close()

    return result