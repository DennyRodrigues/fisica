import os
import shutil

# Define the source and destination directories
source_dir = "C:\\Users\\denny\\Pictures\\instagramCloneImages"
destination_dir = "C:\\Users\\denny\\Documents\\Programming, Science Computer\\react native instagram app\\InstagramClone\\backend\\src\\main\\upload\\images"

# Get list of all files in the destination directory
destination_files = os.listdir(destination_dir)

# Get list of all files in the source directory
source_files = os.listdir(source_dir)

# Check if the source directory has files
if len(source_files) == 0:
    print("No files found in the source directory. Exiting.")
else:
    # Iterate over all files in the destination folder
    for i, dest_filename in enumerate(destination_files):
        # Use source files in a cyclic manner if there are fewer source files
        source_file = os.path.join(source_dir, source_files[i % len(source_files)])
        destination_file = os.path.join(destination_dir, dest_filename)

        # Ensure the source file exists
        if os.path.exists(source_file):
            # Copy and overwrite the file
            shutil.copy2(source_file, destination_file)
            print(f"Copied {source_file} to {destination_file}")
        else:
            print(f"Source file {source_file} does not exist, skipping.")
