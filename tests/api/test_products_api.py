import pytest
from src.api.client import ApiClient

@pytest.mark.smoke
def test_products_list_returns_data():
    api = ApiClient()
    resp = api.get("/api/productsList")

    assert resp.status_code == 200

    data = resp.json()
    # API odatda {"products":[...], ...} ko'rinishida qaytadi
    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0

    first = data["products"][0]
    # Minimal invariantlar (portfolio signal)
    assert "id" in first
    assert "name" in first