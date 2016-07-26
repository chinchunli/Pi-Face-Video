import pysftp
import time


class  pysftp:
    def __init__(self):
        pysftp.Connection("1.34.62.109", username="None", private_key=None, password="None", port=22, private_key_pass=None, ciphers=None, log=False)

        def cwd(self):
            self.tp.cwd('/home/guest/Desktop/Facevideo')
            self.Print(sftp.getcwd())  # is equivalent to sftp.chdir('public')
            return

        # copy myfile, to the current working directory on the server, preserving modification time
        def put(self):
            self.sftp.put('myfile', preserve_mtime=True)
            self.sftp.pwd
            return

        def close(sftp):
            sftp.close()


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
    try:
        ip = kwargs['ip']
        username = kwargs['username']
        password = kwargs['password']
        home_dir = kwargs['home']

    except:
        raise KeyError('Parameters missing...')
        return False

    with pysftp.Connection(host=ip, username=username, password=password) as sftp:

        if not sftp.isdir(home_dir):
            sftp.mkdir(home_dir)

        sftp.cwd(home_dir)
        
        if sftp.exists(filename):
            print('Overwritting the file....')

        sftp.put(filename)

        if sftp.exists(filename):
            return True
        else:
            return False