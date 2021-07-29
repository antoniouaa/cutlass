import pandas

from cutlass.parse import (
    load_codes_and_clean,
    Country,
    parse_phonenumber,
    parse_workbook,
)


def test_load_codes_and_clean():
    codes = load_codes_and_clean()
    for country, code in codes.items():
        assert country != ""
        assert code != ""


def test_dataclasses():
    uk = Country("United Kingdom", "UK", "+44")

    assert str(uk) == "<Country United Kingdom extension=+44>"


def test_phonenumber_parse():
    phonenumber = pandas.Series(["+41 75 550 43 10"])
    parsed = parse_phonenumber(phonenumber)

    assert parsed[0] == "41755504310"
    assert parsed[1] == "Switzerland"
    assert parsed[2] == "CH"


def test_workbook_parse(workbook):
    wb = parse_workbook(workbook_path=workbook)
    assert len(wb) > 0