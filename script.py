import subprocess
import time

def git_auto_update():
    while True:
        try:
           
            subprocess.run(["git", "add", "."])
            
            
            commit_message = "conditions works successfully"             # Commit changes with a default message
            subprocess.run(["git", "commit", "-m", commit_message])
            
            
            subprocess.run(["git", "push", "-u", "origin", "main"])
            
            print("Changes pushed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
        
       
        time.sleep(300)    # Wait for 5 minutes (300 seconds) before the next update

# Run the auto-update function
git_auto_update()
