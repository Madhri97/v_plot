import sys
from collections import defaultdict


offset_range = range(-500, 501)

data = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    lines = line.strip().split()
    start = int(lines[2])
    end = int(lines[3])
    
    pos1 = int(lines[8])
    pos2 = int(lines[9])
    
    frag_length = int(lines[11])
    midpoint1 = (start + end) // 2
    midpoint2 = (pos1 + pos2) // 2
    
    rel_pos = midpoint2 - midpoint1
    
    if -500 <= rel_pos <= 500:
        data[frag_length][rel_pos] += 1

relative_positions = []
fragment_lengths = []
counts = []

for frag_length, rel_pos_dict in data.items():
    for rel_pos, count in rel_pos_dict.items():
        relative_positions.append(rel_pos)
        fragment_lengths.append(frag_length)
        counts.append(count)


with open("vplot_data.tsv", "w") as f:
    f.write("Relative_Position\tFragment_Length\tCount\n")  # Header
    for i in range(len(relative_positions)):
        f.write("{}\t{}\t{}\n".format(relative_positions[i], fragment_lengths[i], counts[i]))

