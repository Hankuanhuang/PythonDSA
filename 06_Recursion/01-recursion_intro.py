# what is Recursion
    # This a function that calling itself

# Two Main parts
    # 1. Base Case
    # 2. Recursive Case

def countdown(n):
    if n == 0:
        return

    print(n) 
    countdown(n-1)

countdown(4)