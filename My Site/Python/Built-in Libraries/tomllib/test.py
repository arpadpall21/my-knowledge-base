from tomllib import load, loads

with open('./pyproject.toml', 'br') as f:
    print(load(f))


toml_str = """
[tool.poetry]
name = "test project"
version = "1.0.0"

[tool.poetry.dependencies]
python = ">=3.10,<3.11"
fastapi = "^0.109.0"
uvicorn = {extras = ["standard"], version = "^0.27.0.post1"}
pandas = "2.1.4"
pydantic = "^2.7.1"
numpy = "<1.24"
deepmerge = "^2.0"
pytest-env = "^1.1.5"
"""

print(loads(toml_str))