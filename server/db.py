import psycopg2

def get_conn():
    return psycopg2.connect(host="localhost",dbname="crux_db", user="postgres", password="test1234")


#prob could make this one function with optional params but not sure what is easier
def execute(query, params):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.commit()
    conn.close()

    return result

def execute(query):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    conn.close()

    return result