from clang.cindex import TokenKind

OPERATORS = {
    "+", "-", "*", "/", "%", "++", "--",
    "==", "!=", ">", "<", ">=", "<=",
    "&&", "||", "!", "&", "|", "^", "~",
    "<<", ">>",
    "=", "+=", "-=", "*=", "/=", "%=",
    "&=", "|=", "^=", "<<=", ">>=",
    "?", ":", "->", ".", "::",
    "(", ")", "[", "]", "{", "}",  
    ";", ",",                      
    "const", "static",             
    "[]", "()"                     
    "new", "delete", "throw",
    "if", "else", "for", "while", "do",
    "switch", "case",
    "return", "break", "continue", "goto", "default"
}


def get_operators(node):
    operators = []

    for t in node.get_tokens():
        if t.kind == TokenKind.KEYWORD or t.kind == TokenKind.PUNCTUATION:
            if t.spelling in OPERATORS:
                operators.append(t.spelling)

    return operators

# большой вопрос: что делать со скобочками???
# ( -> '()'    not '(',')'