import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from typing import Literal


app = typer.Typer(help="Tenrek is C++ code complexity analyzer tool")
console = Console()


def make_clang_args(standard: str):
    return [f"-std=c++{standard[-2:]}"]


def analyze_file(path: Path, standard: str):
    from tenrek.parser import CppParser
    from tenrek.analyzer import ComplexityAnalyzer

    parser = CppParser(path, standard=standard)
    parser.parse()

    analyzer = ComplexityAnalyzer(parser, standard=standard)
    return analyzer.analyze()


def show_result(result: list):
    table = Table(title="Analysis Result")

    table.add_column("Name", style="cyan")
    table.add_column("Type")
    table.add_column("Metric")
    table.add_column("Value", style="magenta")

    for item in result:
        name = item.get("name", "")
        typ = item.get("type", "")

        for key, value in item.items():
            if key in ["name", "type"]:
                continue
            table.add_row(name, typ, key, str(value))

    console.print(table)


def show_multiple(results: list):
    for res in results:
        show_result(res)


@app.command()
def file(
    path: Path = typer.Argument(..., exists=True),
    standard: Literal["cpp11", "cpp14", "cpp17", "cpp20", "cpp23"] = typer.Option(
        "cpp17", "--standard", help="C++ standard"
    ),
):
    """
    Analyze single file
    """
    console.print(f"[bold green]Analyzing file:[/bold green] {path}")

    result = analyze_file(path, standard)

    show_result(result)

@app.command()
def folder(
    path: Path = typer.Argument(..., exists=True),
    standard: Literal["cpp17", "cpp20", "cpp23"] = typer.Option(
        "cpp17", "--standard", help="C++ standard"
    ),
):
    """
    Analyze folder
    """
    console.print(f"[bold blue]Analyzing folder:[/bold blue] {path}")

    results = []

    for file in path.rglob("*.cpp"):
        results.append(analyze_file(file, standard))

    show_multiple(results)