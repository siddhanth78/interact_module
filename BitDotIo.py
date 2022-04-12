import bitdotio

api_key = "3b9iR_UxKXsdA7Bi8aUu6tpSAAxMj"

b = bitdotio.bitdotio(api_key)

conn = b.get_connection()
cur = conn.cursor()