import subprocess as sp
ret = sp.getoutput('date')       # standard output string
ret = sp.check_output('date')    # output b''
ret = sp.getstatusoutput('date') # get (0, 'Sun 19 Nov 14:24:03 UTC 2017')
ret = sp.call('date')            # get exit status and running 
ret = sp.call('date -u',shell='True')            # add parameters
ret = sp.call(['date','-u'])
print(ret)

