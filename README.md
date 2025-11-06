
# ODT Template Renderer

  

A lightweight CLI tool that takes an ODT template (created with LibreOffice or OpenOffice) and renders it using JSON data, replacing variables and loops using Jinja2 syntax and then exports it to PDF or DOCX format.

The project focuses on the essential pipeline like:

- Read and parse `.odt` templates
- Render with Jinja2 (`{{ var }}`, `{% for %}` etc.)
- Fill with JSON data
- Convert to PDF or DOCX via LibreOffice (headless)
-  JSON Schema validation (**Experimental**)

---

  

## Features

  
| Feature | Description |
|-----------|-------------|
|Template Rendering  | Replaces placeholders in `.odt` using Jinja2 |
|JSON Input  | Inject dynamic values, lists, loops, and conditionals |
|CLI Based  | Typer-powered CLI with `render` and `validate` commands |
|Output Formats  | Exports `.odt`, `.pdf`, and `.docx` using LibreOffice headless |
|Modular structure  | (`renderer`, `converter`, `validator`) for modular code implementation |
|Data Validation (EXP) | Validates JSON data against a JSON Schema |

---

## Project Structure

>ODTXPDF/
> ├── cli.py    
> ├── core/    
> │ ├── init.py    
> │ ├── renderer.py    
> │ ├── converter.py     
> │ └── validator.py    
> ├── examples/    
> │ ├── certificate.odt     
> │ └── data.json   
> ├── requirements.txt  
> └── README.md

  

---

  

## How It Works

  

### Step 1 - Input Files

User provides:

1. An `.odt` template with placeholders (like `{{ name }}`, `{% for %}` loops, etc.)

2. A `.json` file with data to fill those placeholders.

  

*Example:*
 - *template (`certificate.odt`) and Example data (`data.json`)*

  

### Step 2 - Rendering

1. The `.odt` is unzipped (since it’s just a ZIP file with XMLs).

2. The `content.xml` file is loaded.

3. It’s passed through Jinja2 for rendering.

4. The filled XML is zipped back into a valid `.odt` file.

  

### Step 3 — Conversion

- Finally, LibreOffice (headless mode) converts it to:

- - .pdf → via --convert-to pdf OR

- - .docx → via --convert-to docx
---

## Usage

### 1. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Ensure LibreOffice is installed
```bash
sudo apt install libreoffice
```
### 3. Run the CLI to render an ODT file
```bash
python cli.py render examples/certificate.odt examples/data.json --out out/ --pdf
```

#### Renders certificate.odt with values from data.json and stores in out/ folder.

```bash
out/output.odt
out/output.pdf
```
#### Validate JSON against a schema **(EXPERIMENTAL)**
```bash
python cli.py validate examples/schema.json examples/data.json
```
