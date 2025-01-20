def log(key, data):
    filename = "data/data.txt"
    with open(filename, 'w') as file:
        file.write(f"{key}: {data}\n")


def output_log(key):
    filename = "data/data.txt"
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(f"{key}:"):
                return line[len(key) + 2:].strip()
    return None