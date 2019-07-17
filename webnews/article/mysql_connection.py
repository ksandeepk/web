import mysql.connector
conn  = mysql.connector.connect(user  =  'pnv'
                               password = 'password'
                               host  =  'localhost'
                               database  = 'webnews')


cursor = conn.cursor()


query   = "select * from sample_table2 limit 5"
cursor.execute(query)
for a, b, c, d, e in cursor:
    print a, b, c, d, e



cursor.close()
conn.close()