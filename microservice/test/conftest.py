from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
pytest_plugins = (
  "fixtures.speed",
  "fixtures.heatmap",
  "fixtures.time",
  "fixtures.distance",  
)
