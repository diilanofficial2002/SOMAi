import requests
import os
import json # import json เพื่อใช้จัด format ตอน print

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

print("Sending request to n8n...")

try:
    # เพิ่ม timeout เป็น 60 วินาที (หรือมากกว่านี้ถ้า AI ทำงานช้ามาก)
    # เพราะเราเปลี่ยน n8n ให้รอจนจบ Flow การตอบกลับจะช้าลง
    r = requests.post(URL, json=payload, headers=HEADERS, timeout=120)

    print("STATUS:", r.status_code)

    if r.status_code == 200:
        # ถ้า n8n ตั้งค่าถูกต้อง มันจะส่ง JSON ผลลัพธ์สุดท้ายกลับมาที่นี่
        try:
            data = r.json()
            print("--- RESULT FROM WORKFLOW ---")
            print(json.dumps(data, indent=4, ensure_ascii=False))
        except ValueError:
            print("Response is not JSON:", r.text)
    else:
        print(f"Error: {r.status_code}")
        print(r.text)

except requests.exceptions.Timeout:
    print("Error: Request timed out. Workflow took too long to complete.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")