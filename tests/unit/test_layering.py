"""Architecture test: the inner layers import no web framework."""

import ast
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[2] / "src" / "personal_site"
INNER_LAYERS = ("domain", "application")
OUTER_PACKAGES = {"flask", "werkzeug", "jinja2", "personal_site.presentation"}


def imported_modules(path: Path) -> set[str]:
    modules: set[str] = set()
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module)
    return modules


def test_domain_and_application_import_no_framework_or_presentation() -> None:
    offenders = []
    for layer in INNER_LAYERS:
        for path in (PACKAGE / layer).glob("*.py"):
            for module in imported_modules(path):
                if any(
                    module == outer or module.startswith(outer + ".")
                    for outer in OUTER_PACKAGES
                ):
                    offenders.append(f"{path.name} imports {module}")
    assert offenders == []


def test_domain_imports_no_application_or_infrastructure() -> None:
    offenders = []
    for path in (PACKAGE / "domain").glob("*.py"):
        for module in imported_modules(path):
            if module.startswith(
                ("personal_site.application", "personal_site.infrastructure")
            ):
                offenders.append(f"{path.name} imports {module}")
    assert offenders == []
