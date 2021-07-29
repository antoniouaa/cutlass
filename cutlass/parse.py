import re
import json
import pathlib
from typing import Dict
from dataclasses import dataclass

import pandas


@dataclass
class Country:
    name: str
    short_name: str
    extension: str

    def __str__(self):
        return f"<Country {self.name} extension={self.extension}>"


def load_codes_and_clean(
    codes_path: pathlib.Path = pathlib.Path("codes/codes.json"),
    names_path: pathlib.Path = pathlib.Path("codes/names.json"),
) -> Dict[str, Country]:
    with open(codes_path) as codes_file:
        codes = json.load(codes_file)
    with open(names_path) as names_file:
        names = json.load(names_file)
    countries = {}
    for country, code in codes.items():
        extension = re.sub(r"([a-zA-Z\s\-\+])", "", code)
        if extension != "":
            countries[country] = Country(
                name=names[country],
                short_name=country,
                extension=extension,
            )
    return countries


def parse_phonenumber(row: pandas.Series) -> pandas.Series:
    codes = load_codes_and_clean()
    number = re.sub(r"([a-zA-Z\s\-\+])", "", row[0])
    for _, country in codes.items():
        if number.startswith(country.extension):
            return pandas.Series([number, country.name, country.short_name])


def parse_workbook(workbook_path: pathlib.Path) -> pandas.DataFrame:
    wb = pandas.read_excel(workbook_path)
    wb[["Parsed", "Country", "Short"]] = wb.apply(parse_phonenumber, axis=1)
    return wb
