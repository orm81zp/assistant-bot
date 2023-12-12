def is_yes_prompt(msg="Please confirm"):
    user_input = input(f"{msg} (y/no) ")
    user_input = user_input.strip().lower()

    return user_input in ["yes", "y"]


__all__ = ["is_yes_prompt"]
