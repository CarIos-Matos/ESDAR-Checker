"""
This File is used to setup the needed Configurations which the user has to perform

RELATIVE_FILE_PATH: Provide the relative File Path which you want to use to for the Output File
E.g: resources/output/ or you can also use the absolute filepath C:/Users/[USERNAME]/PycharmProjects/ESDAR-Checker/resources/output/

@author Merlin von der Weide
@version 1.2.0-beta
@date 08.08.2024
"""
RELATIVE_FILE_PATH = "resources/output/"

def update_path(path):
    global RELATIVE_FILE_PATH
    RELATIVE_FILE_PATH = path
