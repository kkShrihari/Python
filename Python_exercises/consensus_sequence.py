def consensus_sequence(pwm):
    """
    Builds consensus sequence(s) from a PWM.
    If ties occur, returns all possible consensus combinations.

    Parameters:
        pwm (list[list[int]]): A,C,G,T x length PWM

    Returns:
        list[str]: all possible consensus sequences
    """
    tranposed_pwm = [list(row) for row in zip(*pwm)]
    Nucleotide_bases = ["A","C","G","T"]
    value = [0,1,2,3]
    base_value_map = {k:v for k,v in zip(value,Nucleotide_bases)}

    result_index = []
    for element in tranposed_pwm:
        max_val = max(element)
        index = [str(idx) for idx, val in enumerate(element) if val == max_val]
        result_index.append(''.join(index))

    def val_2_list(x1, y1):
        final_list = []
        for x in y1:
            if isinstance(x, str):
                mapping = [x1[int(char)] for char in x]
                if len(mapping) == 1:
                    final_list.append(mapping[0])
                else:
                    final_list.append(mapping)
            else:
                final_list.append(x)
        return final_list  

    x1 = base_value_map
    y1 = result_index
    list_1 = val_2_list(x1, y1)[0]
    list_2 = val_2_list(x1, y1)[1:]

    final_result = []
    for x in list_1:
        string_1 = x + ''.join(list_2)
        final_result.append(string_1)
    return final_result
