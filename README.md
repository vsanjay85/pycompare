# PyCompare
## Python-based image similarity calculator
Code in this repo helps calculate a similarity score of two images.

The algorithm is based on MSE ([Mean Squared Error](https://en.wikipedia.org/wiki/Mean_squared_error)) and a part of the Python code was obtained from this [post](https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/).

TravisCI [builds the python code](https://travis-ci.com/vsanjay85/pycompare) into two executables; one for MacOS and another one for Windows; and uploads it to this Github repo under 'Releases' [here](https://github.com/vsanjay85/pycompare/releases).

#### Considerations 
##### How do you know if your code works?
- `pytest` unit tests are written in `comparator_test.py`. Running `pytest` from the command line will test basic functionality. It wasn't possible to integrate this into TravisCI because of [an issue with opencv-python](https://travis-ci.community/t/python-and-opencv-dll-load-fails-every-time/4431/11) on Windows.
- You may also run `python comparator.py` to test functionality before committing changes. A sample `images.csv` and test images are provided `images` folder.

##### How are you going to teach Bjorn how to use the program? 
- A help dialog pops up every time the program is run. ![help-dialog](/help_images/help_dialog.png)
- When the program finishes successfully, another dialog pops up letting the user know so. ![finished-dialog](/help_images/finished_dialog.png)

##### How are you ensuring Bjorn gets the latest version of your application?
- A new version is created everytime the build succeeds. A version info dialog pops up if a newer version of the program is available on Github. ![version-dialog](/help_images/version_info.png). Version info is bundled into the executable at build time by 'pyinstaller' and is checked on program startup.

##### Your manager Jeanie is assigning you to a different task and is making Ferris the maintainer of your application. How do you make sure he succeeds?
- The #Maintainer section of this README contains setup and dev instructions for a future maintainer.

## Running this program 
Download an executable for your operating system (MacOS or Windows) from the [releases](https://github.com/vsanjay85/pycompare/releases) page. 

#### Requirements 

In the same folder populate a CSV file with two columns:

 - Column#1 must contain an absolute path to a source image. 
 - Column#2 must contain the absolute path to a second image to compare the first against.

Path must be compatible with the OS. Windows paths are of style: `C:/Users/<-username->/Documents/pycompare/image1.png`. MacOS paths are your typical Unix-style paths: `/Users/<-username->Library/Documents/pycompare/image1.png`

#### Limitations and future improvements
- The program doesn't yet accept files of GIF and TIFF formats due to opencv-python's limitations with licensing. This will be addressed in a future version.
- We're unable to run pytests [because of a Windows-TravisCI bug](https://github.com/vsanjay85/pycompare#running-this-program). Hopefully, a fix is available in the future.
- A new version of the program is created on every successful TravisCI build, regardless of whether there's a change in the Python code. This must be fixed to only run on code changes.

#### Execute
Execute the program by double-clicking on the executable file. You will first be presented with a help dialog box. See: https://github.com/vsanjay85/pycompare#how-are-you-going-to-teach-bjorn-how-to-use-the-program

If the program runs successfully, you will be presented with a window citing so, and a file named `processed_images.csv` will be placed in the same folder where the executable was placed.

This file will contain four columns:
 - Column1 and Column2 will be the same as the source CSV.
 - Column3 holds the similarity score of the two source and target images. A score of '0' indicates 100% similar images.
 - Column4 holds the time the program took to calculate the score, in seconds.

## Maintainer
#### How to use this repo

 - Install Python 3.7 or up
 - Open a terminal (Unix) or powershell (Windows) window
 - Create a [virtualenv](https://docs.python.org/3.7/library/venv.html), ensuring the venv is based on python 3.7
 - Activate the virtualenv
 - Clone this repo
 - Install the required pip packages by running: `pip3 install -r requirements.txt`
 - Create a new branch `git checkout -b <branch-name>`
 - Make your modifications to the code
 - Test the functioning of the code by running: `python comparator.py`. Code will use the sample `images.csv` and images from the `images` folder. Python works with both `/` and `\` path separators without issues.
 - If you'd prefer creating an executable to test, run the appropriate `pyinstaller` command from file `.travis.yml`. This creates an executable in the `dist` folder. 
 - Once tested and satisfied, push your changes to your branch `git push`.

#### Github-Releases token creation
A token is used to push the build artifacts into Github/Releases. This token is generated by using the `travis` CLI which is installed by running 
`gem install travis`
Then you run:
`travis login --pro`
`travis setup releases --com`
which automatically creates, encrypts, and adds the token to .travis.yml. 
