"""
Assignment 2: Word Counter from Text File
Count number of words, lines, and characters.
"""

import os


def count_file_stats(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    return {
        "lines": line_count,
        "words": word_count,
        "characters": char_count,
    }


def create_sample_file(filepath):
    sample_text = (
        "Python is a versatile programming language.\n"
        "It is widely used for web development, data science, and automation.\n"
        "This is a sample file created for the Word Counter assignment.\n"
    )
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(sample_text)
    print(f"Sample file created at '{filepath}'.")


def main():
    filepath = input("Enter the path of the text file: ").strip()

    if not os.path.exists(filepath):
        print(f"File '{filepath}' not found.")
        create_sample = input("Create a sample file at this path? (y/n): ").strip().lower()
        if create_sample == "y":
            create_sample_file(filepath)
        else:
            print("Exiting without processing.")
            return

    stats = count_file_stats(filepath)
    print("\n--- File Statistics ---")
    print(f"Lines      : {stats['lines']}")
    print(f"Words      : {stats['words']}")
    print(f"Characters : {stats['characters']}")


if __name__ == "__main__":
    main()
