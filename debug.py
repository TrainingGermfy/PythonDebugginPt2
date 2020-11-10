def max_subarray(sequence):
    max_ending_here = max_so_far = 0
    for x in sequence:

        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        import pdb; pdb.set_trace()

    return max_so_far
