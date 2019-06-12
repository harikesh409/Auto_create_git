@echo off 

if [%1]==[] (set /p repo="Enter repository name: ") else (set repo=%1)
if [%2]==[] (set /p username="Enter repository name: ") else (set username=%2)
if [%3]==[] (set /p pac="Enter PAC (Personal Access Token): ") else (set pac=%3)

set endpoint="https://api.github.com/user/repos?access_token=%pac%"

rem set op=curl -i -d "{\"name\": \"%repo%\", \"private\": true}" %endpoint%

curl -i -d "{\"name\": \"%repo%\", \"private\": true}" %endpoint%

echo create.bat>>.gitignore
git init
git add .
git commit -m "Initial commit"
git remote add origin "https://%username%:%pac%@github.com/%username%/%repo%.git"
git push -u origin master
