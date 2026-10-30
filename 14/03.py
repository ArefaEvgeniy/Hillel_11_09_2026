def validate_input(value):
    if value < 0:
        raise ValueError("Hello World: Value must be non-negative")


validate_input(-1)  # This will raise a ValueError
