import os
import sys

# ضمان رؤية مسار التطبيق سواء تم التشغيل من المجلد الرئيسي أو الداخلي
sys.path.insert(0, os.path.dirname(__file__))

from app import app


def test_home():
  client = app.test_client()
  response = client.get("/")
  assert response.status_code == 200
  assert response.json["status"] == "healthy"
