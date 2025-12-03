def common_kmers(fasta, k):
    """
    Reads a FASTA file and extracts all overlapping k-mers from each sequence.
    Returns the set of k-mers common to ALL sequences.

    Parameters:
        fasta (str): FASTA file path
        k (int): k-mer length

    Returns:
        set: Set of shared k-mers across all sequences
    """
    join_list = []
    unique = ''

    with open(fasta, 'r') as seq:
        seq_data = seq.readlines()
        for x in seq_data:
            if x.startswith('>'):
                if unique:
                    join_list.append(unique)
                    unique = ''
            else:
                unique += x
        if unique:
            join_list.append(unique)

    fasta_list = [y.replace("\n", "") for y in join_list]

    NO_list = []
    for seq in fasta_list:
        KMER = 0
        final_set = set()
        A = 0
        B = k
        None_list = []
        while KMER < k:
            for z in seq:
                imp_list = list(seq[A:B])
                A += 1
                B += 1
                if imp_list != None_list:
                    if len(imp_list) == k:
                        result = set(["".join(map(str,imp_list))])
                final_set.update(result)
                KMER += 1
        NO_list.append(final_set)

    common_kmers1 = set.intersection(*NO_list)
    return common_kmers1
