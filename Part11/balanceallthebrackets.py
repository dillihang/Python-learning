import string
def balanced_brackets(my_string: str):
    """
    Determine whether the round '()' and square '[]' brackets in a string 
    are correctly balanced and properly nested. All other characters 
    are ignored. Only entirely nested brackets are considered valid; 
    sequences like '()()' are not balanced.

    Args:
        my_string (str): The input string to check.

    Returns:
        bool: True if brackets are balanced and nested, False otherwise.

    Example:
        balanced_brackets("([([])])")
        True
    """
    if len(my_string) == 0:
        return True

    if any(char in string.ascii_letters or char in string.digits or char in string.whitespace or char == "" for char in my_string):
        brackets_only = "".join([char for char in my_string if char in '()[]'])
        my_string=brackets_only

    if my_string.startswith('('):
        if not (my_string[0] == '(' and my_string[-1] == ')'):
            return False
    elif my_string.startswith('['):
        if not (my_string[0] == '[' and my_string[-1] == ']'):
            return False
    elif my_string.startswith(')'):
        return False 
    elif my_string.startswith(']'):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])


ok = balanced_brackets("([([])])")
print(ok)

ok = balanced_brackets("(python version [3.7]) please use this one!")
print(ok)

# this is no good, the closing bracket doesn't match
ok = balanced_brackets("(()]")
print(ok)

# different types of brackets are mismatched
ok = balanced_brackets("([bad egg)]")
print(ok)