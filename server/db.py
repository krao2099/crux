import psycopg2

DB_PASSWORD = None

def setPass():
    global DB_PASSWORD
    with open('/run/secrets/db-password') as p_file:
        DB_PASSWORD = p_file.read()

def get_conn():
    return psycopg2.connect(host="db",dbname="crux_db", user="postgres", password=DB_PASSWORD)


#prob could make this one function with optional params but not sure what is easier
def execute(query, params):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def retrieve(query, params):
    conn = get_conn()
    cursor = conn.cursor()
    if params == None:
        cursor.execute(query)
    else:
        cursor.execute(query, params)
    result = cursor.fetchall()
    conn.commit()
    conn.close()

    return result