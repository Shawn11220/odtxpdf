import typer
from core.renderer import render_odt
from core.converter import convert_with_soffice
from core.validator import validate_json
from pathlib import Path
import json

app = typer.Typer(help="ODT Template Renderer CLI")

@app.command()
def render(
    template: Path = typer.Argument(..., help="Path to .odt template"),
    data: Path = typer.Argument(..., help="Path to JSON data file"),
    out: Path = typer.Option(Path("out"), help="Output folder"),
    pdf: bool = typer.Option(True, help="Export PDF"),
    docx: bool = typer.Option(False, help="Export DOCX"),
):
    """Render ODT with JSON data, export to PDF/DOCX."""
    out.mkdir(parents=True, exist_ok=True)

    typer.echo("Loading data...")
    context = json.load(open(data))

    typer.echo("Rendering template...")
    rendered_odt = render_odt(template, context, out / "output.odt")

    if pdf:
        typer.echo("Converting to PDF...")
        convert_with_soffice(rendered_odt, out, "pdf")

    if docx:
        typer.echo("Converting to DOCX...")
        convert_with_soffice(rendered_odt, out, "docx")

    typer.echo("Done!")

@app.command()
def validate(schema: Path, data: Path):
    """Validate JSON against schema."""
    validate_json(schema, data)

if __name__ == "__main__":
    app()
