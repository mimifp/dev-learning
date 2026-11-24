def read_file(input_file: str):
    with open(input_file, "r") as f:
        string = f.read()
        return string

def obtain_complementary(string: str):
    complementary = ""
    for nucleotide in string[::-1]:
        if nucleotide == "A":
            complementary += "T"
        elif nucleotide == "C":
            complementary += "G"
        elif nucleotide == "T":
            complementary += "A"
        elif nucleotide == "G":
            complementary += "C"

    return complementary


def write_file(complementary: str):
    with open("./solution.txt", "w", encoding = "utf-8") as r:
        r.write(complementary)

if __name__ == "__main__":
    input_file = "./complementing_strand_dna.txt"
    write_file(obtain_complementary(read_file(input_file)))
