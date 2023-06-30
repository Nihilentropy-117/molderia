import os
import re

def remove_dead_markdown_links(folder_path):
    # Iterate over all files and folders in the given path
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()

                # Find and remove dead markdown links
                updated_content = re.sub(r'\[([^\]]+)\]\(.md\)', r'\1', content)

                # Write the updated content back to the file
                with open(file_path, 'w') as f:
                    f.write(updated_content)

                print(f"Processed file: {file_path}")

# Usage example
folder_path = '../docs'
remove_dead_markdown_links(folder_path)

