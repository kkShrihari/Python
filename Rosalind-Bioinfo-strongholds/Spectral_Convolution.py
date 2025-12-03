class Spectral_Convolution:
    """
    A class to compute the spectral convolution between two lists of masses.
    """

    def __init__(self, data):
        """
        Initializes with two space-separated lines of masses.

        Parameters:
        data (str): Two lines of floating point mass values.
        """
        print("\n")
        self.input_data = data

    def spectral(self):
        """
        Computes all pairwise differences between the masses in the first list
        and the masses in the second list.

        Returns:
        tuple: (most frequent mass difference, its count)
        """
        final_list = []
        pre_list1 = list(self.input_data.strip(" ").splitlines())
        for i in range(len(pre_list1)):
            pre_list2 = list(pre_list1[i].split())
            final_list.append(pre_list2)

        list1 = []
        for i2 in range(len(final_list[1])):
            for i1 in range(len(final_list[0])):
                diff = float(final_list[0][i1]) - float(final_list[1][i2])
                list1.append(round(diff,5))

        number_set = set(list1)

        count_list_ = []
        number_list_ = list(number_set)
        for i in range(len(number_set)):
            c = list1.count(number_list_[i])
            count_list_.append(c)

        final_dict = dict(zip(number_list_, count_list_))
        maxi = max(final_dict, key=final_dict.get)
        value = final_dict[maxi]
        return maxi, value
       
input_data = """186.07931 287.12699 548.20532 580.18077 681.22845 706.27446 782.27613 968.35544 968.35544
101.04768 158.06914 202.09536 318.09979 419.14747 463.17369"""
SC1 = Spectral_Convolution(input_data)
print(SC1.spectral())
