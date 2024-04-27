import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("text_eq executed")
        node = TextNode("This is a text node", "bold", "random url")
        node2 = TextNode("This is a text node", "bold", "random url")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    print("main executed")
    unittest.main()