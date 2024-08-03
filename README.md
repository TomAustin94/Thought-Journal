# CBT Thought Journal

## Description
This project contains four Python scripts for a Cognitive Behavioral Therapy (CBT) Thought Journal. These tools help users identify and challenge negative thoughts, providing a structured approach to cognitive restructuring.

## Scripts

### Terminal Versions
1. `cbt_journal_terminal.py`
   - Provides a CBT thought journaling experience that only outputs to the terminal and does not store any information.

2. `cbt_journal_terminal_csv.py`
   - Offers the same CBT thought journaling experience but with an additional option to save entries to a CSV file.

### Web UI Versions
3. `cbt_journal_web.py`
   - A web-based version of the CBT thought journal that doesn't store any information.

4. `cbt_journal_web_csv.py`
   - A web-based version that offers the option to save entries to a CSV file.

## Features
- Guided prompts for CBT thought journaling
- Pretty formatting for terminal output (in terminal versions)
- Modern, responsive web interface using Bootstrap (in web versions)
- Option to save entries to a CSV file (in CSV-saving versions)

## Requirements
- Python 3.x
- Flask (for web versions)
- Bootstrap 5.1.3 (loaded via CDN in web versions)

## Installation
1. Clone this repository or download the scripts.
2. Ensure you have Python 3.x installed on your system.
3. Install required packages:

pip install -r requirements.txt


## Usage

### For Terminal Versions
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script:

python cbt_journal_terminal.py

or

python cbt_journal_terminal_csv.py

4. Follow the prompts to complete your thought journal entry.
5. Review your entry in the terminal output.
6. For the CSV version, choose whether to save the entry when prompted.

### For Web UI Versions
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script:

python cbt_journal_web.py

or

python cbt_journal_web_csv.py

4. Open a web browser and go to `http://127.0.0.1:5000/`
5. Fill out the form and submit to see your journal entry.
6. For the CSV version, entries are automatically saved.

## CSV File
- If using CSV-saving versions, entries are saved to `cbt_journal_entries.csv` in the same directory as the script.
- Each entry is appended as a new row in the CSV file.
- The CSV file includes headers for each column.

## Privacy Note
- The terminal-only and web-only versions do not store any information.
- The CSV-saving versions store entries locally in a CSV file.

## Customization
You can modify the scripts to add more prompts, change the formatting, or adjust the CSV saving functionality as needed. The web UI can be further customized by modifying the HTML templates and CSS.

## Acknowledgments
This project was inspired by Cognitive Behavioral Therapy techniques and aims to provide a simple, accessible tool for thought journaling. The web UI utilizes Bootstrap for responsive design.
