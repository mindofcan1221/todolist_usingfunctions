# a simple to do list program
#this uses a single file to register the tasks and their status
#it uses a dictionary data structure to do that
from datetime import date
from todolist_files import task_list,status_list
import ast
tasks = {}
current_date = date.today()
#filename1 = 'tasks.txt'
#filename2='status.txt'
filename = 'todolist.txt'
print("#### A simple to do list program.###")
print("####1.to enter the list of your tasks.###")
print("####2.to enter the status of each task.###")
mychoice = "Enter your choice"
choice = int(input(mychoice+">"))

#list your daily tasks
#use the function task_list() to take tasks and write them on a file

if choice ==1:
    task_list(filename,tasks)

#list the status of your tasks     
elif choice ==2:
   status_list(filename)
#if other values are entered   
else:
    print("Enter the right choice")
