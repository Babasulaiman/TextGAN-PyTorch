def check_sequence_lengths(file_path, expected_length):
    with open(file_path, 'r') as file:
        for line in file:
            tokens = line.strip().split()  # or another tokenization method
            if len(tokens) != expected_length:
                print(f"Unexpected length {len(tokens)}: {line}")

check_sequence_lengths('dataset/sample.txt', 115)
