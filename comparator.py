import csv
import time
import cv2
import requests
import github_repo
import json
import PySimpleGUI as sg
import numpy as np

#from PIL import Image as image

def version_check():
    with open('version.txt', 'r') as versionfile:
        for line in versionfile:
            version=line
        git_api_url="https://api.github.com/repos/"+github_repo.fullname()+"/releases/latest"
        response=requests.get(url=git_api_url)
        release_ver=response.json()['tag_name']
        if release_ver > version:
            github_url=github_repo.remote.url()

            layout = [  [sg.Text("You're running an older version of this program")],
                        [sg.Text("Download the latest version from: "+github_url)],
                        [sg.Button("OK")] ]

            # Create the Window
            window = sg.Window('Version Info', layout)
            # Event Loop to process "events" and get the "values" of the inputs
            while True:
                event, values = window.read()
                if event in (None, 'OK'):   # if user closes window or clicks cancel
                    break
                print('You entered ', values[0])

            window.close()                



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

        csv_writer(processed_list)

def mse(image_a, image_b):
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

if __name__ == "__main__":
    version_check()
    comparator()
    

