#!/usr/bin/python
import sys
import os
import zipfile
import tempfile
import shutil

from os import listdir
from os.path import isfile, join, basename

if (len(sys.argv) < 4):
    print("Invalid usage at least two files are expected\nusage: concat.py <FILE_1> <FILE_2> ... <OUTPUT_NAME>")
    sys.exit(0)

# intial variables, creating temporary dir and saving output name
temp_dir = tempfile.mkdtemp()
outputName = sys.argv[len(sys.argv) -1]
currentDirectory = os.path.dirname(os.path.abspath(__file__))
common_extension = None # will save the extension of the output file

try:
    # running over all of the arguments and extracting
    for i in range(1, len(sys.argv)-1):
        if (os.path.isfile(sys.argv[i])):
            # getting file extension and checking it's validity
            extension = os.path.splitext(sys.argv[i])[1]
            if (extension == ".zip"):
                # opening zip file
                zip_ref = zipfile.ZipFile(sys.argv[i], 'r')
                print("Extracting ",  sys.argv[i])
                # getting zip file members 
                members = zip_ref.namelist()
                #print("Extracted: " + members)
                zip_ref.extractall(temp_dir, members)
                zip_ref.close()
            else:
                print("Invalid file "+  sys.argv[i] +  " skipping")
        else:
            print("File ",  sys.argv[i],  " doesn't exist")
    
    # running over all of the files in the temp dir and concatenating files saving the in the original directory
    files = [f for f in listdir(temp_dir) if isfile(join(temp_dir, f))]
    # getting the extension
    common_extension =  os.path.splitext(temp_dir+"/"+ files[0])[1]
    with open(temp_dir+"/"+ outputName + common_extension, 'wb') as outfile:
        for filename in files:
            with open(temp_dir+"/"+ filename, 'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)
    
    #compressing output file
    zout = zipfile.ZipFile(outputName + ".zip", "w", zipfile.ZIP_DEFLATED) 
    zout.write(temp_dir+"/"+ outputName + common_extension,  basename(temp_dir+"/"+ temp_dir+"/"+ outputName + common_extension))
    zout.close()
# deleting temporary dir finally
finally:
    shutil.rmtree(temp_dir)
        
    

