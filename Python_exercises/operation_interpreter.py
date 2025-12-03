def solve(n, operations):
    """
    Evaluates a list of mathematical operations applied in sequence.

    Supported operations:
        mod X  → n = n % X
        add X  → n = n + X
        mul X  → n = n * X
        div X  → n = n / X

    Parameters:
        n (int/float): starting value
        operations (str): space-separated operations and operands

    Returns:
        number: final computed value
    """
    Final_value = n
    operation_list = operations.split()

    for val in range(0, len(operation_list), 2):
        calculation = operation_list[val]
        cal_value = operation_list[val+1]

        match calculation:
            case "mod":
                Final_value %= int(cal_value)
            case "add":
                Final_value += int(cal_value)
            case "mul":
                Final_value *= int(cal_value)
            case "div":
                Final_value /= int(cal_value)
            case _:
                raise ValueError("Unknown operation")

    return Final_value
