import os
pid = os.getpid()
path = os.getcwd()
uid = os.getuid()
gid = os.getgid()
print(pid,path,uid,gid) 