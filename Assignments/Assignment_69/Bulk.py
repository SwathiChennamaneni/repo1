"""69. Bulk file copy. 
     Take source and destination file paths from a file and copy the source file content into destination file.
     
     Maintain configuration file and put the below fields there
      Source not found: Skip the copy
      destination found: skip/replace
     maintain a remarks log. What are the files skiped from copy because no source file found.
     What are the files skip/replaced because of destination file foun in the specified path """
import sys
#sys.exit()
import os
import shutil

with open('remarks.log','a') as log:
            log.write('')
with open("files.txt") as f:
    files = f.readlines()
    for i in files[1:]:
        #print i
        j = i.split(" ")
        #print j
        source = j[0]
        x = j[1].split('\n')
        dest = x[0]
        
        #print source
        #print dest
        
        if os.path.exists(source):
            #print "yes"
            if os.path.exists(dest):
                #print "no"
                with open('config.txt','r') as conf:
                    data = conf.readlines()
                    #print data
                    print data[1]
                opt = raw_input("\nEnter[skip/replace]:")
                if opt.lower() == 'skip':
                    with open('remarks.log','a') as log:
                        log.write('File {} skipped from copy\n'.format(dest))
                    print "Skipped the Copy as user requested"
                else:
                    shutil.copy(source, dest)
                    with open('remarks.log','a') as log:
                        log.write('File {} copied because destination file found\n'.format(dest))
            else:
                with open('remarks.log','a') as log:
                        log.write('File {} skipped from copy because no destination file found\n'.format(dest))
        else:
            print "Skipped the copy as Source file not found"
            with open('config.txt','r') as conf:
                data = conf.readlines()
                print data[0]
            with open('remarks.log','a') as log:
                log.write('File {} skipped from copy because no source file found\n'.format(dest))
print "** Check Remarks Log for Remarks **"
                
