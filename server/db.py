import psycopg2

DB_PASSWORD = None

def setPass():
    global DB_PASSWORD
    with open('/run/secrets/db-password') as p_file:
        DB_PASSWORD = p_file.read()

def get_conn():
    return psycopg2.connect(host="db",dbname="crux_db", user="postgres", password=DB_PASSWORD)
    #for unit testing --- kiran you said you would handle the devops stuff
    #return psycopg2.connect(host="localhost",dbname="crux_db", user="postgres", password="test1234")


#Inserts, updates, deletes
def execute(query, params, retrieve=False):
    return_val = None
    with get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            if retrieve:
                temp = cursor.fetchone()
                return_val = temp[0]
        conn.commit()
    return return_val

#Selects
def retrieve(query, params):
    result = None
    with get_conn() as conn:
        with conn.cursor() as cursor:
            if params == None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)
            result = cursor.fetchall()
        conn.commit()
    return result