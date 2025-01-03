import subprocess
from datetime import datetime

def get_git_changeset_timestamp(absolute_path):
    repor_dir = absolute_path
    git_log = subprocess.Popen(
        "git log --pretty=format:%ct --quiet -1 HEAD",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True, 
        cwd=repor_dir,
        universal_newlines=True
    )
    timestamp = git_log.communicate()[0]
    try:
        timestamp = datetime.utcfromtimestamp(int(timestamp))
        
    except ValueError as vr:
        # fallback for current time stamp
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    change_set_timestamp= timestamp.strftime('%Y-%m-%d %H:%M:%S')
    return change_set_timestamp