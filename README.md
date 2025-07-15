# Aviation
Learn the fundamentals of transform-based low-order modelling and analysis.

## Developer guide
- Using venv for virt env
- install MK Docs
- Serve the documentation website. To serve the site locally run 
```
mkdocs serve
```

## Dependencies
First install the virtual environment:
```
python3 -m venv .venv
```
Then activate it:
```
source .venvbin/activate
```
Then install dependencies:
```
pip install mkdocs
```

Or instead use [uv](https://docs.astral.sh/uv/) for comprehensive project management. Dependency bounds are defined in [`pyproject.toml`](pyproject.toml) and the locked environment is specified in [`uv lock`](uv.lock). 
To create the virtual environment from lockfile, and install the dependencies inside a virtual environement using [venv](https://docs./python.org/3/library/venv.), make sure you have installed uv and run html, run:
```
uv sync
```

### Documentation 
This repositiry uses [MKDocs](https://www.mkdocs.org) to generate static documentation site for users. The source files for the site can be fouind in the [`docs`](docs) directory and site configuration in [`mkdocs.yml`](mkdocs.yml). To serve the site locally, run: 
```
uv run mkdocs serve
```
