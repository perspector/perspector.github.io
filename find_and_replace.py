# Useful find-and-replace script for replacing text in multiple files

import os


find = """
<p>Copyright &copy; 2023 - 2026 by Benjamin Chase</p>
            <p>The code for this website, excluding dependencies, is licensed under the GNU GPLv3 license.</p>
            <p>Code and license are available at: <a href="https://github.com/perspector/perspector.github.io">GitHub</a></p>
            <p><a href="https://github.com/perspector/perspector.github.io/actions/workflows/pages/pages-build-deployment"><img src="https://github.com/perspector/perspector.github.io/actions/workflows/pages/pages-build-deployment/badge.svg"></a><p>
"""

replace = """
<p>Copyright &copy; 2023 - 2026 by Benjamin Chase</p>
            <p>The code for this website, excluding dependencies, is licensed under the GNU GPLv3 license.</p>
            <p>Code and license are available at: <a href="https://github.com/perspector/perspector.github.io">GitHub</a></p>
            <p><a href="https://github.com/perspector/perspector.github.io/actions/workflows/pages/pages-build-deployment"><img src="https://github.com/perspector/perspector.github.io/actions/workflows/pages/pages-build-deployment/badge.svg"></a></p>
            <p><a href="https://perspector.github.io/impressum.html">Impressum</a></p>
"""
# remove leading and trailing newline
find = find[1:-1]
replace = replace[1:-1]


# originally from https://umatechnology.org/find-and-replace-text-in-multiple-files-in-bulk-on-windows-11-10/
def find_and_replace(dir_path, file_extension, find_text, replace_text):
    replace_count = 0
    for foldername, subfolders, filenames in os.walk(dir_path):
        print(f'Found {len(filenames)} files...')
        for filename in filenames:
            if filename.endswith(file_extension):  # You can specify other file types
                file_path = os.path.join(foldername, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        file_contents = file.read()
                        replace_count += file_contents.count(find_text)
                        new_contents = file_contents.replace(find_text, replace_text)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(new_contents)
                except Exception as e:
                    print(f'[ERROR] Skipped ({file_path}) because of exception:\n{e}\nMoving on...')
    print(f'Complete!\nReplaced {replace_count} occurances!')

# Usage
dir_path = '/home/superuser/Documents/GitHub/perspector.github.io'
file_extension = ".html"

find_and_replace(dir_path, file_extension, find, replace)
