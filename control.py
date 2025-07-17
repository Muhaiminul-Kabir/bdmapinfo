import json
import time
import sys
import subprocess

from link_ex import extract_link
from art_ex import extract_art
from para_ex import extract_para


url = "https://www.thedailystar.net/news/bangladesh"

e = 3

while e>0:
    print("Initiating process...")

    
    
    extract_link(url)
            
    with open('data/output.json', 'r') as file:
        data = json.load(file)  # load JSON into a Python dict/list
        
    for i in data:
        sub_url = i['links'][0]
        sub_url = "https://www.thedailystar.net/"+sub_url['href']
        date = extract_para(sub_url)
        extract_art(sub_url,date)
    
    
    command = "git add * && git commit -m \"CRUD\" && git push"

    # Run command as string
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    print("STDOUT:")
    print(result.stdout)

    print("STDERR:")
    print(result.stderr)
    
    
    e = e-1
    total = 60
    for remaining in range(total, 0, -1):
        sys.stdout.write(f" \rProcess resumes untill : {remaining}s left...")
        sys.stdout.flush()
        time.sleep(1)