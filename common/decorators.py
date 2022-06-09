from dataclasses import fields

def custom_dataclass(dataclass):
    def decorator(*args, **kwargs):
        def wrapper_func(*args, **kwargs):
            field_names = set(field.name for field in fields(dataclass))
            return dataclass(**{key: kwargs[key] for key in field_names if key in kwargs})
        return wrapper_func
    return decorator(dataclass)

