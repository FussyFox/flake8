"""Lambda function that executes flake8, a static file linter."""
from lintipy import CheckRun


handle = CheckRun.as_handler(
    'flake8',
    'flake8', '--jobs', '1', '.'
)
