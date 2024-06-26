import pytest

def test_deadline_task_init(task_deadline1):

    assert task_deadline1.name == "Купить перец"
    assert task_deadline1.description == "Купить перец для салата"
    assert task_deadline1.created_at == "20.06.2024"
    assert task_deadline1.status == 'Ожидание старта'
    assert task_deadline1.deadline == "25.07.2024"

def test_deadline_test_add(task_deadline1, task_deadline2):
    assert task_deadline1 + task_deadline2 == 120


def test_deadline_test_add_error(task_deadline1, task_deadline2):
    with pytest.raises(TypeError):
        result = task_deadline1 + 1
