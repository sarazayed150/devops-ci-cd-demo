import os
import sys

# إضافة المسار الحالي إلى مسارات بايثون لضمان التعرف على app.py مباشرة
sys.path.insert(0, os.path.dirname(__file__))

from app import app


def test_home():
  client = app.test_client()
  response = client.get("/")
  assert response.status_code == 200
  assert response.json["status"] == "healthy"
