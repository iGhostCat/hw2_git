import pytest

from src.decorators import log_output


def test_divide_foo_with_decorator(tmp_path, capsys):
    # Тестирование вывода в консоль
    file_log = tmp_path / "temporary_log"

    @log_output(filename=str(file_log))
    def divide_foo(base, divider):
        try:
            return base / divider
        except Exception as e:
            return f"Error {e}"

    divide_foo(1, 1)
    divide_foo("1", 1)

    # Открытие и чтение временного файла лога
    with open(file_log, "r", encoding="utf-8") as log:
        lines = log.readlines()

    assert len(lines) == 2  # Проверка наличия двух строк
    assert "Function divide_foo has been called with args=(1, 1), kwargs={}. Result: 1.0" in lines[0]
    assert (
        "Function divide_foo has been called with args=('1', 1), kwargs={}. Result: Error unsupported operand type(s) for /: 'str' and 'int'"
        in lines[1]
    )

    # Тестирование вывода в консоль
    @log_output()
    def divide_foo_console(base, divider):
        try:
            return base / divider
        except Exception as e:
            return f"Ошибка {e}"

    divide_foo_console(1, 1)
    divide_foo_console("1", 1)

    # Проверка консоли
    captured = capsys.readouterr()
    output = captured.out
    assert "Function divide_foo_console has been called with args=(1, 1), kwargs={}. Result: 1.0" in output
    assert "Function divide_foo_console has been called with args=('1', 1), kwargs={}. Result: Ошибка" in output
