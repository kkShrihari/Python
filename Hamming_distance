def HammingDistance (sequence1,sequence2):
  """
    Calculate the Hamming distance between two strings.

    The Hamming distance is defined as the number of positions
    at which the corresponding characters in the two strings are different.

    Args:
        sequence1 (str): The first string to compare.
        sequence2 (str): The second string to compare.

    Returns:
        int: The Hamming dsitance between the two strings.

    Raises:
        ValueError: If the strings are not of the same length.
  """
      
  if len(sequence1) != len(sequence2):
      print("unequal string lengths")
  if len(sequence1) > 1000 :
      print("1 or more input sequences above 1kbp ")

  count,index = 0,0
  for nucleotide in sequence1:
    if nucleotide != sequence2[index]:
        count +=1
        index +=1
    elif nucleotide == sequence2[index]:
        index +=1   
  return count


str1 = "GAGCCTACTAACGGGAT"
str2 = "CATCGTAATGACGGCCT"
result = HammingDistance(str1,str2)
print(f"The Hamming distance between the two sequences is {result}")
