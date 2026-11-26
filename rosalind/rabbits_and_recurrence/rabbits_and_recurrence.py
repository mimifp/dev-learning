def read_file(input_file: str):
    with open(input_file, "r") as f:
        numbers = f.read()
        return numbers.strip().split(" ")


def rabbits_algorithm(numbers: list):
    months = int(numbers[0])
    offspring = int(numbers[1])
    f1 = f2 = 1

    for i in range(months-1):
        f2, f1 = f1, f1 + (f2 * offspring)

    return f2


def write_results(result: int):
    with open("./solution.txt", "w", encoding = "utf-8") as r:
        print(result, file = r)

if __name__ == "__main__":
    input_file = "./rabbits_and_recurrence.txt"
    write_results(rabbits_algorithm(read_file(input_file)))
