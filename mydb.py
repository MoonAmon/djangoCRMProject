import psycopg2

database = psycopg2.connect(
    host='localhost',
    dbname='GCOM_Comercial',
    user='postgres',
    port='5434'
)

# Prepare a cursor object
cursorObject = database.cursor()

# Close the connection
database.close()

print("All Done!!")
