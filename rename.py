import os

# Parent directory containing the subdirectories
parent_directory = "dataset"

# List of subdirectories
directories = ["cheese", "okay", "one", "open hand", "revolt", "spiderman", "thumbs up"]

def rename_files_in_directory(directory):
    try:
        # Construct the full path of the subdirectory
        subdirectory_path = os.path.join(parent_directory, directory)
        
        # Get a list of all files in the subdirectory
        files = sorted(os.listdir(subdirectory_path))
        
        # Loop through the files and rename them
        for index, filename in enumerate(files, start=1):
            # Create the new filename
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{index}{file_extension}"
            
            # Create full path for old and new filenames
            old_filepath = os.path.join(subdirectory_path, filename)
            new_filepath = os.path.join(subdirectory_path, new_filename)
            
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{old_filepath}' to '{new_filepath}'")
    
    except Exception as e:
        print(f"An error occurred while renaming files in directory '{directory}': {e}")

# Loop through each subdirectory and rename the files
for directory in directories:
    rename_files_in_directory(directory)
