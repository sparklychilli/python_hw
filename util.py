def read_file_into_lines(file_path):
    """
    A simple function to read a file into
    a list of lines, removing the newline
    character at the end.

    Arguments:
    ==========
    file_path: str
        The location of a text file to read.

    Returns:
    ========
    list[str]
        A list that contains all stripped lines
        of the input text file.
    """
    lines = []
    with open(file_path, 'r') as infile:
        for line in infile.readlines():
            cleaned = line.rstrip()
            lines.append(cleaned)
    return lines

def reverse_complement_dna(dna_strand)
#make a reverse complement of an DNA-strand
    revc_dna = ""
        for base in dna_strand: #loop through all positions of the string
        if base == "A": #making an if/elif loop to assign all possible complements that the base could have
            new_base = "T"
        elif base == "T":
            new_base = "A"
        elif base == "G":
            new_base = "C"
        elif base == "C":
            new_base = "G"
        revc = new_base + revc
    return revc_dna
