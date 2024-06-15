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
    "chmod": "\n[chmod (permissions) (file)]: this changes the permissions of a file or directory.\n",
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

def printAll(dic):
    for key in dic:
        print(dic[key])

        
if command == 'all':
    	printAll(dict)
elif command not in dict:
	print("command not found")
else:
	print(dict[command])
