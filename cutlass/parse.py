import json
import pathlib


def load_codes_and_clean(in_file: pathlib.Path = pathlib.Path("codes/codes.json")) -> dict:
    with open(in_file) as codes:
        codes = json.load(codes)
    return {country: code for country, code in codes.items() if not code == ""}
