# Code Listing #2

"""

Maximum subarray problem - version #2

"""

def max_subarray(sequence=[-5, 20, -10, 30, 15]):
    """ Find sub-sequence in sequence having maximum sum """

    sums = {}
    indices = []

    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            sub_seq = sequence[i:j+1]
            sub_seq_sum = sum(sub_seq)
            #print(sub_seq,'=>',sub_seq_sum)
            sums[sum(sub_seq)]=[i,j+1]

    i_indice = sums[max(sums)][0]
    j_indice = sums[max(sums)][1]
    return (max(sums), sequence[i_indice:j_indice])


print(max_subarray([-5, 20, -10, 30, 15, -15, -55]))