class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None
        self.stack = list()
        self.stack_data = ""
    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if len(self.stack) == 0:
            self.stack.append(Node(data, None))
            self.stack_data += data
        else:
            self.stack.append(Node(data, self.top))
            self.stack_data += f"\n{data}"
        self.top = self.stack[-1]

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        data_remote = self.stack.pop()
        if len(self.stack) == 0:
            self.top = None
        else:
            self.top = self.stack[-1]

        return data_remote.data

    def __str__(self):
        return f"{self.stack_data}"
