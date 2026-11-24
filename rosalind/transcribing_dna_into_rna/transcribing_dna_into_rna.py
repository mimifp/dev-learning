# Tested in file transcribing_dna_into_rna.py
input_file = "./transcribing_dna_into_rna.txt"

with open(input_file, 'r') as f:
    dna = f.read()

rna = dna.replace('T', 'U')

with open("./solution.txt", "w", encoding = "utf-8") as result:
    result.write(rna)
