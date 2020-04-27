#!/usr/bin/env python
import glob
import os
import logging
#import path
import time

import subprocess

from datetime import datetime

LOG_FILE = '/lmshome/Sanjay/DeleteCores/logs_corefiles.log'
logging.basicConfig(filename=LOG_FILE,level=logging.DEBUG)

# logging.info('--LOG INFO--')

# Get a list of all the file paths that ends with core.* from specified directory
fileList = glob.glob('/lmshome/routings/LMSTST_**/Bin/core.*')



#To send email


os.chdir("/lmshome/Sanjay/DeleteCores/")
f1 = open("logsout.txt","a+")

print("File created")

for filePath1 in fileList:
    logging.info(str(datetime.now()))
    logging.info(filePath1)
    # os.chdir("/lmshome/Sanjay/DeleteCores/")
    # f1 = open("logsout.txt","a+")
    # f1.write("Generated Files:\n\n")
    f1.write(filePath1+"\n")
        # time.sleep(5)

f1.close()
        # os.system("chmod 777 logsout.txt")
print(os.stat("logsout.txt").st_size != 0)
if(os.stat("logsout.txt").st_size != 0):

    os.system("cat /lmshome/Sanjay/DeleteCores/logsout.txt | mail -s 'Core files got generated..' sanjay.gunagi@unisys.com")
        # cmd = "sh SendMail.sh"
        # os.system("SendMail.sh")
        # os.system(cmd)
        # shellscript = subprocess.Popen(["SendMail.sh"], stdin=subprocess.PIPE)
        # shellscript.stdin.write("yes\n")
        # shellscript.stdin.close()
        # returncode = shellscript.wait()
    print("File found, email sent.")
        # time.sleep(5)
        # os.remove(filePath)
        # time.sleep(10)
        # f1.close()
os.remove("/lmshome/Sanjay/DeleteCores/logsout.txt")


 
# Iterate over the list of filepaths & remove each file.
for filePath in fileList:
    try:
        logging.info(str(datetime.now()))
        logging.info(filePath)
        # os.chdir("/lmshome/Sanjay/DeleteCores/")
        # f1 = open("logsout.txt","a+")
        # f1.write("Generated Files:\n\n")
        # f1.write(filePath+"\n")
        # time.sleep(5)

        # f1.close()
        # os.system("chmod 777 logsout.txt")

        # os.system("cat /lmshome/Sanjay/DeleteCores/logsout.txt | mail -s 'Core files got generated..' sanjay.gunagi@unisys.com")
        # cmd = "sh SendMail.sh"
        # os.system("SendMail.sh")
        # os.system(cmd)
        # shellscript = subprocess.Popen(["SendMail.sh"], stdin=subprocess.PIPE)
        # shellscript.stdin.write("yes\n")
        # shellscript.stdin.close()
        # returncode = shellscript.wait()
        # print("File found, email sent.")
        # time.sleep(5)
        os.remove(filePath)
        # time.sleep(10)
        # f1.close()
        # os.remove("/lmshome/Sanjay/DeleteCores/logsout.txt")
    except:
        print("Error while deleting file : ", filePath)