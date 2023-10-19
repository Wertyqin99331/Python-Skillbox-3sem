def count_letters(file_name):
    statistics = {}

    with open(file_name, "r") as file:
        for line in file:
            line = line.lower()

            for char in line:
                if char.isalpha():
                    if char in statistics:
                        statistics[char] += 1
                    else:
                        statistics[char] = 1

    sorted_statistics = sorted(statistics.items(), key=lambda x: x[1])

    with open("statistics.txt", "w") as file:
        for item in sorted_statistics:
            file.write(f"{item[0]}: {item[1]}\n")


filename = "input.txt"
count_letters(filename)
