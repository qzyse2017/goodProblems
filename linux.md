Linux 
_problems about Linux_

## How do I install a .tar.gz (or .tar.bz2) file?

steps:

- The first thing you need to do is extract the files from inside the tar archive to a folder.

- open your terminal and navigate to that directory 

- Make sure the directory include some files like`INSTALL`, `INSTALL.txt` or `README.md`. These files should include the instructions to help install the file.

Usually, the three "classical" steps are:

```shell
./configure
make
sudo make install
```

>You may also need to install some dependencies if, for example, running configure prompted you with an error listing which dependencies you are missing. You can also use checkinstall instead of make install. See here https://help.ubuntu.com/community/CheckInstall

REF

[answer from stackoverflow](https://askubuntu.com/questions/25961/how-do-i-install-a-tar-gz-or-tar-bz2-file)

## what is the difference between ctrl-z and ctrl-c in the terminal

>Control+C (control character intr) sends SIGINT which will interrupt the application. Usually causing it to abort, but this is up to the application to decide.

>Control+Z (control character susp) sends SIGTSTP to a foreground application, effectively putting it in the background, suspended

REF

https://askubuntu.com/questions/510811/what-is-the-difference-between-ctrl-z-and-ctrl-c-in-the-terminal

## What is the difference between ```'eval $(<cmds>)' and '<cmds>'```

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
