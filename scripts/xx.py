import os


def get_filenames_without_extensions(folder_path):
    files_without_extensions = []

    # List all files in the folder
    for filename in os.listdir(folder_path):
        # Check if it's a file
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Split the filename and extension
            name_without_extension, _ = os.path.splitext(filename)
            files_without_extensions.append(name_without_extension)

    return files_without_extensions


if __name__ == "__main__":
    folder_path = '../docs/Places'  # Replace this with the folder path you want to inspect

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        filenames_without_extensions = get_filenames_without_extensions(folder_path)
        print("File names without extensions in the folder:")
        for filename in filenames_without_extensions:
            print(filename)
    else:
        print("Invalid folder path.")
