class Tree_of_life:
    """
    A class to process an undirected graph and count connected components
    based on the provided integer-labeled node relationships.
    """

    def __init__(self, input_data):
        """
        Initializes the object with raw multi-line input data.

        Parameters:
        input_data (str): First line contains number of nodes.
                          Remaining lines contain space-separated pairs
                          representing edges.
        """
        self.input_data = input_data
    
    def TOL(self):
        """
        Computes the number of connected components by grouping nodes
        that appear together in the same edges.

        Returns:
        int: Count of discovered connected components.
        """
        list1 =  list(self.input_data.strip().splitlines())

        list_all = []
        total_int = int(list1[0])
        list1.pop(0)

        list_all = list(range(1, total_int+1))

        final_list = []
        for i in range(len(list1)):
            y = list(map(int, list1[i].split()))
            final_list.append(y)
        print(final_list)

        hidden, x = [], 0
        comp_list = []
        for i in range(total_int):
            for i1 in range(len(final_list)):
                for i2 in range(len(final_list[i1])):
                    if list_all[i] == int(final_list[i1][i2]):
                         print(list_all[i],final_list[i1])
                         hidden = hidden + final_list[i1]
                    if list_all[i] != int(final_list[i1][i2]):
                        x +=1
                if len(hidden) > len(final_list[i1]):
                  comp_list.append(hidden)
                  hidden =  []
        print(comp_list)
        return len(comp_list)
        

input_data = """10
1 2
2 8
4 10
5 9
6 10
7 9"""
TOL1 = Tree_of_life(input_data)
print(TOL1.TOL())
