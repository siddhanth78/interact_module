import bitdotio

api_key = "3bBzT_S2RgBz46xD6Xu4VbZ6zv73L"

b = bitdotio.bitdotio(api_key)

conn = b.get_connection()
cur = conn.cursor()
<<<<<<< HEAD

cur.execute("""

select * from "siddhanth78/MainGame".characters

""")

for x in cur.fetchall():
    print(f"{x[0]}\t{x[1]}\t{x[2]}\t{x[3]}\t{x[4]}")
=======
>>>>>>> 53489572d696870eb13fd47d2eca42296f7eb8fd