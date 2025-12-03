def hamming_distance(sequences):
    """
    Reads DNA sequences from a file and calculates the minimum and maximum
    Hamming distances between all sequence pairs.
    Ensures:
    - All sequences are DNA (A,G,T,C)
    - All sequences have the same length

    Parameters:
        sequences (str): File path of FASTA/text file containing sequences.

    Returns:
        tuple: (minimum_hamming_distance, maximum_hamming_distance)
               OR (-1, -1) for invalid input.
    """
    length_1 = []
    length_3 = []
    DNA_base = ["A", "G", "T", "C"]

    with open(sequences, 'rt') as seq:
        seq_data = seq.readlines()
        filtered_list = [x.strip('\n').upper().replace("U", "T") for x in seq_data]
        filtered_list1 = [x.strip('\n').upper().replace("U","T") for x in seq_data]

        for x1 in filtered_list:
            if all(x in DNA_base for x in x1):
                for x in filtered_list:
                    y = str(len(x))
                    length_1.append(y)
                    length_2 = set(length_1)
                if len(length_2) == 1:
                    for x in filtered_list:
                        for y in filtered_list1:
                            if x != y:
                                x2 = list(x)
                                y2 = list(y)
                                count = 0
                                for h, m in zip(x2, y2):
                                    if h != m:
                                        count += 1
                                length_3.append(count)
                                length_3.sort()
                                min_value = length_3[0]
                                max_value = length_3[-1]
                    return (min_value, max_value)
                else:
                    return (-1, -1)
            else:
                return (-1, -1)
