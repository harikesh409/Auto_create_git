@echo off 

rem Batch script for automating the whole process of project creation.
rem This script creates a local directory and repository in github with provided name, using github API.

if [%1]==[] (set /p repo="Enter repository name: ") else (set repo=%1)
if [%2]==[] (set /p username="Enter github username: ") else (set username=%2)
if [%3]==[] (set /p path="Enter local path to save the repository: ") else (set path=%3)
if [%4]==[] (set /p pac="Enter PAC (Personal Access Token): ") else (set pac=%4)

set endpoint="https://api.github.com/user/repos?access_token=%pac%"

curl -i -d "{\"name\": \"%repo%\", \"private\": false, \"auto_init\": true}" %endpoint%

cd %path%
mkdir %repo%
git init
git remote add origin "https://%username%:%pac%@github.com/%username%/%repo%.git"
git pull origin master
pause
