import datetime

from src.task import Task

def test_task_init(task):
    assert task.name == "Купить помидоры"
    assert task.description == "Купить помидоры для салата"
    assert task.status == 'Ожидание старта'
    assert task.created_at == "20.06.2024"

def test_task_create():
    task = Task("Купить огурцы", "Купить огурцы для салата")
    task.name = "Купить огурцы"
    task.description = "Купить огурцы для салата"
    task.status = 'Ожидание старта'
    task.created_at = datetime.datetime.now().date().strftime('%d.%m.%Y')

def test_task_update(capsys, task):
    task.created_at = "29.06.2021"
    message = capsys.readouterr()
    assert message.out.strip() == 'Нельзя изменять дату создания на дату из прошлого'

    task.created_at = datetime.datetime.now().date().strftime('%d.%m.%Y')
    assert  task.created_at == datetime.datetime.now().date().strftime('%d.%m.%Y')

def test_task_str(task):
    assert str(task) == "Купить помидоры, Статус выполнения: Ожидание старта, Дата создания: 20.06.2024"

def test_task_add(task_with_runtime1, task_with_runtime2):
    assert task_with_runtime1 + task_with_runtime2 == 130