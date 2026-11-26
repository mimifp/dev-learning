input_file = str("./computing_gc_content.txt")

with open(input_file, "r", encoding="utf-8") as f:
    data = f.read().splitlines()

all_sequences = []

for i in range(len(data)):
    if data[i][0] == '>':
        seq = [data[i]]
        all_sequences.append(seq)
    else:
        seq.append(data[i])    

formatted_strings = []

for i in range(len(all_sequences)):
    string = ""
    for j in range(1, len(all_sequences[i])):
        string_id = all_sequences[i][0]
        string += all_sequences[i][j]
    formatted_strings.append([string_id, string])

result = []

for i in range(0, len(formatted_strings)):
    nucleotides = len(formatted_strings[i][1])
    rosalind_id = formatted_strings[i][0][1:]
    c_count = formatted_strings[i][1].count('C')
    g_count = formatted_strings[i][1]. count('G')
    gc_value = round((((c_count + g_count) / nucleotides) * 100), 6)

    result.append([gc_value, rosalind_id])


print(max(result)[1])
print("%6f" % max(result)[0])
