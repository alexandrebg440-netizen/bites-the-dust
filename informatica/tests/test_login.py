from app import app


def test_login_page_renders_and_register_link_is_valid():
    client = app.test_client()
    response = client.get('/login')

    assert response.status_code == 200
    assert b'/register' in response.data
