import inspect
import reprlib


def dump(obj):
    print("Type")
    print("======")
    print(type(obj))
    print()

    print("Documentation")
    print("==============")
    print(obj.__doc__)
    print(inspect.getdoc(obj))
    print()

    all_attr_names = set(dir(obj))
    methods_names = set(
        filter(lambda attr_name: callable(getattr(obj, attr_name)), all_attr_names)
    )
    assert methods_names <= all_attr_names
    attr_names = all_attr_names - methods_names

    print("Attributes")
    print("===========")
    attr_names_and_values = [(name, reprlib.repr(getattr(obj, name))) for name in attr_names]
    print_table(attr_names_and_values, "Name", "Value")
    print()

    print("Methods")
    print("========")
    methods = (getattr(obj, method_name) for method_name in methods_names)
    methods_names_and_doc = sorted((full_sig(method), brief_doc(method)) for method in methods)
    print_table(methods_names_and_doc, "Name", "Description")
    print()


def full_sig(method):
    try:
        return method.__name__ + str(inspect.signature(method))
    except ValueError:
        return method.__name__ + "(...)"


def brief_doc(obj):
    doc = obj.__doc__
    if doc is not None:
        lines = doc.splitlines()
        if len(lines) > 0:
            return lines[0]
    return ''


def print_table(rows_of_columns, *headers):
    for row in rows_of_columns:
        print(row)