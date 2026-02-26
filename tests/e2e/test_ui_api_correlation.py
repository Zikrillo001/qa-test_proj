import pytest
from src.pages.home_page import HomePage
from src.pages.products_page import ProductsPage
from src.api.client import ApiClient


@pytest.mark.regression
def test_ui_products_exist_in_api(page, base_url):
    # UI: Products page'dan bir nechta product name olamiz
    HomePage(page).open(base_url)
    products = ProductsPage(page)
    products.open_products()
    ui_names = products.get_first_product_names(limit=5)

    assert len(ui_names) > 0

    # API: productsList
    api = ApiClient()
    resp = api.get("/api/productsList")
    assert resp.status_code == 200
    data = resp.json()

    api_names = {p.get("name") for p in data.get("products", []) if p.get("name")}
    assert len(api_names) > 0

    # UI dagi kamida bitta product API'da bo'lishi kerak
    assert any(name in api_names for name in ui_names)
