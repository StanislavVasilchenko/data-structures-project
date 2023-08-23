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

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if len(self.stack) == 0:
            self.stack.append(Node(data, None))
        else:
            self.stack.append(Node(data, self.top))
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
