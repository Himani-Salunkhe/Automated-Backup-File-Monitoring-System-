####################################################################################
#
#   Importing required libraries
#
####################################################################################

import sys
import os
import time
import schedule

####################################################################################
#
#   Function Name : DirectoryScanner
#   Input         : Name of Directory
#   Description   : Deleted all empty files periodically
#   Date          : 19/07/2026
#   Author        : Himani Ramesh Salunkhe
#
####################################################################################

def DirectoryScanner(DirectoryPath):
    Border = "-"*40
    timestamp = time.ctime()
    logfilename = "Marvellous%s.log"%(timestamp)    #%s for string
    logfilename = logfilename.replace(" ","_")
    logfilename = logfilename.replace(":","_")

    Ret = False

    Ret = os.path.exists(DirectoryPath)     #filter : is name present?
    if(Ret == False):
        print("Marvellous Automation Error : There is no such directory with name",DirectoryPath)
        return
    

    Ret = os.path.isdir(DirectoryPath)      #filter : is directory with that name is present?
    if(Ret == False):
        print("Marvellous Automation Error : It is not a directory with name",DirectoryPath)
        return
    

    print("LogFile gets created with name : ",logfilename)

    fobj = open(logfilename,"w")

    fobj.write(Border+"\n\n")
    fobj.write("Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")

    fobj.write("Files from the directory are : \n\n")
    fobj.write(Border+"\n")

    TotalFiles = 0
    EmptyFiles = 0

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for Fname in FileName:
            TotalFiles = TotalFiles + 1
            Fname = os.path.join(FolderName,Fname)
            fobj.write(f"{Fname} : {os.path.getsize(Fname)} bytes\n")

            if(os.path.getsize(Fname) == 0):
                EmptyFiles = EmptyFiles + 1
                os.remove(Fname)

    fobj.write(Border+"\n")                     # displying statistics
    fobj.write(f"Total files scanned : {TotalFiles}\n")
    fobj.write(f"Total Empty files formed and deleted : {EmptyFiles}\n")

    fobj.write(Border+"\n")
    fobj.write("Log file gets created at : "+timestamp)
    fobj.write("\n"+Border+"\n")
    
    fobj.close()        

####################################################################################
#
#   Function Name : Main
#   Input         : Command Line Arguments
#   Description   : It Controls the Script
#   Date          : 19/07/2026
#   Author        : Himani Ramesh Salunkhe
#
####################################################################################

def main():
    Border = "-"*80
    print(Border) #borders
    print("Marvellous Automation Script")
    print(Border)
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")

        else:    
           
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            

            while(True):    #if dont want to abort use counter like counter <=20 (example)
                schedule.run_pending()
                time.sleep(1)
                #counter = counter + 1
        
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
    

    print(Border)
    print("Thanking for using Marvellous Automation Script")
    print(Border)

####################################################################################
#
#   Starter of the automation script
#
####################################################################################

if __name__ =="__main__":
    main()













































