#I am using tail optimized recursion to ensure conservation of performance when compiled (will result as the same as a while loop)

def compute_sum(number : int, current_sum : int) -> int:
    """
    A tail optimized recursive function that adds up the digits of a number.

    Args:
        number (int): The number to be summed
        current_sum (int): The current sum of the digits

    Returns:
        int: The total sum of the number
    """
    if number//10 == 0: return current_sum + number
    current_sum += number %10; number //= 10; return compute_sum(number, current_sum)
def digit_sum(n : int) -> int: return compute_sum(n, 0)
def digital_root(n : int) -> int:
    """
    A tail optimized recursive function that finds the digital root of a number.
    
    The digital root is the single digit number which resulted from repeatedly
    summing the digits of a number until only one digit remains.
    
    Args:
        n (int): The number to find the digital root of
    
    Returns:
        int: The digital root of n
    """
    if n//10 == 0: return n
    n = digit_sum(n); return digital_root(n)
    
# print(digit_sum(69701))
# print(digital_root(1969))