# Tested in file transcribing_dna_into_rna.py
def read_file(input_file: str):
    with open(input_file, 'r') as f:
        dna = f.read()
        return dna

def replace(dna: str):
    rna = dna.replace('T', 'U')
    return rna

def write_result(rna: str):
    with open("./solution.txt", "w", encoding = "utf-8") as result:
        result.write(rna)

if __name__ == "__main__":
    input_file = "./transcribing_dna_into_rna.txt"
    dna = read_file(input_file)
    rna = replace(dna)
    write_result(rna)
