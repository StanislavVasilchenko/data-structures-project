"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack, Node


class TestStack(unittest.TestCase):
    # stack_test = Stack()

    def test_stack(self):
        self.stack_test = Stack()
        self.stack_test.push("data")
        self.assertTrue(len(self.stack_test.stack) == 1)
        self.assertEqual(self.stack_test.stack[0].data, "data")
        self.assertEqual(self.stack_test.stack[0].next_node, None)
        self.stack_test.push("data2")
        self.assertTrue(len(self.stack_test.stack) == 2)
        self.assertEqual(self.stack_test.stack[1].data, "data2")
        self.assertEqual(self.stack_test.stack[1].next_node, self.stack_test.stack[0])
        self.stack_test.push("data3")
        self.assertTrue(len(self.stack_test.stack) == 3)
        self.assertEqual(self.stack_test.stack[2].data, "data3")
        self.assertEqual(self.stack_test.stack[2].next_node, self.stack_test.stack[1])

