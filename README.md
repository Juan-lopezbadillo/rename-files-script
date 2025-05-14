# rename-files-script
This script is designed to efficiently rename multiple files within the `Files` folder. It prompts the user to enter a prefix, which is then added to the beginning of each filename in the specified folder. This tool can be useful for batch-renaming files to include project codes, dates, or other identifiers.

## How to Use 

1. **Ensure Python 3 is installed** on your system.
2. **Place the file you wish to rename** inside the folder named `Files`. This `Files` folder should be located in the same directory as the script files (`rename_files` and `run_rename_files`).
3. **Double-click the `run_renaame_files`.**
4. A command prompt window will appear, asking yyou to **"Update with?: "**
5. **Type the desired prefix** and press **Enter**
6. Once the script has finished renaming the files, a confirmation messagewill be displayed in the command prompt.

## Notes and Considerations

* This script will rename all files directly within the `Files` folder. It does not process files in subfolders.
* Be cautious when running the script, as the renaming action is immediate and irreversible without manual intervention.
* Ensure that the `Files` folder exists in the same directory as `run_rename_files` before running the script.
* The prefix you enter will be added to the beginning of the existing filename, separated by an underscore (`_`). For example, if you enter `PROJECT-A` and a file is named `document.pdf`, it will be renamed to `PROJECT-A_document.pdf`.
* If you encounter any issues, please ensure that Python 3 is correctly installed and that the folder structure is as described above.

## Author Juan Carlos Lopez Badillo

## Date 

05/14/2025

