from collections import deque

def is_palindrome(string: str) -> bool:
    if not isinstance(string, str):
        raise ValueError("Input should be of type str")
    d = deque(string.lower())  
    while len(d) > 1:  
        if d.pop() != d.popleft():  
            return False  
    return True
    

is_palindrome("abb")