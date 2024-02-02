import os
import sys
from shutil import copyfile

def setup_git_hook():
    git_dir = os.path.join(os.getcwd(), '.git', 'hooks')
    if not os.path.exists(git_dir):
        print("This doesn't seem to be a Git repository.")
        sys.exit(1)
    
    hook_path = os.path.join(git_dir, 'pre-push')
    if os.path.exists(hook_path):
        print("A pre-push hook already exists. Backup and replace? [y/N]")
        if input().lower() != 'y':
            sys.exit(0)
    
    script_path = os.path.join(os.path.dirname(__file__), 'src/generate_docs.py')
    try:
        with open(hook_path, 'w') as hook_file:
            hook_file.write("#!/bin/sh\n")
            hook_file.write(f"python {script_path}\n")
        
        # Make the hook executable
        os.chmod(hook_path, 0o775)
        print("Pre-push hook setup complete.")
    except Exception as e:
        print(f"Failed to set up pre-push hook: {e}")
        sys.exit(1)

if __name__ == "__main__":
    setup_git_hook()
