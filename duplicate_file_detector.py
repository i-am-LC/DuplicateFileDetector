import hashlib, os

# Produce a hash of the file.
def get_file_hash(file_path):
    with open(file_path, 'rb') as file_object:
        file_hash = hashlib.md5(file_object.read()).hexdigest()
    return file_hash

# Find duplicates from the directory.
def find_duplicates(root_folder):
    unique_records = set()
    duplicates = []
    for root, _, files in os.walk(root_folder, topdown=True):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            if file_hash not in unique_records:
                unique_records.add(file_hash)
            else:
                duplicates.append(file_path)
    return duplicates

# Delete duplicates depending on user input.
def delete_duplicates(duplicates):
    if duplicates:
        print('### Duplicate files:')
        for duplicate in duplicates:
            print(duplicate)
        print('\nAre you happy to delete the above records? Enter "Y" to proceed.')
        user_approval = input()
        if user_approval.lower() == 'y':
            for duplicate in duplicates:
                os.remove(duplicate)
            print('Duplicates deleted.')
    else:
        print('No duplicates found.')

# Main function. Explanation to the user and input for the directory path.
def main():
    explanation = (
        "This script scans a directory and its subdirectories for duplicate files. "
        "It calculates the MD5 hash of each file to identify duplicates. "
        "If duplicate files are found, they will be listed, and you'll be prompted to "
        "confirm whether you want to delete them."
    )
    print(explanation)
    proceed = input("Would you like to proceed? (Enter 'Y' for Yes): ")
    if proceed.lower() != 'y':
        return
    root_folder = input("Enter the directory path to scan for duplicates: ")
    if not os.path.isdir(root_folder):
        print("Invalid directory path.")
    else:
        duplicates = find_duplicates(root_folder)
        delete_duplicates(duplicates)

if __name__ == "__main__":
    main()