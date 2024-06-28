# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 06:20:38 2018

@author: Balasubramaniam
"""
import subprocess
import os
import sys

 
## call date command ##
p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
 
## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
## Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.  ##
## Wait for process to terminate. The optional input argument should be a string to be sent to the child process, ##
## or None, if no data should be sent to the child.
(output, err) = p.communicate()
 
## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
print ("Command output : ", output)
print ("Command exit status/return code : ", p_status)

#res = subprocess.Popen(['ls','-al','/ahome'],stdout=subprocess.PIPE,stderr=subprocess.PIPE);
#output,error = res.communicate()

#if res.returncode:
#   #raise Exception(error)
#   print "error>>>> ",res.returncode
#else:
#   print "output>>>> ",output
 
try:
    res = subprocess.Popen(['dir','','./'],stdout=subprocess.PIPE,stderr=subprocess.PIPE);
    #res = subprocess.Popen(['xls','-al','/home'],stdout=subprocess.PIPE);
    output,error = res.communicate()
    if output:
        print ("ret> ",res.returncode)
        print ("OK> output ",output)
    if error:
        print ("ret> ",res.returncode)
        print ("Error> error ",error.strip())
#except CalledProcessError as e:
#   print "CalledError > ",e.returncode
#   print "CalledError > ",e.output
except OSError as e:
    print ("OSError > ",e.errno)
    print ("OSError > ",e.strerror)
    print ("OSError > ",e.filename)
except:
    print ("Error > ",sys.exc_info()[0])