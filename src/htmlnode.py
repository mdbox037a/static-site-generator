class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list | None = None,
        props: dict | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplementedError)

    def props_to_html(self) -> str:
        """Returns a formatted string representing the HTML attributes of node"""
        attributes_string = ""
        if not self.props:
            return ""
        else:
            for key in self.props.keys():
                attributes_string += f' {key}="{self.props[key]}"'
            return attributes_string

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        value: str,
        props: dict | None = None,
    ) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        """If no tag, returns raw text; otherwise returns formatted HTML tag from LeafNode params"""
        if not self.value:
            raise Exception(ValueError)
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict | None = None) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        """Return a string representing the HTML tag of the node and its children"""
        if self.tag is None:
            raise ValueError(
                f"ValueError: Tag must be defined; current tag value: {self.tag}"
            )
        if self.children is None:
            raise ValueError(
                f"ValueError: Child value(s) must be defined; current children value: {self.children}"
            )
        html_tree = ""
        for child in self.children:
            html_tree += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_tree}</{self.tag}>"
