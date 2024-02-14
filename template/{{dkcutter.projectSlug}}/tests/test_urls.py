from http import HTTPStatus

from django.urls import resolve
from django.urls import reverse


def test_home(admin_client):
    url = reverse("home")
    assert resolve(url).view_name == "home"
    response = admin_client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert "pages/home.html" in [t.name for t in response.templates]
    assert "Hello World" in response.content.decode()
