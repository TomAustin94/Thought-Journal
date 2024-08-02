def print_header(title):
    print("\n" + "=" * (len(title) + 4))
    print(f"  {title}  ")
    print("=" * (len(title) + 4) + "\n")

def cbt_thought_journal():
    print_header("CBT Thought Journal")
    print("This tool will help you identify and challenge negative thoughts.")
    print("Let's get started!\n")

    # Step 1: Describe the Situation
    situation = input("1. Describe the situation that triggered your thoughts and feelings: ")

    # Step 2: Record Your Thoughts
    thoughts = input("2. What thoughts went through your mind? ")

    # Step 3: Identify the Emotions
    emotions = input("3. What emotions did you feel? (e.g., sad, anxious, angry) ")

    # Step 4: Challenge the Thoughts
    challenge = input("4. What evidence do you have that supports these thoughts? ")

    # Step 5: Consider Alternative Perspectives
    alternative = input("5. What evidence do you have against these thoughts? ")

    # Step 6: Reframe the Thoughts
    reframe = input("6. What is a more balanced and realistic way of looking at the situation? ")

    # Step 7: Outcome
    outcome = input("7. How do you feel now after reframing your thoughts? ")

    # Display the journal entry
    print_header("Your CBT Thought Journal Entry")
    print(f"Situation: {situation}")
    print(f"Thoughts: {thoughts}")
    print(f"Emotions: {emotions}")
    print(f"Evidence for Thoughts: {challenge}")
    print(f"Evidence Against Thoughts: {alternative}")
    print(f"Reframed Thoughts: {reframe}")
    print(f"Outcome: {outcome}")
    print("\n" + "=" * 40)

if __name__ == "__main__":
    cbt_thought_journal()
