---
title: KDD 2018 - Hands-on Tutorial on Higher-Order Data Analytics
permalink: /setup
---

# Using git to obtain tutorial material

While you can manually download all necessary [`code`](https://github.com/IngoScholtes/kdd2018-tutorial/tree/master/code) and [`data`](https://github.com/IngoScholtes/kdd2018-tutorial/tree/master/code) files from our [gitHub repository](https://github.com/IngoScholtes/kdd2018-tutorial), we strongly recommend to clone this repository with `git` to obtain a local, sychronised copy of all material. Assuming you have a working `git` installation, you can simply do this by executing the following command in the terminal:

`git clone https://github.com/IngoScholtes/kdd2018-tutorial`

If you don't have `git` installed already, here you can find information on [how to set up git](https://help.github.com/articles/set-up-git/).

Prior to the start of the first tutorial session, we will add skeleton `python` files to the [`code` directory](https://github.com/IngoScholtes/kdd2018-tutorial/tree/master/code) of the repository. We will complete the code in these skeleton files together throughout the hands-on coding sessions. At specific *sync points*, we will push the current solution to our `gitHub` repository. You can thus simply execute the terminal command

```
git pull
```

in the directory of your local copy to receive a *sample solution* that is growing as the hands-on tutorial moves forward. If you are using Visual Studio Code (see below) things are even easier: Just click the **sync** symbol in the status bar to update the current sample solution shown on the tutor's screen! This will allow you to quickly correct any potential errors.

# Installing python 3.X

To complete the hands-on exercises, you will need a working `python 3.x` environment running on an operating system of your choice. For Windows, MacOS, and Linux users we recommend [Anaconda 5.2](https://www.anaconda.com/download/) distribution, an OpenSource `python` 3.6 distribution that comes pre-configured for data science and machine learning tasks.

The only additional package that you may need for this tutorial is the package [markdown](https://pypi.org/project/Markdown/). We use it to produce nicely formatted output with the python skeleton files. You can just install it by typing: 

```
pip install markdown
```

# Installing Visual Studio Code

To complete the exercises, we highly recommend using the development environment [Visual Studio Code](https://code.visualstudio.com/Download), a platform-independent Open Source code editor available for Windows, MacOS, and Linux. Just download the installation file and run the setup. Once the installation has completed, run Visual Studio Code either by clicking the icon or by typing `code` in the terminal.

To conveniently work with `python` and `jupyter` notebooks in Visual Studio Code, we need two extensions, which you can install free of charge directly via Visual Studio Code's integrated extension manager. We specifically need the official [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension, which adds `python` code editing, debugging, and linting functionality. We further need the [Jupyter](https://marketplace.visualstudio.com/items?itemName=donjayamanne.jupyter) extension, which provides a convenient interface to the `jupyter` notebook server automatically installed by `Anaconda 5.2`.

To install these two extensions, click the "module" icon in the bottom of the left menu bar or press `Ctrl+Shift+X`. This will bring up the Extensions window. Type `python` and click the top-most search result [Python 2018.7.1](https://marketplace.visualstudio.com/items?itemName=ms-python.python). In the window on the right, click install. Repeat this procedure with the jupyter extension, i.e. search for `jupyter`, click the top-most result [Jupyter 1.1.4](https://marketplace.visualstudio.com/items?itemName=donjayamanne.jupyter) by user Don Jayamanne and install the extension. A restart of Visual Studio Code completes the installation.

Once the installation is finished, open Visual Studio Code, click `File -> Open Folder` and navigate to your local copy of the cloned github repository. In the *Explorer* panel (the files symbol in the left bar) you can then find the notebook files that you need to complete the tutorial.

Conveniently, Visual Studio Code comes with integrated support for `git`. This means you can fetch the current, growing sample solution simply by navigating to the *Source Control* panel (the fork symbol in the left bar). In the *...* menu extension you just have to click *Pull*.

# Installing higher-order data analytics packages for python

To apply higher-order data analytics to real data, we need to set up additional ``python`` packages.

Sessions 1 and 2 will introduce [pathpy](http://www.pathpy.net), an OpenSource `python` package providing higher-order network analysis and visualisation tools for sequence, path, and temporal network data.

Sessions 4 and 5 will introduce [InfoMap](http://www.mapequation.org), an OpenSource package that can be used to reveal overlapping modular patterns in higher-order network flows through complex systems. In the following, we explain how you can set up these two packages:

## Setting up pathpy

`pathpy` is pure python code. It has no platform-specific dependencies and thus work on all platforms. It builds on `numpy` and `scipy` which come preinstalled in the Anaconda 5.2 environment. Assuming that a `python 3.x` environment has been successfully installed as described above, the latest version of `pathpy` can be installed via the [python package index pypi](https://pypi.org/). For this, you just need to open a terminal window of your operating system. Make sure that you have a `python` 3.x environment properly set up. Then run the command:

```
pip install pathpy2
```

Unfortunately, the `pypi` name `pathpy` has been name squatted after a previous version of `pathpy` had been released to the pypi test servers. While we are working to resolve this issue, we will have to use the package `pathpy2`. So make sure that you install the pypi package `pathpy2` rather than the empty (spam) package `pathpy`.

## Setting up InfoMap

Infomap is written in C++ but inludes a python interface. The easiest way to install it is via [PyPI](https://pypi.org/project/infomap/):

```
pip install infomap
```

For more information about installation and usage, see [www.mapequation.org/code.html](http://www.mapequation.org/code.html).


### Verifying your environment

Now that we have installed all necessary tools and packages, let us verify that our environment is set up properly. 

For this, you can either create a new file in Visual Studio Code and copy the following code:

```
#%%  
import pathpy as pp
paths = pp.Paths()
paths.add_path('a,b,c')
#%%
print(paths)
```

Or you can simply open your local copy of the tutorial repository in Visual Studio Code as described above. In the `code` directory, you will find the file `0_test_environment.py`, which contains the code above.

If the `python` extension of Visual Studio Code has been installed correctly, you should see the `python` code properly highlighted and colored. If the `jupyter` extension has been set up properly, two code lenses `Run cell` will appear above the `#%%` tags. These tags mark the start of a cell in a `jupyter` notebook that we can execute directly fron within Visual Studio Code.

Click the top-most `Run cell` code lens. A menu will appear, asking you whether to start a new notebook or whether to select an existing `jupyter` notebook server. Select `Start a new Notebook` and wait for the status line `Python 3 Kernel (idle)` to appear in Visual Studio Code's status bar. Now click the second `Run cell` code lens. A new window should pop up that shows the output of your code, in our example a list frequencies of paths of different lengths.

If you see this output, all is set up properly, and you are all set to complete the first two sessions of the hands-on tutorial.
