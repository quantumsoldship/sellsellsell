def log(key, data):
    filename = "data/data.txt"
    entries = {}

    # Read existing entries from the file
    try:
        with open(filename, 'r') as file:
            for line in file:
                existing_key, existing_data = line.strip().split(": ", 1)
                entries[existing_key] = existing_data
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty dictionary
        pass

    # Update the entry or add a new one
    entries[key] = data

    # Write all entries back to the file
    with open(filename, 'w') as file:
        for k, v in entries.items():
            file.write(f"{k}: {v}\n")


def output_log(key):
    filename = "data/data.txt"
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(f"{key}:"):
                return line[len(key) + 2:].strip()
    return None