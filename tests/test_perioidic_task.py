import pytest


def test_periodic_task_init(task_periodic1):
    assert task_periodic1.name == "Купить огурцы"
    assert task_periodic1.description == "Купить огурцы для салата"
    assert task_periodic1.start_date == "01.07.2024"
    assert task_periodic1.created_at == "20.06.2024"
    assert task_periodic1.status == 'Ожидание старта'
    assert task_periodic1.end_date == "01.08.2024"
    assert task_periodic1.frequency == "Ежедневно"

def test_periodic_task_add(task_periodic1, task_periodic2):
    assert task_periodic1 + task_periodic2 == 120


def test_periodic_task_add_error(task_periodic1, task_periodic2):
    with pytest.raises(TypeError):
        result = task_periodic1 + 1