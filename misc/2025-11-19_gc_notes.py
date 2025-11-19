'''
Rosalind GC Count

Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''

'''
GC-content: 
#G+#C/len(s) --> will be used a lot, write a function

def gc_content(seq)
    "Calculate the GC content of a sequence (0-100)."
    total_C = seq.count ('C')
    total_G = seq.count ('G')
    percent_gc = (total_C + total_G) / len(seq) * 100
    return percent_gc

'''

'''
sequences have unique ID --> Dictionary is good way to deal with that
-->manually

'''
'''
for seq_id in sequences:
    seq = sequences[seq_id]
    gc = gc_content(seq)

for seq_id, seq in sequences.items():
    gc = gc_content(seq)
    print(f"sequence{seq_id} has a GC content of {gc}.")


''''

'''
find max GC content:
-->max function, but works for highest value only
we want seq_id AND value....

instead go through list of sequences and ask if current value is highest --> if yes overwrite highest gc value +seq-id with new values

make a starter value that is definitely smaller than all we would get

maximum_gc = -1
maximum_gc_id = ''

for seq_id, seq in sequences.items():
    gc = gc_content(seq) #is this the highest GC-content we have seen
    if gc > maximum_gc: #then overwrite the maximum_gc and maximum_gc_id
        maximum_gc = gc
        maximum_gc_id = seq_id

print (maximum_gc_id)
print (maximum_gc)
'''
'''
Reading in function
from util import read_file_into_lines

fasta = read_file_into ('./rosalind_gc_blabla.txt')

the sequences and id are 3 lines each - but we cannot rely on them not being longer
each id is prequelled by >

does line start with ">"?
yes --> we have a new sequence; id is everything but first character(>) --> id=line[1:]
no --> still the sequence, append to previous one

current_sequence = ''
current_id = ''
sequences = {}

for line in fasta: 
    #if line.startswith(">"):
    if line[0] == '>': #if the line starts with a > (if it is the id line)
        sequences [current_id] = current_sequence
        current_sequence = '' #since we always append to the current sequence, we have to clear it when we reach a new id
        line[1:] = current_sequence_id
    else: #if the line contains sequencce
        current_sequence += line    #append to current sequence

del sequences[''] #removing the empty strings we added in first iteration
sequences [current_id] = current_sequence #for the last iteration of the loop (because we always fo that when the next line comes up)

--> it would be smart to make this a function (in our util)


def parse_fasta(lines_list):
    

'''

#plug-ins for visual studio code
#can I create a notebook in code
#why does code show me my drafs/deleted notebooks --> because of notebook back-ups? 
#where are daylies and scripts --> https://ue300160.github.io/code : dailies
#how long do functions exist after I called them? For whole session? As long as working memory lasts?
