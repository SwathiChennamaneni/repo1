import os  
source=(raw_input('Enter a source path'))
def fileop(source):
    if os.path.exists(source):
        des=raw_input('Enter a des path')
        if os.path.exists(des):
            print "File already existS"
            x=raw_input("do you want to proceed or enter new destination file name or want to quit(proceed,new,quit):")
            if x.lower()=='proceed':
                f=open(source)
                f1=open(des, 'a')
                for line in f.readlines():
                    f1.write(line)
                f1.close()
                f.close()
                print "Content copied to des file:"
            elif x.lower()=='new':
                des=raw_input('Enter a new des path')
                f=open(source)
                f1 = open(des, 'a')
                for line in f.readlines():
                    f1.write(line)
                    f.close()
                print "Content copied to des file:"
            else:
                print "User quit from process"
        else:
           f=open(source)
           f1=open(des, 'a')
           for line in f.readlines():
               f1.write(line)
           f1.close()
           f.close()
           print "Content copied to des file:"
           
    else:
        print "file doesnot exit:"
        x=raw_input('do you want enter a new file or quit the program(Yes/quit)')
        if x.lower()=='yes':
            source=raw_input('Enter a new source path')
            fileop(source)
        else:
            print "user want to quit the process"
fileop(source)
