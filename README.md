# PyTODO  
PyTODO.py - a pythonian way to handle tasks from the command line  
author: Sebastian Schwalbe  
date:   12.03.2019  
language: python2.7  
os: tested and generated on linux (ubuntu, debian, cent-os etc.)  

This is a very small sized implementation of a pythonian todo task manager.  
The package uses the os, pickle, datetime and argparse python packages.  
It is designed for the command line usage.  
All tasks are save in a todo.pckl file.  

**Installation**  

You might need to install the package/s:  

* pickle  
* argparse   

Add in your .bashrc file  

* alias todo='python /[path_to_todo.py]/PyTODO.py'  

and do  

* source .bashrc.  

After that the todo.py is available as todo command in your bash.  

**Example usage in command line (bash)**

user@pc:~ todo -t test.pckl -p project1  
Creating: test.pckl  
{'project1': {}}  
user@pc:~ todo -t test.pckl -a project1 do 1st task 1 high  
Loading: test.pckl  
{'project1': {1: ['Sunday 09. December 2018', 'do 1st task', 'high']}}  
user@pc:~ todo -t test.pckl -a project1 do 2nd task 1 medium  
Loading: test.pckl  
{'project1': {1: ['Sunday 09. December 2018', 'do 2nd task', 'medium']}}  
user@pc:~ todo -t test.pckl -la  
Loading: test.pckl  
Project: project1
1 (medium) Sunday 09. December 2018 : do 2nd task  
user@pc:~ rm test.pckl  
user@pc:~ todo -t test.pckl -p project1  
Creating: test.pckl  
{'project1': {}}  
user@pc:~ todo -t test.pckl -a project1 do 1st task 1 high  
Loading: test.pckl  
{'project1': {1: ['Sunday 09. December 2018', 'do 1st task', 'high']}}  
user@pc:~ todo -t test.pckl -a project1 do 2nd task 2 medium  
Loading: test.pckl  
{'project1': {1: ['Sunday 09. December 2018', 'do 1st task', 'high'], 2: ['Sunday 09. December 2018', 'do 2nd task', 'medium']}}  
user@pc:~ todo -t test.pckl -la  
Loading: test.pckl  
Project: project1  
1 (high) Sunday 09. December 2018 : do 1st task  
2 (medium) Sunday 09. December 2018 : do 2nd task  
user@pc:~ todo -t test.pckl -d project1 1  
Loading: test.pckl  
{'project1': {2: ['Sunday 09. December 2018', 'do 2nd task', 'medium']}}  
user@pc:~ todo -t test.pckl -la  
Loading: test.pckl  
Project: project1  
2 (medium) Sunday 09. December 2018 : do 2nd task  

**Further examples**

Some examples are provided in the examples directory  
An alternative use of this package can be monitoring of cluster/queuing jobs.  
For example, you can use one project for one cluster you need to monitor your calculations (see e.g. examples/jobs.pckl).   

You can load the examples like  
* user@pc:~ todo -t todo.pckl -la
* user@pc:~ todo -t todo2.pckl -la
* user@pc:~ todo -t jobs.pckl -la
