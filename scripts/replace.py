import os

folder_path = '../docs'

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith('.md'):
            file_path = os.path.join(root, filename)
            with open(file_path, 'r') as file:
                content = file.read()
        
            modified_content = content.replace('.md.md', '.md')
            print(f"Replaced in {filename}")
            with open(file_path, 'w') as file:
                file.write(modified_content)

