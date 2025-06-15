import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crm import create_app

def test_homepage(tmp_path):
    app = create_app({'SQLALCHEMY_DATABASE_URI': f'sqlite:///{tmp_path}/test.db'})
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
