"support has stopped at this moment"

from subprocess import Popen, PIPE
scan_command = ['sudo','iwlist',"wlo1",'scan']
scan_process = Popen(scan_command, stdout=PIPE, stderr=PIPE)
(raw_output, raw_error) = scan_process.communicate() 
print(raw_output)