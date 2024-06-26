import pytest


def test_user_init(first_user, second_user):
    assert first_user.username == "User"
    assert first_user.email == "user@mail.ru"
    assert len(first_user.task_in_list) == 2

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_tasks_cound == 5
    assert second_user.all_tasks_cound == 5


def test_user_task_list_property(first_user):
    assert first_user.task_list == ("Купить огурцы, Статус выполнения: Ожидание старта, Дата создания: 12.06.2024\n"
                                    "Купить помидоры, Статус выполнения: Ожидание старта, Дата создания: 12.06.2024\n")


def test_user_task_list_setter(first_user, task):
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task
    assert len(first_user.task_in_list) == 3


def test_user_str(first_user):
    assert str(first_user) == "Userov User, user@mail.ru, Всего задач в списке: 156"


def test_task_iterator(task_iterator):
    iter(task_iterator)
    assert task_iterator.index == 0
    assert next(task_iterator).name == "Купить огурцы"
    assert next(task_iterator).name == "Купить помидоры"
    assert next(task_iterator).name == "Купить лук"

    with pytest.raises(StopIteration):
        next(task_iterator)


def test_user_task_list_setter_error(first_user, task):
    with pytest.raises(TypeError):
        first_user.task_list = 1

def test_user_task_list_setter_periodic_task(first_user, task_periodic1):

    first_user.task_list = task_periodic1
    assert first_user.task_in_list[-1].name == "Купить огурцы"