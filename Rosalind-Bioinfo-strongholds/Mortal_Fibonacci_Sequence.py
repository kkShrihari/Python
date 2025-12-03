class Mortal_Fibonacci_sequence:
    """
    A class to compute the mortal Fibonacci sequence, where rabbits reproduce
    but die after a fixed number of months.
    """
    def __init__(self, x, y):
        """
        Initializes the model.

        Parameters:
        x (int): Total number of months.
        y (int): Lifespan (in months) after which rabbits die.
        """
        self.month = x
        self.death = y
    
    def MFS(self):
        """
        Computes the total number of rabbit pairs alive after 'month' months
        using the mortal Fibonacci recurrence logic.
        """
        MFS_month  = [0] * self.death
        MFS_month[1] = 1
        
        if self.month == 1 or self.month == 2:
            return 1
        
        for i in range(2, self.month):
            copy_MFS = MFS_month.copy()
            print(MFS_month, "hi", i-1)
            for m in range(len(MFS_month)):
                if copy_MFS[m] != 0:
                    if (m != (len(MFS_month)-1)) and (m == 0):
                        MFS_month[1] = copy_MFS[0]
                        MFS_month[0] = 0
                        print(MFS_month, "1", m)

                    if (m != (len(MFS_month)-1)) and (m == 1):
                        MFS_month[2] = copy_MFS[1]
                        MFS_month[1] = 0
                        MFS_month[0] += 1
                        print(MFS_month, "2", m)

                    if (m > 1) and (m != (len(MFS_month)-1)):
                        MFS_month[m+1] = copy_MFS[m]
                        MFS_month[0] += 1
                        print(MFS_month, "3", m)

                    if m == (len(MFS_month)-1):
                        MFS_month[m] = 0
                        MFS_month[0] += 1
                        print(MFS_month, "4", m)

            total = 0
            for no in MFS_month:
                total = total + no  

        return total
