from src.task import Task
from src.periodic_task import PeriodicTask
from src.deadline_task import DeadlineTask

def test_print_mixin(capsys):
    Task("Купить помидоры", "Купить помидоры для салата", created_at="20.06.2024")
    message = capsys.readouterr()
    assert message.out.strip() == "Task(Купить помидоры, Купить помидоры для салата, Ожидание старта, 20.06.2024)"

    PeriodicTask("Купить огурцы", "Купить огурцы для салата", "01.07.2024", "01.08.2024", run_time=60, created_at="20.06.2024")
    message = capsys.readouterr()
    assert message.out.strip() == "PeriodicTask(Купить огурцы, Купить огурцы для салата, Ожидание старта, 20.06.2024)"

    DeadlineTask("Купить перец", "Купить перец для салата", "25.07.2024", run_time=60, created_at="20.06.2024")
    message = capsys.readouterr()
    assert message.out.strip() == "DeadlineTask(Купить перец, Купить перец для салата, Ожидание старта, 20.06.2024)"

