#
# Simple pythonian framework for task management 
#
# Author: 	Sebastian Schwalbe (SS) 
# Date: 	09.12.2018 
# TODO: 	- color theme for ouput might need an approvement 
#		- support for combing two todo.pckl files needed 
#		- supoort for adding specific data from one to another todo.pckl file needed 
	
import pickle 
import os 
import os.path  
from datetime import * 
import argparse

class PyTODO:
	# todo package main class

	def __init__(self,fname="./todo.pckl"):
		# Check wheather a todo.pckl exist or not 
		# If a todo.pckl exist load it 
		# fname ... name of the todo list in a todo.pckl format 
		self.fname = fname
		if os.path.isfile(self.fname) and os.access(self.fname, os.R_OK):
			print("Loading: %s" % fname)
			self.load_dict()
		else:
			print("Creating: %s" % fname)
			self.todo_dict = {}

	def add_project(self,project_title):
		# Add a new project 
		project_dict = {project_title : {}}
		self.todo_dict.update(project_dict)	
		print(self.todo_dict)
		self.save_dict()
	
	def del_project(self,project_title):
		# Delete a complete project 
                del self.todo_dict[project_title]
		print(self.todo_dict)
                self.save_dict()
	
	def add_task(self,project_title,task,task_num,priority):
		# Add a task for a project 
		d = date.today()
		date_str =  d.strftime("%A %d. %B %Y")
		self.todo_dict[project_title].update({task_num : [date_str,task,priority]})
		print(self.todo_dict)
		self.save_dict()

	def del_task(self,project_title,task_num):
		# Delete a task from a project 
		del self.todo_dict[project_title][task_num]
		print(self.todo_dict)
		self.save_dict()

	def print_task(self,project_title,task_num):
		# Print a task from a project
		keys = self.todo_dict[project_title].keys() 
		task = self.todo_dict[project_title][keys[task_num]]
		print("%i (%s) %s : %s" % (keys[task_num],task[2],task[0],task[1]))
	
	def print_project(self,project_title):
		# Print all tasks for one project 
		# Ref.: colors https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
		CEND = '\33[0m'
		CRED = '\33[31m'
		CGREEN  = '\33[92m'
		CYELLOW = '\33[33m'
		CBLUE   = '\33[34m'
		CVIOLETT = '\33[35m'
		priority = {'veryhigh' : CRED, 'high': CRED, 'medium' : CYELLOW, 'low' : CGREEN} 
		print(CBLUE + "Project: %s" % project_title + CEND)
		keys = self.todo_dict[project_title].keys()
		for i in range(1,len(self.todo_dict[project_title])+1):
			task = self.todo_dict[project_title][keys[i-1]]
                	print("%i (" %keys[i-1] +priority[task[2].lower()]+ "%s" % task[2]+ CEND +") %s : %s" % (task[0],task[1]))

	def print_all_projects(self):
		# Print all tasks for all projects
		for i in self.todo_dict.keys():
			self.print_project(i)
	def save_dict(self):
		# Save the todo_dict as todo.pckl file 
		pickle.dump( self.todo_dict, open( self.fname, "wb" ) ) 

	def load_dict(self):
		# Load a todo.pckl file 
		self.todo_dict = pickle.load( open( self.fname, "rb" ) )

def todo_argparser():
	# Command line parsing for the todo package. 
	parser = argparse.ArgumentParser(description='Commandline argparser for todo package.')
	parser.add_argument('-t', metavar='t',type=str, nargs='+', help='load a specific todo.pckl: path/[name],pckl (one word)')
	parser.add_argument('-p', metavar='p',type=str, nargs='+', help='add new project: format project_title (one word)')
	parser.add_argument('-f', metavar='f',type=str, nargs='+', help='finish project: format project_title (one word) ')
	parser.add_argument('-l', metavar='l',type=str, nargs='+', help='list all task for a project: format project_title (one word) ')
	parser.add_argument('-la',action='store_true', default = None, help='list all task for all projects')
	parser.add_argument('-a', metavar='a', type=str, nargs='+', help='add_task: format project_title (one word) task (more words) task_num (integer number)  priority (one word)')
	parser.add_argument('-d', metavar='d', type=str, nargs='+', help='del_task: format project_title (one word) task_num (integer number)')
	
	# Parse all command line arguments	
	args = parser.parse_args()

	# Load a toto class instance 
        if args.t is not None:
                td = PyTODO(fname=args.t[0])
	if args.t is None:	
		td = PyTODO()
	# Update the the todo class instance 
	if args.p is not None:
		td.add_project(args.p[0])
	if args.f is not None:
                td.del_project(args.f[0])
	if args.l is not None:
                td.print_project(args.l[0])
	if args.la is not None:
                td.print_all_projects()
	if args.a is not None: 
		td.add_task(args.a[0],' '.join(args.a[1:-2]),int(args.a[-2]),args.a[-1])
	if args.d is not None: 
		td.del_task(args.d[0],int(args.d[1]))

if __name__ == "__main__":

	todo_argparser()
