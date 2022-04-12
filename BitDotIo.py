import bitdotio

api_key = "3bBzT_S2RgBz46xD6Xu4VbZ6zv73L"

b = bitdotio.bitdotio(api_key)

conn = b.get_connection()
cur = conn.cursor()
