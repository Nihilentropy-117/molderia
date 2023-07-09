import os
import re

def remove_markdown_links(directory):
    # Regex pattern to match markdown links: ![alt_text](url)
    md_link_pattern = r"\[([^]]+)\]\(([^)]+)\)"

    # Walk through directory, including subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Process .md files only
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf8') as f:
                    file_contents = f.read()

                # Replace markdown links with link text
                new_contents = re.sub(md_link_pattern, r'\1', file_contents)

                # Write the modified contents back to the file
                with open(file_path, 'w', encoding='utf8') as f:
                    f.write(new_contents)

# Example usage
remove_markdown_links('../docs')
