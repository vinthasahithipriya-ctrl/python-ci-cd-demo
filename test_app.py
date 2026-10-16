from app import app


def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_add():
    r = app.test_client().get("/add/2/3")
    assert r.get_json()["result"] == 5
