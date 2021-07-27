from cutlass.parse import load_codes_and_clean


def test_load_codes_and_clean():
    codes = load_codes_and_clean()
    for country, code in codes.items():
        assert country != ""
        assert code != ""
