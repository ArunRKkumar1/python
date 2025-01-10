import subprocess

# Prompt for the commit message
commit_message = input("Enter commit message: ")

try:
    # Stage all changes
    subprocess.run(["git", "add", "."], check=True)
    
    # Commit changes with the provided message
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    
    # Push to the main branch
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
    
    print("Git operations completed successfully!")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")