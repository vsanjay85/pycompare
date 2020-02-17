# PyCompare
## Python-based image similarity calculator

Code in this repo helps calculate a similarity score of two images.

The algorithm is based on MSE (Mean Squared Error) and a part of the Python code was obtained from this [post](https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/).

TravisCI builds the python code into two executables; one for MacOS and another one for Windows; and uploads it to this Github repo under 'Releases' [here](https://github.com/vsanjay85/pycompare/releases).

## Running this program 
Download an executable for your operating system (MacOS or Windows) from the [releases](https://github.com/vsanjay85/pycompare/releases) page. 

#### Requirements 

In the same folder populate a CSV file with two columns:

 - Column#1 must contain an absolute path to a source image. 
 - Column#2 must contain the absolute path to a second image to compare the first against.

Path must be compatible with the OS. Windows paths are of style: `C:/Users/<-username->/Documents/pycompare/image1.png`. MacOS paths are your typical Unix-style paths: `/Users/<-username->Library/Documents/pycompare/image1.png`

#### Limitations
The program doesn't yet accept files of GIF and TIFF formats due to opencv-python's limitations with licensing. This will be addressed in a future version.

#### Execute
Execute the program by double-clicking on the executable file. You will first be presented with a help dialog b

If the program runs successfully, you will be presented with a window citing so, and a file named `processed_images.csv` will be placed in the same folder where the executable was placed.

This file will contain four columns:
 - Column1 and Column2 will be the same as the source CSV.
 - Column3 holds the similarity score of the two source and target images. A score of '0' indicates 100% similar images.
 - Column4 holds the time the program took to calculate the score, in seconds.

## Maintainer
#### How to use this repo

 - Install Python 3.7 or up
 - Create a [virtualenv](https://docs.python.org/3.7/library/venv.html), ensuring the venv is based on python 3.7
 - Activate the virtualenv
 - Clone this repo
 - Install the required pip packages by running: `pip3 install -r requirements.txt`
 - Create a new branch `git checkout -b <branch-name>`
 - Make your modifications to the code
 - Test the functioning of the code by running: `python comparator.py`. Code will use the sample `images.csv` and images from the `images` folder. Python works with both `/` and `\` path separators without issues.
 - Once tested and satisfied, push your changes to your branch `git push`
