import os
from bs4 import BeautifulSoup


def load_index():
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "index.html")
    with open(path, encoding="utf-8") as f:
        return BeautifulSoup(f, "html.parser")


def test_header_exists():
    soup = load_index()
    assert soup.find('h1') is not None


def test_section_exists():
    soup = load_index()
    assert soup.find('section') is not None


def test_footer_exists():
    soup = load_index()
    assert soup.find('footer') is not None
