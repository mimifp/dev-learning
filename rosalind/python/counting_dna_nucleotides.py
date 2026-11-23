# Test in file C:/Users/miria/Documents/programacion/rosalind/counting_dna_nucleotides.txt

dna_file = str(input("DNA string file path:"))

with open(dna_file, "r") as f:
    dna = f.read()

def count_nucleotides(dna: str):
    a_count = c_count = g_count = t_count = 0

    for letter in dna:
        if letter.upper() == 'A':
            a_count +=1
        elif letter.upper() == 'C':
            c_count += 1
        elif letter.upper() == 'G':
            g_count += 1
        elif letter.upper() == 'T':
            t_count += 1
    
    return a_count, c_count, g_count, t_count

if __name__ == "__main__":
    print(count_nucleotides(dna))
