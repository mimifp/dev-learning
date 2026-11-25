input_file = str("./computing_gc_content.txt")
with open (input_file, "r", encoding="utf-8") as f:
    fast_seq = f.readlines
    clean_seq = [s.strip() for s in fast_seq]
    # continue ...

print(clean_seq)
print(len(clean_seq))