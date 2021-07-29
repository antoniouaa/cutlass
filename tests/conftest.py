import io
from tempfile import NamedTemporaryFile
import pytest
from openpyxl import Workbook


@pytest.fixture(scope="function")
def workbook(tmp_path):
    wb = Workbook()
    ws = wb.active
    ws.append(("Phone", "Company"))
    ws.append(("+41 75 550 43 10", "Dibbert - Blanda"))

    with NamedTemporaryFile(delete=False, dir=tmp_path) as temp_workbook:
        wb.save(temp_workbook.name)
        # yield io.BytesIO(temp_workbook.read())
        yield temp_workbook
