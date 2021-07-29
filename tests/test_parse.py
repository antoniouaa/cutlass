from cutlass.parse import load_codes_and_clean, Country


def test_load_codes_and_clean():
    codes = load_codes_and_clean()
    for country, code in codes.items():
        assert country != ""
        assert code != ""


def test_dataclasses():
    uk = Country("United Kingdom", "UK", "+44")

    assert str(uk) == "<Country United Kingdom extension=+44>"
