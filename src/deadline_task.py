from src.task import Task

class DeadlineTask(Task):
    def __init__(self, name, description, deadline, status='Ожидание старта', created_at=None, run_time=0):
        super().__init__(name, description, status, created_at, run_time)
        self.deadline = deadline

    def __add__(self, other):
        if type(other) is DeadlineTask:
            return self.run_time + other.run_time
        raise TypeError

if __name__ == "__main__":
    deadline_task = DeadlineTask("Купить огурцы", "Купить огурцы для салата", "25.07.2024", run_time=60)
    print(deadline_task.name)
    print(deadline_task.description)
    print(deadline_task.status)
    print(deadline_task.created_at)
    print()
    print(deadline_task.deadline)

    deadline_task2 = DeadlineTask("Купить огурцы", "Купить огурцы для салата", "25.07.2024", run_time=60)

    deadline_task2 + deadline_task