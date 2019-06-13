# Python script for automating the whole process of project creation.

# This script creates a local directory and repository in github with provided name, using github API.

import requests
import subprocess
import json
import os.path
import sys

if len(sys.argv) == 4:
	repo = sys.argv[1]
	path = sys.argv[2]
	PAT = sys.argv[3]
elif len(sys.argv) == 3:
	repo = sys.argv[1]
	path = sys.argv[2]
	PAT = input("Enter PAT (Personal Access Token) ")
elif len(sys.argv) == 2:
	repo = sys.argv[1]
	path = input("Enter local path to save the repository ")
	PAT = input("Enter PAT (Personal Access Token) ")
else:
	repo = input("Enter repository name ")
	path = input("Enter local path to save the repository ")
	PAT = input("Enter PAT (Personal Access Token) ")

# Creating the required directory
dirName = path+"\\"+repo
try:
	os.makedirs(dirName)
except FileExistsError:
	print("Directory " , dirName ,  " already exists!")

# Making the created directory as present working directory
os.chdir(dirName)
# Initializing with empty git repository
subprocess.call("git init")

endpoint = "https://api.github.com/user/repos?access_token="+PAT

req_body = {
  "name": repo,
  "description": "Repo creted using script",
  "private":"false",
  "auto_init":"true"
}

r = requests.post(url = endpoint ,json = req_body)
r.json()
my_json = r.content.decode('utf8').replace("'", '"')
data = json.loads(my_json)

# Display errors if found any
if 'documentation_url' in data:
	if('errors' in data):
		print(data['errors'][0]['message'])
	else:
		print(data['message'])
else:
	# Creating the origin url with PAT token
	origin = "https://"+data['owner']['login']+":"+PAT+"@github.com/"+data['full_name']+".git"
	cmd = "git remote add origin "+origin
	subprocess.call(cmd)
	subprocess.call("git pull origin master")
	print("Successfully created and pushed at: "+data['clone_url'])
