# 🚢 IMPORTS
import os, subprocess, shutil

# ⚙️ CONFIG
repo_to_update = "https://github.com/aeiea/maybe-forknight.git" # put your repo's github thingy
folder_to_check_for_updates = "videos" # checks the folder test for updates
file_to_update = "videos.txt" # list of files in the directory test

# 🐍 CODE
print('''
       ,            .    ,       
 _.. .-+- _ . .._  _| _.-+- _ ._.
(_](_| | (_)(_|[_)(_](_] | (/,[  
               |                 
          by @aeiea
 used on aeiea/maybe-forknight
''')
subprocess.run("git clone --depth=1 " + repo_to_update + " thisfolderisgoingtobedeleted && rm -rf thisfolderisgoingtobedeleted/.git", shell=1)
files = [f for f in os.listdir("thisfolderisgoingtobedeleted/" + folder_to_check_for_updates + "/") if os.path.isfile(os.path.join("thisfolderisgoingtobedeleted/" + folder_to_check_for_updates + "/", f))]
shutil.rmtree("thisfolderisgoingtobedeleted")
thingtoedit = open(file_to_update, "w")
thingtoedit.write(str(files))
thingtoedit.close()
