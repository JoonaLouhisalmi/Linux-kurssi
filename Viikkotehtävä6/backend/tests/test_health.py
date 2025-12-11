import app


def test_health_endpoint():
    """Varmentaa, että /api/health toimii."""
    client = app.app.test_client()
    resp = client.get("/api/health")

    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get("status") == "ok"
