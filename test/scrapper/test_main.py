import pytest

from inmozer.scraper.__main__ import get_params


@pytest.mark.parametrize("inp, expected_result", [
    (["D:/projects/inmozer/inmozer/scraper/__main__.py", "--url",
      "https://www.idealista.com/venta-viviendas/palma-de-mallorca-balears-illes/"],
     "https://www.idealista.com/venta-viviendas/palma-de-mallorca-balears-illes/")
])
def test_params(inp, expected_result):
    result: dict[str, str] = get_params(inp)
    assert result.get("url") == expected_result
