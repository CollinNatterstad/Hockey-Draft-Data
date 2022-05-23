def main():
    import json
    import os
    #function takes in a .json file reads each item 
    def take_and_convert():
        directory_list = os.listdir(r'D:\Coding Projects\Hockey Stats\DraftYear.json')

        for files in directory_list:
            #objective: take in intial file. Read values and convert the data type where necessary.
            jsonfilepath = (r'D:\Coding Projects\Hockey Stats\DraftYear.json\\')
            readpath = jsonfilepath+files
            

    take_and_convert()
if __name__ == '__main__':
    main()