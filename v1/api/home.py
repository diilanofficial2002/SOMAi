import requests
import time
import random
import os

from dotenv import load_dotenv
load_dotenv()

URL = "https://expenditures-inc-evaluating-symphony.trycloudflare.com/webhook/SOMAi-home"
TOKEN = os.getenv("N8N_TOKEN")

if not TOKEN:
    raise RuntimeError("N8N_TOKEN is not set in .env")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "user_brief": "มีสินค้า ไก่ย่าง เพื่อทำโฆษณาลงโซเชียลแบบไม่ต้องมีรูป ราคาไม้ละ20บาท ไก่หมักสมุนไพรด้วย",
    "platformIds": ["Facebook", "Tiktok"],
    "temp": "https://5shwv7n9-5000.asse.devtunnels.ms/api/test_gen_content"
}

r = requests.post(URL, json=payload, headers=HEADERS)

print("STATUS:", r.status_code)
print("HEADERS:", r.headers.get("content-type"))

if r.headers.get("content-type", "").startswith("application/json"):
    print("JSON:", r.json())
    # JSON: {'message': 'Workflow was started'}
else:
    print("TEXT:", r.text)
