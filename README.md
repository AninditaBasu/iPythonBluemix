# iPythonBluemix

A simple starter app to get an iPython framework up and running on Bluemix. 

## Installation

1.    Deploy this app to Bluemix by clicking here: [![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/AninditaBasu/iPythonBluemix # [required])
2.    Follow the onscreen directions. After the app is deployed and running, click the app's URL. You are taken to the iPython Jupyter login page. 
3.    Click __Log in__ without typing any password. The iPython framework opens. Open a new notebook, import the `hello_world.py` script, and run it. You should be asked your name and shown some lines of text.

## Files and folders

-    static
    - hello.txt: A file that is used by the HelloWorld script (further down this list).
-    License.txt: Contains placeholder text that you replace with the license that you distribute your app with.
-    Procfile: Contains the command that tells Bluemix which file to launch when the app is opened. In this file, the iPython framework is specified as the app launchpoint.
-    README.md: The file that you are reading at this moment.
-    manifest.yml: A file that tells Bluemix a bit more about the app.
-    requirements.txt: A file for listing the Python libraries that you need for your app code, with each library on a new line.
-    hello_world.py: A simple HelloWorld script to test your deployment with.
