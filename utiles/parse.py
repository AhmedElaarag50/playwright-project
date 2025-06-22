from selectolax.parser import Node, HTMLParser
from typing import Union

def parse_raw_attributes(node:Union[Node, str], selectors:list[dict]) -> dict:
    if not issubclass(Node, type(node)):
        node = HTMLParser(node)
    parsed ={}
    for s in selectors:
        name = s.get("name")
        selector = s.get("selector")
        match = s.get("match")
        type_ = s.get("type")
        if match == "all":
            process = node.css(selector)
            if type_ == "text":
                parsed[name] = [node.text() for node in process]
            elif type_ == "node":
                parsed[name] = process
        elif match == "first":
            process = node.css_first(selector)
            if type_ == "text":
                parsed[name] = process.text()
            elif type_ == "node":
                parsed[name] = process
    return parsed