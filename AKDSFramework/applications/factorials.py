def factorials(number: int, iteratively=True):
    """
    Calculates factorials iteratively as well as recusively. Default iteratively. Takes linear time.
        Args:
            - ``number`` (int): Number for which you want to get a factorial.
            - ``iteratively`` (bool): Set this to False you want to perform a recursion factorial calculation. By default calculates iteratively
    """
    if iteratively:
        if not (isinstance(number, int) and number >= 0):
            # Raise non negative number error
            raise ValueError("'number' must be a non-negative integer.")

        result = 1
        if number == 0:
            return 1
        for i in range(2, number+1):
            result *= i

        return result
    
    else:
        # If user want's to perform a recusive factorial calculation
        if not (isinstance(number, int) and number >= 0):
            # Raise non negative number error
            raise ValueError("'number' must be a non-negative integer.")

        if number == 0:
            return 1
        result = number * factorials(number - 1)

        return result


if __name__ == "__main__":
    print(factorials(5, True))