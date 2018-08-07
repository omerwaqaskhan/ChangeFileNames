import Constants
import os
import sys

def change_file_names():

    if os.path.isdir(Constants.FOLDER_PATH):

        # get list of the files in folder
        list_of_files = os.listdir(Constants.FOLDER_PATH)

        for i, file in enumerate(list_of_files):
            # to get the name and extension
            name, ext = os.path.splitext(file)

            # change the name of the file and keep extension
            os.rename(Constants.FOLDER_PATH + '/' + file,
                      Constants.FOLDER_PATH + '/' + Constants.FILES_NAME + str(i + 1) + ext)
    else:
        sys.exit('Directory/Folder does not exist. Please checkt the path in Constants.py')


if __name__ == '__main__':

    try:
        # call method to change the file names
        change_file_names()
    except Exception as ex:
        print('Error: ' + ex)