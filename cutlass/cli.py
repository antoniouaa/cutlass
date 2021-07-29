import pathlib

import click

from cutlass.parse import parse_workbook, dump_workbook

# TODO: Fix test cases
# Temporary dirs aren't working atm for the tests. Gotta fix it


@click.command()
@click.argument("in_file")
@click.option("-o", "--out_file", default=None, help="Specified output file")
def run(in_file, out_file):
    try:
        in_path = pathlib.Path(in_file)
        workbook = parse_workbook(in_path)
    except FileNotFoundError:
        click.echo(f"File {in_file} does not exist")
        return
    try:
        out_path = pathlib.Path(out_file)
        dump_workbook(workbook, out_path)
        click.echo(f"Output dumped into {out_path}")
    except TypeError:
        click.echo(workbook)
