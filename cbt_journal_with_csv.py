import csv
from datetime import datetime
import os

def print_header(title):
    print("\n" + "=" * (len(title) + 4))
    print(f"  {title}  ")
    print("=" * (len(title) + 4) + "\n")

def cbt_thought_journal():
    print_header("CBT Thought Journal")
    print("This tool will help you identify and challenge negative thoughts.")
    print("Let's get started!\n")

    # Collect journal entry data
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    situation = input("1. Describe the situation that triggered your thoughts and feelings: ")
    thoughts = input("2. What thoughts went through your mind? ")
    emotions = input("3. What emotions did you feel? (e.g., sad, anxious, angry) ")
    challenge = input("4. What evidence do you have that supports these thoughts? ")
    alternative = input("5. What evidence do you have against these thoughts? ")
    reframe = input("6. What is a more balanced and realistic way of looking at the situation? ")
    outcome = input("7. How do you feel now after reframing your thoughts? ")

    # Display the journal entry
    print_header("Your CBT Thought Journal Entry")
    print(f"Date: {date}")
    print(f"Situation: {situation}")
    print(f"Thoughts: {thoughts}")
    print(f"Emotions: {emotions}")
    print(f"Evidence for Thoughts: {challenge}")
    print(f"Evidence Against Thoughts: {alternative}")
    print(f"Reframed Thoughts: {reframe}")
    print(f"Outcome: {outcome}")
    print("\n" + "=" * 40)

    # Ask user if they want to save the entry
    save_option = input("\nWould you like to save this entry to a CSV file? (yes/no): ").lower()
    if save_option == 'yes':
        save_to_csv(date, situation, thoughts, emotions, challenge, alternative, reframe, outcome)

def save_to_csv(date, situation, thoughts, emotions, challenge, alternative, reframe, outcome):
    filename = 'cbt_journal_entries.csv'
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Date', 'Situation', 'Thoughts', 'Emotions', 'Evidence For', 'Evidence Against', 'Reframed Thoughts', 'Outcome']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()  # Write header if file doesn't exist
        
        writer.writerow({
            'Date': date,
            'Situation': situation,
            'Thoughts': thoughts,
            'Emotions': emotions,
            'Evidence For': challenge,
            'Evidence Against': alternative,
            'Reframed Thoughts': reframe,
            'Outcome': outcome
        })
    
    print(f"\nEntry saved to {filename}")

if __name__ == "__main__":
    cbt_thought_journal()
