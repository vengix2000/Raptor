import os
from cryptography.fernet import Fernet
import argparse


class node:
    def __init__(self, file, n=None):
        self.file = file
        self.next = n


class Raptor:
    def __init__(self):
        self.root = None
        self.display = self.banner()
        self.print()
        self.path = None





    def print(self):
        print(self.display)



    def add_file(self, file):
        if self.root is None:
            new_node = node(file, self.root)
            self.root = new_node
        else:
            new_node = node(file, self.root)
            self.root = new_node

    def print_files(self):
        temp_node = self.root
        if self.root is None:
            print("Directory is empty")
        else:
            while temp_node is not None:
                print('File name: ' + str(temp_node.file))
                temp_node = temp_node.next

    def check_file(self, file):
        if os.path.isfile(file):
            return True
        else:
            return False


    def genrate_key(self,k_name):
       if os.path.exists(k_name):
           pass
       else:
            key = Fernet.generate_key()
            with open(k_name,'wb') as f:
                f.write(key)


    def load_key(self,k_name):
        with open(k_name,'rb') as f:
            return f.read()


    def Encrypt(self,k_name):
        self.genrate_key(k_name)
        key = self.load_key(k_name)
        temp_node = self.root
        fernet = Fernet(key)

        while temp_node is not None:
            if self.check_file(temp_node.file) and temp_node.file != 'main.py' and temp_node.file != k_name:
                with open(temp_node.file, 'rb') as f:
                    orig_file = f.read()
                encrpted = fernet.encrypt(orig_file)
                with open(temp_node.file, 'wb') as f:
                    f.write(encrpted)
            else:
                pass
            temp_node = temp_node.next

    def decrypt(self,k_name):
          dec_key = self.load_key(k_name)
          temp_node = self.root
          fernet = Fernet(dec_key)

          while temp_node is not None:
              if self.check_file(temp_node.file) and temp_node.file != 'main.py' and temp_node.file != k_name:
                  with open(temp_node.file,'rb') as f:
                      encry_file = f.read()

                  decrypted = fernet.decrypt(encry_file)

                  with open(temp_node.file,'wb') as f:
                      f.write(decrypted)
              else:
                  pass

              temp_node = temp_node.next
    def banner(self):
        Banner = '''

                   ______            _
                   | ___ \          | |
                   | |_/ /__ _ _ __ | |_ ___  _ __
                   |    // _` | '_ \| __/ _ \| '__|
                   | |\ \ (_| | |_) | || (_) | |
                   \_| \_\__,_| .__/ \__\___/|_|
                              | |
                              |_|

                   raptor v1.0
                   developed by Dhananjay Meshram
                   year 2021
                   The Encryptor you want!!!!!!!!!!!!!!!!!!!!!
                   *careful while handeling keys*
                   *Do not use same key for different Encryption*


                       '''

        return Banner
def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypts a file or whole dir")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypts a file or whole dir")
    parser.add_argument("-r", "--route", help="specifies the path")
    parser.add_argument("-k", "--key", required=True, help="specifies key file name")

    args = parser.parse_args()
    if args.encrypt and args.key and args.route:
        k_name = args.key
        raptor.path = args.route
        for files in os.listdir(raptor.path):
            raptor.add_file(raptor.path + files)
        raptor.Encrypt(k_name)

    elif args.decrypt and args.key and args.route:
        k_name = args.key
        raptor.path = args.route
        for files in os.listdir(raptor.path):
            raptor.add_file(raptor.path + files)
        try:
            raptor.decrypt(k_name)
        except:
            print("Invalid Key")
    else:
        if args.encrypt and args.key:
            k_name = args.key
            raptor.path = args.route
            for files in os.listdir():
                raptor.add_file(files)
            raptor.Encrypt(k_name)
        else:
            if args.decrypt and args.key:
                k_name = args.key
                raptor.path = args.route
                for files in os.listdir():
                    raptor.add_file(files)
                raptor.decrypt(k_name)

if __name__ == '__main__':
    raptor = Raptor()
    arg()






