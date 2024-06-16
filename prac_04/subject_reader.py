FILENAME = "subject_data.txt"


def main():
    subjects = get_subjects()
    display_subjects(subjects)


def get_subjects():
    subjects = []
    input_file = open(FILENAME)
    for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subjects.append(parts)
    input_file.close()
    return subjects


def display_subjects(subjects):
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {str(subject[2])} students. ")


main()