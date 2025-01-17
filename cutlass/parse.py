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
        extension = re.sub(r"([\s\-\+])", "", code)
        # TODO: Figure out multiple extension codes eg Dominican Republic
        if re.search(r"[a-zA-Z]+", extension):
            continue
        if extension != "":
            countries[country] = Country(
                name=names[country],
                short_name=country,
                extension=extension,
            )
    return countries


# TODO[Enhancement]: Possibility for malformed home numbers
# Some dummies might include home specific digits like the UK's
# (0) in their international number. eg +44 (0)xxxx xxxxxx


def parse_phonenumber(row: pandas.Series) -> pandas.Series:
    codes = load_codes_and_clean()
    number = re.sub(r"(^0+|\+0*|\s|-|^\(0+|\(|\))", "", row[0])
    for _, country in codes.items():
        if number.startswith(country.extension):
            return pandas.Series([number, country.name, country.short_name])


def parse_workbook(workbook_path: pathlib.Path) -> pandas.DataFrame:
    wb = pandas.read_excel(workbook_path)
    wb[["Parsed", "Country", "Short"]] = wb.apply(parse_phonenumber, axis=1)
    return wb


def reset_index(workbook: pandas.DataFrame) -> None:
    workbook.index = pandas.RangeIndex(start=1, stop=len(workbook) + 1)


def dump_workbook(workbook: pandas.DataFrame, out_file: pathlib.Path) -> None:
    try:
        existing = pandas.read_excel(out_file, converters={"Parsed": str})
        whole = pandas.concat([existing, workbook], join="inner")
        whole.drop_duplicates(subset=["Parsed", "Company"], keep="first", inplace=True)
    except FileNotFoundError:
        whole = workbook

    whole = whole.sort_values(["Country", "Parsed"])
    reset_index(whole)
    whole.to_excel(out_file, sheet_name="Parsed Phone numbers")
