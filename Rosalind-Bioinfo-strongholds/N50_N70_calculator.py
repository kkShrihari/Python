class N5_N7:
    """
    A class to compute the N50 and N75 statistics commonly used in genome assembly.
    """

    print("\n")

    def __init__(self, input):
        """
        Parameters:
        input (str): Multi-line string where each line represents a contig sequence.
        """
        self.input = input

    def n5n7(self):
        """
        Computes:
        - N50: contig length where cumulative length ≥ 50% of total
        - N75: contig length where cumulative length ≥ 75% of total

        Prints:
        A string: "<N50> <N75>"
        """
        list1 = list(self.input.strip().splitlines()) 
        list1 = [len(i) for i in list1]
        list1.sort(reverse=True)
        total_sum = sum(list1)

        list2 = []
        for i in range(len(list1)):
            if i == 0:
                list2.append(list1[i])
            else:
                sum1 = list1[i] + list2[i-1]
                list2.append(sum1)

        list3 = [(i / total_sum) * 100 for i in list2]
        dict1 = dict(zip(list3, list1))

        for i1 in list3:
            if i1 >= 50:
                answer = str(dict1[i1])
                break
        for i2 in list3:
            if i2 >= 75:
                answer += " " + str(dict1[i2])
                break 
        print(answer)


input ='''
GATTACA
TACTACTAC
ATTGAT
GAAGA
'''
N5_N71 = N5_N7(input)
N5_N71.n5n7()
