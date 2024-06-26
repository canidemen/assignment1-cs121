import PartA

def tokenize_file(file_path):
    file_list = PartA.tokenize(file_path)
    return PartA.computeWordFrequencies(file_list)


def compare_files():
    file_1 = input("Please enter a path to a text file:\n")
    file_2 = input("Please enter a path to a second file:\n")
    file_1_dict = tokenize_file(file_1)
    file_2_dict = tokenize_file(file_2)
    similar_words = []

    for token in file_1_dict:
        if token in file_2_dict:
            if token in similar_words:
                continue
            else:
                similar_words.append(token)

    print(f"Common words:")
    for i in similar_words:
        print(i)

    print(f"\nCommon occurrences:\n{len(similar_words)}")


if __name__ == "__main__":
    compare_files()
