#!/bin/bash

# Function to recursively delete files with specified extensions
delete_files() {
    local directory="$1"
    shift
    local extensions=("$@")
    
    # Loop through all files in the directory
    for file in "$directory"/*; do
        if [ -f "$file" ]; then
            # Check if the file has one of the specified extensions
            for ext in "${extensions[@]}"; do
                if [[ "$file" == *"$ext" ]]; then
                    # Delete the file if it has the specified extension
                    echo "Deleting file: $file"
                    rm "$file"
                    break
                fi
            done
        elif [ -d "$file" ]; then
            # Check if the directory starts with "_minted" and delete it
            if [[ "$file" == */_minted* ]]; then
                echo "Deleting folder: $file"
                rm -r "$file"
            else
                # Recursively call the function for subdirectories
                delete_files "$file" "${extensions[@]}"
            fi
        fi
    done
}

root_directory="/home/ugli/cours-2023-2024"
delete_extensions=("nav" "aux" "log" "out" "snm" "vrb" "toc" "synctex.gz" "pygtex" "pygstyle")
# Call the function to start the deletion process
delete_files "$root_directory"

echo "Deletion complete."
