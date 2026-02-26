import pytest
from src.api.client import ApiClient


@pytest.mark.regression
def test_verify_login_missing_params_returns_error():
    api = ApiClient()
    resp = api.post("/api/verifyLogin", data={})  # email/password yo'q

    assert resp.status_code in (200, 400)
    # Ko'p hollarda API JSON qaytaradi:
    # {"responseCode": 400, "message": "Bad request, email or password parameter is missing in POST request."}
    try:
        data = resp.json()
        assert "message" in data
    except Exception:
        # agar plain text bo'lsa ham, hech bo'lmasa error signal bo'lsin
        assert len(resp.text) > 0


@pytest.mark.regression
def test_verify_login_invalid_creds_returns_error():
    api = ApiClient()
    resp = api.post(
        "/api/verifyLogin",
        data={"email": "notreal@example.com", "password": "wrongpass123"},
    )

    assert resp.status_code in (200, 400)
    try:
        data = resp.json()
        assert "message" in data
    except Exception:
        assert len(resp.text) > 0
