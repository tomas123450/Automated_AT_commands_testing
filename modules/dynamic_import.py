import importlib

def dynamic_import(module_name, function_name, **kwargs):
    try:
        imported_module = importlib.import_module(module_name)
        imported_function = getattr(imported_module, function_name)
        return imported_function(**kwargs)
    except (ImportError, AttributeError):
        print(f"Could not import module {module_name} or call function {function_name}")
