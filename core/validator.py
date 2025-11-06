import json
from jsonschema import validate, ValidationError

def validate_json(schema_file, data_file):
    """Validate a JSON file against a schema."""
    schema = json.load(open(schema_file))
    data = json.load(open(data_file))

    try:
        validate(instance=data, schema=schema)
        print("JSON is valid!")
    except ValidationError as e:
        print(f"Validation error: {e.message}")
