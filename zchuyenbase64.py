# encode_excel.py
import base64

with open("data.xlsx", "rb") as f:
    encoded = base64.b64encode(f.read()).decode("utf-8")

with open("data_base64.txt", "w", encoding="utf-8") as out:
    out.write(encoded)
