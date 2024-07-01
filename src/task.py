import  datetime
from src.base_task import BaseTask

class Task(BaseTask):
    name: str
    description: str
    status: str
    created_at: str
    run_time: int

    def __init__(self, name, description, status='Ожидание старта', created_at=None, run_time=0):
        self.name = name
        self.description = description
        self.status = status
        # Делаем  created_at  приватным __created_at
        self.__created_at = created_at if created_at else datetime.date.today().strftime('%d.%m.%Y')
        self.run_time = run_time

    def __str__(self):
        return f"{self.name}, Статус выполнения: {self.status}, Дата создания: {self.created_at}"

    def __add__(self, other):
        if type(other) is Task:
            return self.run_time + other.run_time
        raise TypeError



    @classmethod
    def new_task(cls, name, description, status='Ожидание старта', created_at=None):
        return cls(name, description, status, created_at)

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, new_date: str):
        if datetime.datetime.strptime(new_date,    '%d.%m.%Y').date() < datetime.datetime.now().date():
            print('Нельзя изменять дату создания на дату из прошлого')
            return
        self.__created_at = new_date


if __name__ == "__main__":
    task = Task("Купить огурцы", "Купить огурцы для салата", run_time=60)

    print(task.name)
    print(task.description)
    print(task.status)
    print(task.created_at)

    task2 = Task.new_task("Купить перец", "Купить перец для салата")
    print(task2.name)
    print(task2.description)
    print(task2.status)
    print(task2.created_at)

    task2.created_at = "29.01.2024"
    print(task2.created_at)
    print(task + task2)

    # task + 1