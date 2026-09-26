# Constructing a De Bruijn Graph


# Helpers and references
CompDict = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

#Preprocessing the input data
raw_input = """TGAT
CATG
TCAT
ATGC
CATC
CATC
"""
input = raw_input.splitlines()#replace("\"","").rsplit("\n")
length = len(input[0])
k = length - 1
print(length , k )

# Splitting function
def Split(input_list: list[str]) -> list[tuple[str, str]]:
    """
    Construct de Bruijn graph edges from DNA reads and their reverse complements.

    Args:
        input_list: List of DNA strings of equal length.

    Returns:
        A sorted list of unique (prefix, suffix) tuples representing graph edges.
    """
    split_list = []
    for reads in input_list:
        front = reads[:-1]
        back = reads[1:]
        split_list.append((front, back))
        rev = reads[::-1]
        rc = ""
        for i in rev:
            rc += CompDict[i]
        rc_front = rc[:-1]
        rc_back = rc[1:]
        split_list.append((rc_front, rc_back))
        
    split_list = sorted(set(split_list))
    return split_list

print(Split(input))

