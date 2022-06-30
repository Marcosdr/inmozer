import sys
import scraper

def get_params(argv: list) -> dict[str, str]:
    result: dict[str, str] = dict()
    param: str = argv[1]
    result[param[2:]] = argv[2]
    return result


if __name__ == '__main__':
    params = get_params(sys.argv)
    print(f"pennis {params}")
    print(f"content {scraper.scrap(params['url'])}")
