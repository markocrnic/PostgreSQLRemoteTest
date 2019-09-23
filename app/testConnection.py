import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="10.0.200.68",
                                  port="5432",
                                  database="testdb")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    # Print PostgreSQL table contents
    cursor.execute("SELECT * FROM employees;")
    record = cursor.fetchone()
    print(record)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")