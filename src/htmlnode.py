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
