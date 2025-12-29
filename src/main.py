from textnode import TextNode, TextType


def main() -> None:
    test_node = TextNode("sample url text", TextType.LINK, "http://sample.example.com")
    print(test_node)


if __name__ == "__main__":
    main()
