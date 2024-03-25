"""
This is a decorator that is used to add it's argument to the func result.
"""

def tags(html_tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{html_tag}>{func(*args, **kwargs)}</{html_tag}>"

        return wrapper
    return decorator



@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
