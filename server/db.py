import psycopg2

DB_PASSWORD = None

def setPass():
    global DB_PASSWORD
    with open('/run/secrets/db-password') as p_file:
        DB_PASSWORD = p_file.read()

def get_conn():
    return psycopg2.connect(host="db",dbname="crux_db", user="postgres", password=DB_PASSWORD)


#prob could make this one function with optional params but not sure what is easier
def execute(query, params, retrieve=False):
    return_val = None
    with get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            if retrieve:
                temp = cursor.fetchone()
                print(temp)
                return_val = temp[0]
                print(return_val)
        conn.commit()
    return return_val

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