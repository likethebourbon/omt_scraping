import os
from pathlib import Path
from PyPDF2 import PdfFileMerger

# files = Path.cwd().joinpath("omt").joinpath("assignment_pdfs").joinpath("assignment_pdfs").resolve()
files = Path.cwd().joinpath("assignment_pdfs").joinpath("assignment_pdfs").resolve()

sorted_files = sorted(files.iterdir(), key=os.path.getmtime)

merger = PdfFileMerger()

for file in sorted_files:
    merger.append(file.as_posix(), bookmark=file.as_posix().split("/")[-1][:-4])

merger.write(
    Path.cwd()
    # .joinpath("omt")
    .joinpath("assignment_pdfs")
    .joinpath("joined")
    .joinpath("omt_workbook.pdf")
    .as_posix()
)
