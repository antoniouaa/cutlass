import pathlib

import pandas
from click.testing import CliRunner

from cutlass.cli import run


def test_run_no_out_file(tmp_path, workbook):
    runner = CliRunner()
    print(workbook.name)
    print(tmp_path)
    file_name = pathlib.Path(workbook.name).name
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(run, [file_name])

        assert result.exit_code == 0
        # assert "Parsed" in result.output


def test_run_with_out_file(tmp_path, workbook):
    out_file = "test.xlsx"

    runner = CliRunner()
    file_name = pathlib.Path(workbook.name).name
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(run, [file_name, "-o", out_file])

        assert result.exit_code == 0
        # assert f"Output dumped into {out_file}" in result.output
        # out_ = pandas.read_excel(out_file)
        # assert "Parsed" in out_.columns
        # assert pathlib.Path(out_file).exists()
