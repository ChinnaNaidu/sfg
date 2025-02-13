import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text nod", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, Bold, None)")
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, Bold, https://www.example.com)")


if __name__ == "__main__":
    unittest.main()