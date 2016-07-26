import pysftp

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