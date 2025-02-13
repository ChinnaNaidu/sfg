from textnode import TextNode, TextType

def main():
    text = "Hello, World!"
    text_type = TextType.NORMAL
    url = "https://www.example.com"
    node = TextNode(text, text_type, url)
    print(node)

main()