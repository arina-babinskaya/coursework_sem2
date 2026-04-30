import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import os
from typing import List, Optional
from enum import Enum


# Инициализация Typer и Rich
app = typer.Typer(rich_markup_mode="rich")
console = Console()

# Перечисление для стандартов C++
class CppStandard(str, Enum):
    cpp11 = "c++11"
    cpp14 = "c++14"
    cpp17 = "c++17"
    cpp20 = "c++20"
    cpp23 = "c++23"

@app.command()
def analyze(
    paths: List[Path] = typer.Argument(
        ..., 
        help="Список файлов или папок для анализа."
    ),
    standard: Optional[CppStandard] = typer.Option(
        None, 
        "--std", 
        help="Стандарт C++ для парсера."
    )
):
    """
    [bold green]Программа для статического анализа C++ кода.[/bold green]
    Позволяет рассчитать метрики сложности, LOC, Halstead и индекс поддерживаемости.
    """
    console.print(Panel("[bold cyan]Запуск анализа проекта[/bold cyan]", expand=False))

    valid_paths = []
    
    # 1. Проверка существования файлов и папок
    for path in paths:
        if not path.exists():
            console.print(f"[bold red]Ошибка:[/bold red] Путь '{path}' не существует!", style="red")
            continue
        valid_paths.append(path)
        
    if not valid_paths:
        console.print("[bold red]Критическая ошибка:[/bold red] Не указано ни одного валидного пути для анализа.")
        raise typer.Exit(code=1)

    # 2. Вывод выбранных параметров в виде таблицы Rich
    table = Table(title="Параметры запуска", title_style="bold magenta")
    table.add_column("Параметр", style="cyan")
    table.add_column("Значение", style="green")

    # Форматируем список путей для красивого вывода
    paths_str = "\n".join([str(p.resolve()) for p in valid_paths])
    table.add_row("Объекты анализа", paths_str)
    table.add_row("Стандарт C++", standard.value if standard else "[yellow]По умолчанию[/yellow]")

    console.print(table)

    # 3. Здесь вы вызываете функции из вашего analyzer.py или parser.py
    with console.status("[bold blue]Выполняется анализ кода...[/bold blue]"):
        # Имитация работы
        import time
        time.sleep(1.5) 
        
        # Пример интеграции с вашим кодом:
        # from analyzer import run_analysis
        # run_analysis(paths=valid_paths, cpp_std=standard.value if standard else "c++17")

    console.print("\n[bold green]🎉 Анализ успешно завершен![/bold green]")

if __name__ == "__main__":
    app()
