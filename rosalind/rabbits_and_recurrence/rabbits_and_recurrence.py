def read_file(input_file: str):
    with open(input_file, "r") as f:
        numbers = f.read()
        return numbers.strip().split(" ")

def dynamic_algorithm(numbers: list):
    fn = [1, 1]
    n = int(numbers[0])
    k = int(numbers[1])

    # n-2 because F1 and F2 are already defined
    for i in range(0, n-2):
        rabbits = fn[i+1] + (fn[i] * k)
        fn.append(rabbits)

    result = fn[n-1]
    return result


def write_results(result: int):
    with open("./solution.txt", "w", encoding = "utf-8") as r:
        print(result, file = r)

if __name__ == "__main__":
    input_file = "./rabbits_and_recurrence.txt"
    write_results(dynamic_algorithm(read_file(input_file)))