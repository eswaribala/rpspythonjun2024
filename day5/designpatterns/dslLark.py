from lark import Lark
parser = Lark('operator: "<" | ">" | "=" | ">=" | "<=" | "!="', start="operator", keep_all_tokens=True)
parsed = parser.parse(">")
parsed
parsed.children[0].value
