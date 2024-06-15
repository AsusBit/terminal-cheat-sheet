import sys
command = ''
try:
	command = sys.argv[1]
except Exception as e:
	print("error:", e)

dict = {
    "cat": "\n[cat (some file)]: this command is used to display the contents of a file in the terminal.\n",
    "mkdir": "\n[mkdir (new folder name)]: this creates a new folder in your current directory.\n",
    "cp" : "\n[cp (original file) (new duplicate file)]: this copies the original file then duplicates it into the other file, in case the other file does not exist, it creates it.\n",
    "ls": "\n[ls]: this lists all files and directories in the current directory.\n",
    "cd": "\n[cd (directory)]: this changes the current directory to the specified one.\n",
    "rm": "\n[rm (file)]: this removes a file.\n",
    "rmdir": "\n[rmdir (directory)]: this removes an empty directory.\n",
    "touch": "\n[touch (file)]: this creates a new empty file or updates the timestamp of an existing file.\n",
    "mv": "\n[mv (source) (destination)]: this moves or renames a file or directory.\n",
    "pwd": "\n[pwd]: this prints the current working directory.\n",
    "echo": "\n[echo (text)]: this prints the specified text to the terminal.\n",
    "grep": "\n[grep (pattern) (file)]: this searches for a specified pattern in a file or files.\n",
    "find": "\n[find (directory) -name (filename)]: this searches for files and directories by name starting from a specified directory.\n",
    "chmod": "\n[chmod (permissions) (file)]: this changes the permissions of a file or directory.\n\nUnderstanding File Permissions\nEach file or directory has three types of permissions:\n\n    Read (r): Permission to read the file.\n    Write (w): Permission to modify the file.\n    Execute (x): Permission to execute the file (run it as a program or script).\n\nPermissions are also divided into three categories based on who can access the file:\n\n    Owner (user): The user who owns the file.\n    Group: Other users who are in the file's group.\n    Others: All other users.\n\nSymbolic Mode\n\nIn symbolic mode, you can set or modify permissions using symbols.\n\nAdding Permissions\n\n    +: Adds a permission.\n    -: Removes a permission.\n    =: Sets a permission explicitly.\n\nExamples\n\n    chmod +x file: Adds execute permission for everyone.\n    chmod u+x file: Adds execute permission for the file's owner (user).\n    chmod g+x file: Adds execute permission for the group.\n    chmod o+x file: Adds execute permission for others.\n    chmod a+x file: Adds execute permission for all (equivalent to chmod +x file).\n",
    "pbcopy": "\n[pbcopy < (file)]: this one copies file to the clipboard instead of directly moving it into a destinaation.\n",
    "pbpaste": "\n[pbpaste > (new file)]: this pastes the file you copied using pbcopy in your current directory",
    "chown": "\n[chown (user):(group) (file)]: this changes the owner and group of a file or directory.\n",
    "man": "\n[man (command)]: this displays the manual page for the specified command.\n",
    "df": "\n[df]: this shows the disk space usage of the file system.\n",
    "du": "\n[du]: this shows the disk usage of files and directories.\n",
    "ps": "\n[ps]: this displays information about currently running processes.\n",
    "kill": "\n[kill (process id)]: this terminates a process by its process ID.\n",
    "ssh": "\n[ssh (user)@(host)]: this connects to a remote host via SSH.\n",
    "scp": "\n[scp (source) (destination)]: this securely copies files between hosts over SSH.\n",
    "wget": "\n[wget (url)]: this downloads files from the internet.\n",
    "curl": "\n[curl (url)]: this transfers data from or to a server using various protocols.\n",
    "tar": "\n[tar -czvf (archive.tar.gz) (directory)]: this creates a compressed archive of a directory.\n",
    "unzip": "\n[unzip (file.zip)]: this extracts files from a zip archive.\n"
}

dict_desc = {
    "display": "cat",
    "make-directory": "mkdir",
    "copy": "cp",
    "copy-to-clipboard": "pbcopy",
    "paste": "pbpaste",
    "list": "ls",
    "change-directory": "cd",
    "remove": "rm",
    "remove-directory": "rmdir",
    "create-file": "touch",
    "move": "mv",
    "print-directory": "pwd",
    "print": "echo",
    "search": "grep",
    "locate": "find",
    "change-permissions": "chmod",
    "change-owner": "chown",
    "manual": "man",
    "disk-space": "df",
    "disk-usage": "du",
    "processes": "ps",
    "terminate": "kill",
    "connect": "ssh",
    "secure-copy": "scp",
    "download": "wget",
    "transfer": "curl",
    "archive": "tar",
    "extract": "unzip"
}

def printAll(dict):
    for key in dict:
        print(dict[key])


def help(dict, dict2):
    print("--Help section--")
    for key in dict:
        print(key)
    helpVal = input("which keyword did you need help with: ")
    if helpVal in dict:
        print("use:",dict2[dict[helpVal]])
    else:
        print("keyword is not in the list.")

def helpCMD(dict, dict2, argval):
    if argval in dict:
        print("use:", dict2[dict[argval]])
    else:
        print("keyword is not in list")       
                     
if command == 'all':
    	printAll(dict)
elif command == "help":
    if len(sys.argv) > 2:
        helpCMD(dict_desc, dict, sys.argv[2])   
    else:
        help(dict_desc, dict)     	
elif command not in dict:
	print("command not found")
else:
	print(dict[command])
