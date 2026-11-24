# Tested in file counting_dna_nucleotides.txt
def read_file(input_file: str):
    with open(input_file, "r") as f:
        dna = f.read() 
        return dna

def count_nucleotides(dna: str):
    a_count = c_count = g_count = t_count = 0

    for letter in dna:
        if letter.upper() == "A":
            a_count +=1
        elif letter.upper() == "C":
            c_count += 1
        elif letter.upper() == "G":
            g_count += 1
        elif letter.upper() == "T":
            t_count += 1

    count_list = [a_count, c_count, g_count, t_count]

    return count_list


def write_results(count_list: list):
    with open("./solution.txt", "w", encoding="utf-8") as r:
        print(count_list[0], count_list[1], count_list[2], count_list[3], sep=",", file = r)


if __name__ == "__main__":
    input_file = "./counting_dna_nucleotides.txt" 
    dna = read_file(input_file)
    counting = count_nucleotides(dna)
    write_results(counting)

