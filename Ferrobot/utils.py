





# This module contains helper functions for common tasks.
# For example, it includes a function to print text with a typewriter effect,
# which can be used to enhance the user interface when displaying responses.





# utils.py
import textwrap
import time

def response_printer(text):
    """
    Prints the given text to the console with a typewriter effect.
    
    """
    wrapper = textwrap.TextWrapper(width=70)
    paragraphs = text.split('\n')
    wrapped_text = "\n".join([wrapper.fill(p) for p in paragraphs])
    for char in wrapped_text:
        time.sleep(0.06)
        print(char, end="", flush=True)
    print()
