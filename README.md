# terminal-cheat-sheet
a small cheat sheet I've made using python that prints out a command you'd need to know the syntax of, or just need to remember it's functionality.

#PREREQUISITES
- python3 obviously
- a linux terminal (mac is the same)

#USAGE
- cheat (command you'd like to know about)
- cheat all: gives you all the commands and their syntax/use case
- cheat help: prompts you what you'd like to do with the terminal, then provides the command needed to execute said thing.
- cheat help (thing *not command*): provides instant help execution without display & prompt process.

#EXAMPLES
- cheat pwd
- cheat all
- cheat help
- cheat help copy

you may use a windows shell/command prompt for this project too! just add it to your PATH as an alias then you're good to go.

#HOW TO USE
1. clone the repository into your home directory, meaning Users/{your-name}
2. ensure you get your files's exact root directory (you can have it using "find / -name "cheat.py" 2>/dev/null" on the terminal [without the " ])
3. cd to your ~./bash_profile or ~/.zshrc, which are both located in the root (meaning if you were in the {your-name} directory, do cd .. twice to reach top level)
4. edit your bash profile or zshrc using nano {name from earlier} or sudo nano {name from earlier} if you face any permission erros.
5. go to the last line, add this: alias cheat:'python3 path/to/cheat.py', then control O, enter, then control X to exit
6. now use command line arguments to use the input for the cheat sheet, as such: cheat mkdir
7. you may use 'cheat all' to see all the currently saved commands and their explanations listed. 
