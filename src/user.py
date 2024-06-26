from src.task import Task

class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list
    users_count = 0
    all_tasks_cound = 0

    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        # указываем атрибут класа как приватны __task_lis
        self.__task_list = task_list if task_list else []
        User.users_count += 1
        User.all_tasks_cound += len(task_list) if task_list else 0

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.email}, Всего задач в списке: {len(self.task_list)}"

    @property
    def task_list(self):
        task_str = ''
        for task in self.__task_list:
            task_str += f"{str(task)}\n"
        return task_str

    @task_list.setter
    def task_list(self, task: Task):
        if isinstance(task, Task):
            self.__task_list.append(task)
            User.all_tasks_cound += 1
        else:
            raise TypeError


    @property
    def task_in_list(self):
        return self.__task_list

if __name__ == "__main__":
    task1 = Task("Купить огурцы", "Купить огурцы для салата")
    task2 = Task("Купить лук", "Купить лук для салата")
    task3 = Task("Купить помидоры", "Купить помидоры для салата")
    task4 = Task("Купить перец", "Купить перец для салата")

    user = User('User', 'user@mail.ru', 'User', 'Userov', [task1, task2, task3, task4])

    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)

    print(user.users_count)
    print(User.all_tasks_cound)

    task4 = Task("Купить перец", "Купить перец для салата")
    user.task_list = task4
    print(user.task_list)
    print(User.all_tasks_cound)

    print(user)