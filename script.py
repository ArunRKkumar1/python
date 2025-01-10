import subprocess
import time

def git_auto_update():
    while True:
        try:
            # Stage all changes
            subprocess.run(["git", "add", "."], check=True)
            
            # Commit changes with a default message
            commit_message = "Auto-update"
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            
            # Push changes to the main branch
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            
            print("Changes pushed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
        
        # Wait for 5 minutes (300 seconds) before the next update
        time.sleep(300)

# Run the auto-update function
git_auto_update()
