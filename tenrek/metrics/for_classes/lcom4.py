from clang.cindex import CursorKind
from .lcom_help_functions import (
    collect_methods,
    collect_fields,
    method_key
)


def calculate(class_cursor):
    """
    LCOM4 (Hitz & Montazeri)

    Definition:
    Number of connected components in graph:
      node  = method
      edge  = methods share at least one field
              OR one method calls another

    Good cohesion:
      1 = cohesive class

    Poor cohesion:
      >1 = class should probably be split
    """

    methods = collect_methods(class_cursor)

    if not methods:
        return 0

    if len(methods) == 1:
        return 1

    class_fields = collect_fields(class_cursor)

    method_keys = [method_key(m) for m in methods]

    field_usage = {}
    calls = {}

    for method in methods:
        key = method_key(method)
        field_usage[key] = collect_used_fields(method, class_fields)
        calls[key] = collect_called_methods(method, method_keys)

    graph = {k: set() for k in method_keys}

    for i in range(len(method_keys)):
        for j in range(i + 1, len(method_keys)):
            m1 = method_keys[i]
            m2 = method_keys[j]

            connected = False

            if field_usage[m1] & field_usage[m2]:
                connected = True

            elif m2 in calls[m1] or m1 in calls[m2]:
                connected = True

            if connected:
                graph[m1].add(m2)
                graph[m2].add(m1)

    return count_components(graph)


def count_components(graph):
    visited = set()
    components = 0

    for node in graph:
        if node not in visited:
            components += 1
            dfs(node, graph, visited)

    return components


def dfs(node, graph, visited):
    stack = [node]

    while stack:
        cur = stack.pop()

        if cur in visited:
            continue

        visited.add(cur)

        for nxt in graph[cur]:
            if nxt not in visited:
                stack.append(nxt)



def collect_used_fields(method_cursor, class_fields):
    used = set()

    def walk(node):
        if node.kind in {
            CursorKind.MEMBER_REF_EXPR,
            CursorKind.DECL_REF_EXPR,
            CursorKind.UNEXPOSED_EXPR,
        }:
            if node.spelling in class_fields:
                used.add(node.spelling)

        for c in node.get_children():
            walk(c)

    walk(method_cursor)
    return used


def collect_called_methods(method_cursor, method_keys):
    names = {extract_name(k) for k in method_keys}
    called = set()

    def walk(node):
        if node.kind == CursorKind.CALL_EXPR:
            name = node.spelling

            if name in names:
                for mk in method_keys:
                    if extract_name(mk) == name:
                        called.add(mk)

        for c in node.get_children():
            walk(c)

    walk(method_cursor)
    return called


def extract_name(method_key_value):
    if "::" in method_key_value:
        return method_key_value.split("::")[-1]

    if ":" in method_key_value:
        return method_key_value.split(":")[0]

    return method_key_value