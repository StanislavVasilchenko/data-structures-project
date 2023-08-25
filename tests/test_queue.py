"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue, Node


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        self.test_enqueue = Queue()
        self.test_enqueue.enqueue(data="data1")
        self.test_enqueue.enqueue(data="data2")
        self.test_enqueue.enqueue(data="data3")

        self.assertEqual(self.test_enqueue.head.data, "data1")
        self.assertEqual(self.test_enqueue.head.next_node.data, "data2")
        self.assertEqual(self.test_enqueue.tail.next_node, None)

    def test_str(self):
        self.test_enqueue = Queue()
        self.assertEqual(str(self.test_enqueue), "")
        self.test_enqueue.enqueue(data="data1")
        self.test_enqueue.enqueue(data="data2")
        self.test_enqueue.enqueue(data="data3")

        self.assertEqual(str(self.test_enqueue), "data1\ndata2\ndata3")
