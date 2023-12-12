def confirm_prompt(message="Please confirm"):
    """
    This is a Decorator
    Prompts a user to confirm running decorated function.

    Parameters:
        message (str): a prompt message

    Returns:
        handler (function): hendler of decorated function
    """

    def handler(func):
        def inner(*args, **kwargs):
            user_input = input(f"{message} (y/no) ")
            user_input = user_input.strip().lower()

            if user_input in ["yes", "y"]:
                return func(*args, **kwargs)

        return inner

    return handler


__all__ = ["confirm_prompt"]
