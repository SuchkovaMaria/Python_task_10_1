from src.decorators import log


def test_log_1():
    @log(filename="file_log.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    assert my_function(1, 2) == 3


def test_log_2(capsys):
    @log()
    def my_func(x, y):
        return x + y

    my_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_func ok\n"


def test_log_3(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "my_function error:TypeError. Inputs: (1, '2'), {}. unsupported operand type(s) for +: 'int' and 'str'\n"
    )


def test_log_4(capsys):
    @log()
    def my_function(x, y):
        return x / y

    my_function(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error:ZeroDivisionError. Inputs: (1, 0), {}. division by zero\n"
