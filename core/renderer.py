import zipfile
import tempfile
import shutil
from jinja2 import Template
from pathlib import Path

def render_odt(template_path: Path, context: dict, output_path: Path) -> Path:
    
    with tempfile.TemporaryDirectory() as tmpdir:
        shutil.unpack_archive(template_path, tmpdir)

        content_xml = Path(tmpdir) / "content.xml"
        xml_text = content_xml.read_text(encoding="utf-8")

        rendered_xml = Template(xml_text).render(**context)
        content_xml.write_text(rendered_xml, encoding="utf-8")

        # Repacking into a new .odt
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for path in Path(tmpdir).rglob("*"):
                zipf.write(path, path.relative_to(tmpdir))

        return output_path
