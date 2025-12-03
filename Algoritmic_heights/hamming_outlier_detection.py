def Hamming_Outlier_Detection(data):
    """
    Computes total Hamming distance of each sequence to all others.

    Parameters:
        data (str): FASTA-like multiline string.

    Returns:
        list[int]: Sum of Hamming distances for each sequence.
    """
    data = [line for line in data.splitlines() if line.strip() != ""]
    
    list1, list2 = [], []
    for i in range(len(data)):
        if i % 2 != 0:
            list1.append(data[i])
        else:
            list2.append(data[i][1:])
    dict1 = dict(zip(list2, list1))

    final_list = []
    for x in dict1:
        total = 0
        for y in dict1:
            if x != y:
                count = 0
                for i in range(len(list1[0])):
                    if dict1[x][i] != dict1[y][i]:
                        count += 1
                total += count
        final_list.append(total)
    return final_list
