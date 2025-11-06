import subprocess
from pathlib import Path

def convert_with_soffice(odt_file: Path, outdir: Path, fmt: str):
    """Use LibreOffice headless to convert ODT → PDF/DOCX."""
    result = subprocess.run([
        "soffice",
        "--headless",
        "--convert-to", fmt,
        "--outdir", str(outdir),
        str(odt_file)
    ], capture_output=True)

    if result.returncode != 0:
        print(result.stderr.decode())
        raise RuntimeError("LibreOffice conversion failed.")
