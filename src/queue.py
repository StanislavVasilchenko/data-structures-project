class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.queue = list()
        self.head = None
        self.tail = None
        self.str_data = ""

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if len(self.queue) == 0:
            new_obj = Node(data, self.tail)
            self.queue.append(new_obj)
            self.head = new_obj
            self.str_data += data
        else:
            new_obj = Node(data)
            self.queue[-1].next_node = new_obj
            self.head = self.queue[0]
            self.queue.append(new_obj)
            self.tail = self.queue[-1]
            self.str_data += f"\n{data}"

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return f"{self.str_data}"
