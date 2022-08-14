import psycopg2

conn = psycopg2.connect("dbname = new_postgres_db user = postgres password = 123456789")

cur = conn.cursor()

cur.execute("""
SELECT * FROM public.new_postgres_tb
ORDER BY id ASC 

""")