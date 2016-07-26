from __future__ import print_function
import pysftp
import time
import sys



def uploadVideoSFTP(filename, **kwargs):
    '''
    Author: Fu-Chun Hsu
    This method requires a filename and the setting of the SFTP,
    includes IP, username, and password:
    Usage: uploadVideoSFTP(filename, kwargs)
    kwargs: dict:
    {'ip': your_ip, 'username': your_usename,
    'password': your_pwd, 'home': your_home}
    '''
    import pysftp
    try:
        ip = kwargs['ip']
        username = kwargs['username']
        password = kwargs['password']
        home_dir = kwargs['home']

    except:
        raise KeyError('Parameters missing...')
        return False


    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None    
        

    with pysftp.Connection(host=ip, username=username, password=password, cnopts=cnopts) as sftp:

        if not sftp.isdir(home_dir):
            sftp.mkdir(home_dir)

        sftp.cwd(home_dir)
        
        if sftp.exists(filename):
            print('Overwritting the file....')
        else:
            print('New file, uploading start')

        sftp.put(filename, callback=printTotals)

        if sftp.exists(filename):
            return True
        else:
            return False

def printTotals(transferred, toBeTransferred): 
    text = 'Transferred: ' + str(transferred) + ' Out of: ' + str(toBeTransferred)
    
    print(text)
    
    #print "Transferred: {0}\tOut of: {1}".format(transferred, toBeTransferred)
   
