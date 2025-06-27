# find files that start with a certain pattern
def find_files(directory,start_str):
    import os
    files = [f for f in os.listdir(directory) if f.startswith(start_str)]

    # If you want to handle only the first matching file
    if files:
        matching_file = files[0]
        #print(f"Found file: {matching_file}")
        return matching_file
    else:
        print(f"No file found for {directory}{start_str}")
        return None