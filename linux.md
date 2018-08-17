Linux 
_problems about Linux_

## What is the difference between 'eval $(<cmds>)' and '<cmds>'

It is `eval` will combine arguments follows it into a command and pass it to interpreter and return the exit code. But using `cmds` will directly run `<cmds>` itself which could sometimes contain some commands which can not be executed directly.

REF

[answer from stackoverflow](https://stackoverflow.com/questions/43001805/whats-the-difference-between-eval-command-and-command)
[bash manual reference](https://www.gnu.org/software/bash/manual/bash.html)

## SSH Key Permissions Chmod settings?
REF:  
[solution -- stackexchange](https://unix.stackexchange.com/questions/257590/ssh-key-permissions-chmod-settings)  
[gnu softerware manual about numeric chmod](https://www.gnu.org/software/coreutils/manual/html_node/Numeric-Modes.html#Numeric-Modes)  
Got a warning about ```permission for <id_rsa> are too open``` while adding it ssh-agent. 
The file ```~/.ssh/id_rsa``` should be writable and readable only to the user so its numeric mode should be ```600``` 

## Is there a TRY CATCH command in Bash?
REF: [answer from stackoverflow](https://stackoverflow.com/questions/22009364/is-there-a-try-catch-command-in-bash)  
No, use ```||``` or ```&&```
> Using ||:  
> if command1 fails then command2 runs as follows  
> command1 || command2  
> Similarly, using &&, command2 will run if command1 is successful