import pytest
from typing import Iterator
from flask.testing import FlaskClient

from hgnc_gene_data_collector.app import create_app

# ------------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------------

@pytest.fixture
def client():

    app = create_app()

    app.config["TESTING"] = True

    app.config["DATA"] = [
        {
            "HGNC gene symbol": "ABC1",
            "HGNC ID": "HGNC:1",
            "Gene Name": "Alpha Beta Gamma 1",
        }
    ]

    with app.test_client() as client:
        yield client



# ------------------------------------------------------------------
# Home route tests
# ------------------------------------------------------------------

def test_home_page_status(client: FlaskClient) -> None:
    """
    Test that the home page returns HTTP 200.

    Parameters
    ----------
    client : FlaskClient
        Flask test client.
    """
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_contains_html(client: FlaskClient) -> None:
    """
    Test homepage returns HTML content.

    Checks that basic HTML structure is present.

    Parameters
    ----------
    client : FlaskClient
    """
    response = client.get("/")
    html = response.data.decode()

    assert "<html" in html.lower()
    assert "</html>" in html.lower()


def test_empty_search(client):

    response = client.post(
        "/search",
        data={"query": ""}
    )

    html = response.data.decode()

    assert response.status_code == 200
    assert "No query identified." in html


def test_invalid_gene(client):

    response = client.post(
        "/search",
        data={"query": "FAKEGENE"}
    )

    html = response.data.decode()

    assert response.status_code == 200
    assert "not found" in html



# ------------------------------------------------------------------
# Search route tests (happy path)
# ------------------------------------------------------------------

def test_valid_symbol(client):

    response = client.post(
        "/search",
        data={"query": "ABC1"}
    )

    html = response.data.decode()

    assert response.status_code == 200
    assert "Info for ABC1" in html
    assert "ABC1" in html
    assert "HGNC:1" in html

def test_search_valid_hgnc_id(client):

    response = client.post(
        "/search",
        data={"query": "HGNC:1"}
    )

    assert response.status_code == 200

    html = response.data.decode()

    assert "Info for HGNC:1" in html
    assert "ABC1" in html
    assert "HGNC:1" in html