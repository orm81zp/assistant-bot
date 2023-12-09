def confirm_prompt(message="Please confirm"):
    """The decorator calls the function after confirming the user"""
    def handler(func):
        def inner(*args, **kwargs):
            user_input = input(f"{message} (yes/no) ")
            user_input = user_input.strip().lower()

            if user_input in ["yes", "y"]:
                return func(*args, **kwargs)
        return inner
    return handler

__all__ = ["confirm_prompt"]
