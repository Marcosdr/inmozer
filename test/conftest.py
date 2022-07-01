from pathlib import Path
import pytest

def data_folder():
    return str(Path(__file__).parent)

@pytest.fixture()
def page_idealista_property_listing():
    with open(data_folder() + '/data/html/idealista/property_listing.html') as file:
        return file.read()
