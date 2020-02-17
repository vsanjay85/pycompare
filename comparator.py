import csv
import time
import cv2
import requests
import github_repo
import json
import PySimpleGUI as sg
import numpy as np
from sys import exit

#from PIL import Image as image

def window_maker(title,layout,exit_button):
    # Create the Window
    window = sg.Window(title, layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, exit_button):   # if user closes window or clicks cancel
            exit()
        else:
            window.close()
            return
    
def help():
    text='''
    This program:
     - Reads from a CSV file.
     - Compares the images for similarity.
     - Scores them accordingly, where a score of 0 means 100% similar images.
     - Saves the results into another CSV file.

    To run this program on Windows, you will need:
    - images.csv in the same folder as this program, with two columns:
        - Column#1 must contain the full Windows-style path to a source image.
        - Column#2 must contain the full Windows-style path to a second image to compare against.

    To run this program on MacOS, you will need:
    - images.csv in the same folder as this program, with two columns:
        - Column#1 must contain the full Unix-style path to a source image.
        - Column#2 must contain the full Unix-style path to a second image to compare against.

    The program will compare the images in these columns and store the results in a file named:
    processed_images.csv
    '''

    layout = [  [sg.Text(text)],
                [sg.Button('Run Program'), sg.Button('Cancel')] ]
    window_maker('Info',layout,'Cancel')

def version_check():
    with open('version.txt', 'r') as versionfile:
        for line in versionfile:
            version=line

    git_api_url="https://api.github.com/repos/vsanjay85/pycompare/releases/latest"
    response=requests.get(url=git_api_url)
    release_ver=response.json()['tag_name']
    if release_ver > version:
        github_url="https://github.com/vsanjay85/pycompare/releases/latest"

        layout = [  [sg.Text("You're running an older version of this program")],
                    [sg.Text("Download the latest version from: "+github_url)],
                    [sg.Button("OK")] ]
        window_maker('Info',layout,'')

def comparator():
    processed_list = []
    with open('images.csv', newline='') as csvfile:
        img_reader = csv.reader(csvfile, delimiter=',')
        for row in img_reader:
            print(row[0])
            image_a = cv2.imread(row[0])
            image_b = cv2.imread(row[1])
            start = time.time()
            score = mse(image_a, image_b)
            elapsed = str(round(time.time() - start, 4))
            processed_list.append({"SourceImg":row[0], 'DestImg':row[1], 'SimilarityScore':score, 'Elapsed':elapsed})

        return processed_list

def mse(image_a, image_b):
    # From: https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/#
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((image_a.astype("float") - image_b.astype("float")) ** 2)
    err /= float(image_a.shape[0] * image_a.shape[1])
    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return str(err)

def csv_writer(processed_list):
    csv_columns = ['SourceImg', 'DestImg', 'SimilarityScore', 'Elapsed']
    with open('processed_images.csv', 'w', newline='') as csvtargetfile:
        img_writer = csv.DictWriter(csvtargetfile, fieldnames=csv_columns)
        img_writer.writeheader()
        for item in processed_list:
            img_writer.writerow(item)
    return True

if __name__ == "__main__":
    help()
    version_check()
    processed_list=comparator()
    if csv_writer(processed_list):
        text='''
        Program finished successfully.
        Results saved to 'processed_images.csv'
        '''
        layout = [  [sg.Text(text)],
                    [sg.Button('OK')] ]
        window_maker('Info',layout,'OK')