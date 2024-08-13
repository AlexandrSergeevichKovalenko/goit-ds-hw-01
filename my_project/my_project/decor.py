def input_error(expected_arg_count=None):
    error_messages = {
        "ValueError": "Please provide a valid name and phone number.",
        "TypeError": "Invalid input type",
        "IndexError": "You did not provide enough arguments.",
        "InvalidName": "Invalid format for name. Please use alphabetic characters only.",
        "InvalidPhone": "Invalid format for phone. Please use numeric characters only."
    }

    def decorator(func):
        def inner(*args, **kwargs):
            try:
                # checking arguments availability
                if not args or not args[0]:
                    raise IndexError(error_messages["IndexError"])
                # checking numbers og arguments
                if expected_arg_count is not None and len(args[0]) != expected_arg_count:
                    raise ValueError(error_messages["ValueError"])
                # checking additionaly some spesific functions
                if func.__name__ in ["add_contact", "change_contact"]:
                    if not args[0][0].isalpha():
                        raise ValueError(error_messages["InvalidName"])
                    if not args[0][1].isdigit():
                        raise ValueError(error_messages["InvalidPhone"])
                return func(*args, **kwargs)
            except Exception as e:
                return str(e)
        return inner
    return decorator
