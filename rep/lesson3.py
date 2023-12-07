import mysql.connector


try:
    sql_connection = mysql.connector.connect(
        user='db_almas_py', password='FP2233am',
        host='db4free.net', database='databasepy')
except Exception as err:
    print(err)

try:
    query_str = 'select name1, number2 from first_table'
    sql_cursor = sql_connection.cursor()
    sql_cursor.execute(query_str)

    for(name1, number2) in sql_cursor:
        print(f'number: {number2} name: {name1}')

except Exception as err:
    print(err)
finally:
    sql_connection.close()