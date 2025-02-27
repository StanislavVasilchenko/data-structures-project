"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack, Node


class TestStack(unittest.TestCase):
    stack_test = Stack()

    def test_stack_push(self):
        self.stack_test = Stack()
        self.stack_test.push("data")
        self.assertEqual(self.stack_test.stack[0].data, "data")
        self.assertEqual(self.stack_test.stack[0].next_node, None)

        self.stack_test.push("data2")
        self.assertEqual(self.stack_test.stack[1].data, "data2")
        self.assertEqual(self.stack_test.stack[1].next_node, self.stack_test.stack[0])

        self.stack_test.push("data3")
        self.assertEqual(self.stack_test.stack[2].data, "data3")
        self.assertEqual(self.stack_test.stack[2].next_node, self.stack_test.stack[1])

    def test_stack_pop(self):
        self.stack_test = Stack()
        self.stack_test.push("data")
        self.assertEqual(self.stack_test.pop(), "data")
        self.assertEqual(self.stack_test.top, None)

        self.stack_test.push("data")
        self.stack_test.push("data1")
        self.stack_test.pop()
        self.assertEqual(self.stack_test.top, self.stack_test.stack[-1])

        self.stack_test.pop()
        self.assertEqual(self.stack_test.top, None)

    def test_str(self):
        self.stack_test = Stack()
        self.assertEqual(str(self.stack_test), "")
        self.stack_test.push("data")
        self.stack_test.push("data2")
        self.stack_test.push("data3")
        self.assertEqual(str(self.stack_test), "data\ndata2\ndata3")







