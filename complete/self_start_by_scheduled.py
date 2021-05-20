import win32com.client
from datetime import datetime, timedelta
import pathlib
from win10toast import ToastNotifier
import os
import time


def startSchedule(min):
    task_name = "PBI_VIEWER"

    computer_name = "" #leave all blank for current computer, current user
    computer_username = ""
    computer_userdomain = ""
    computer_password = ""
    action_id = task_name #arbitrary action ID
    # print(str(pathlib.Path(__file__).parent.absolute()) + '\\' + __file__)

    action_path = r"c:\Users\Lucy\anaconda3\python.exe" #executable path (could be python.exe)
    #action_path = r"python.exe" #executable path (could be python.exe)
    action_arguments = str(pathlib.Path(__file__).parent.absolute()) +  '\\temp.py'#arguments (could be something.py)

    action_workdir = str(pathlib.Path(__file__).parent.absolute()) +"\\" #working directory for action executable
    author = "Lucy" #so that end users know who you are
    description = "testing task" #so that end users can identify the task
    task_id = task_name
    # task_hidden = False #set this to True to hide the task in the interface
    # username = ""
    # password = ""
    run_flags = "TASK_RUN_NO_FLAGS" #see dict below, use in combo with username/password



    #define constants
    TASK_TRIGGER_DAILY = 2
    # TASK_CREATE = 2
    TASK_CREATE_OR_UPDATE = 6
    TASK_ACTION_EXEC = 0
    # IID_ITask = "{148BD524-A2AB-11CE-B11F-00AA00530503}"
    RUNFLAGSENUM = {
        "TASK_RUN_NO_FLAGS"              : 0,
        "TASK_RUN_AS_SELF"               : 1,
        "TASK_RUN_IGNORE_CONSTRAINTS"    : 2,
        "TASK_RUN_USE_SESSION_ID"        : 4,
        "TASK_RUN_USER_SID"              : 8 
    }
    #connect to the scheduler (Vista/Server 2008 and above only)
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect(computer_name or None, computer_username or None, computer_userdomain or None, computer_password or None)
    rootFolder = scheduler.GetFolder("\\")

    taskDef = scheduler.NewTask(0)
    colTriggers = taskDef.Triggers
    trigger = colTriggers.Create(TASK_TRIGGER_DAILY)
    trigger.DaysInterval = 365
    trigger.StartBoundary = (datetime.now() + timedelta(minutes = min)).isoformat()
    trigger.Enabled = True

    colActions = taskDef.Actions
    action = colActions.Create(TASK_ACTION_EXEC)
    action.ID = action_id
    action.Path = action_path
    action.WorkingDirectory = action_workdir
    action.Arguments = action_arguments

    info = taskDef.RegistrationInfo
    info.Author = author
    info.Description = description

    #register the task (create or update, just keep the task name the same)
    rootFolder.RegisterTaskDefinition(task_id, taskDef, TASK_CREATE_OR_UPDATE, "", "", RUNFLAGSENUM[run_flags] ) #username, password
    return


def main():
    deltamin = 15
    # Check database is loaded
    # 
    # with open('1.txt', 'r') as reader:
    #     # Read & print the entire file
    #     num = int(reader.read())
    #     num += 1
    # reader.close()
    if True:
        # schedule_id = num % 2
        startSchedule(deltamin)
        # with open('1.txt', 'w') as writer:
        # # Read & print the entire file
        #     writer.write(str(num))
        # writer.close()
    else:
        # Here, add the first file
        os.system('python 1.py')

if __name__ == '__main__':
	main()