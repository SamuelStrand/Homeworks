import psycopg2

conn = psycopg2.connect(dbname='new_postgres_db', user='postgres', password='123456789', host='localhost')
cursor = conn.cursor()

data_arr = [
    [25, 'true', 'Sarah'],
    [30, 'true', 'Brendon'],
    [18, 'false', 'Marta'],
    [19, 'false', 'James'],
    [23, 'true', 'Nicole'],
]

index = 0
for i in data_arr:
    index += 1
    query_string = f"""
    INSERT INTO public.new_postgres_db (id, age, is_have_money, name)
    VALUES ({index}, {i[0]}, {i[1]}, '{i[2]}')
    """
    cursor.execute(query_string)
    conn.commit()
cursor.close()
conn.close()

conn = psycopg2.connect(dbname='new_postgres_db', user='postgres', password='123456789', host='localhost')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM public.new_postgres_db
WHERE age > 20
ORDER BY id ASC
""")
records = cursor.fetchall()
for i in records:
    print(i)
cursor.close()
conn.close()
