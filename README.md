# iPythonBluemix

A simple starter app to get an iPython framework up and running on Bluemix. 

Use this app to deploy an iPython framework on Bluemix. The steps:

1.    Deploy to Bluemix `insert Bluemix Deploy button here`
2.    Click the app's URL. You are taken to the iPython login page. 
3.    Click __Log in__ without typing any password. The iPython framwork opens. Open the `hello_world.ipynb` file and run it. You should see output similar to the following image: `insert image here`

## Files and folders

-    static
    - hello.txt: A file that is used by the HelloWorld script (further down this list).
-    License.txt: Contains placeholder text that you replace with the license that you distribute your app with.
-    Procfile: Contains the command that tells Bluemix which file to launch when the app is opened. At the moment, you specify that the iPython framewrk should be the app launchpoint.
-    README.md: The file that you are reading at this moment.
-    manifest.yml: A file that tells Bluemix a bit more about the app.
-    requirements.txt: A file for listing the Python libraries that you need for your app code, with each library on a new line. At the moment, the only library you need is iPython. 
-    hello_world.ipynb: A simple HelloWorld script to test your deployment with.
