# About
This repository contains all the source code and an example problem to perform optimization using the DOT optimizer.  This is a commercially available gradient-based optimizer from [VR&D](http://www.vrand.com).

# Information
This project was setup to work for both Linux and Windows environments.  The corresponding DOT library is required and a few environment variables should be set when using the wrapper.

# Requirements
- The DOT optimizer itself (commercially available form [VR&D](http://www.vrand.com)).  A Python wrapper for DOT is provided that will allow the user to call the DOT shared library from Python.  Because DOT is a commercial optimizer, a license is required to use it.
- [NumPy](http://www.numpy.org/) Python library


# File description
| File        | Description  |
| ------------- |-------------|
| [dot.py](https://github.com/MODRG/DOTWrapper/blob/master/dot.py)  | The Python wrapper for DOT |
| [dot.pdf](https://github.com/MODRG/DOTWrapper/blob/master/dot.pdf) | The DOT manual |
| [box_example.py](https://github.com/MODRG/DOTWrapper/blob/master/box_example.py) | The first example problem from the DOT manual, using the provided wrapper |

# Getting started
Before running the code, please make sure that you have DOT installed on your computer.  If you do not have DOT installed, you should get hold of the VisualDOC installation from VR&D.  DOT is installed from within the VisualDOC installation.  It can be installed with VisualDOC, or you can select to only install DOT.  Please make sure to use 64-bit software throughout (this includes a 64-bit Python with the 64-bit DOT shared library).  However, the wrapper should also work if you use 32-bit applications throughout.

1. Set the VRAND_AUT environment variable to point to the VR&D license file and the LD_LIBRARY_PATH environment variable to point to the location of your DOT shared library.  For example, on Linux:
```
export VRAND_AUT=/opt/vrand/licenses/vrand.lic
export LD_LIBRARY_PATH=/opt/vrand/dot6.0
```
On Windows, you need to define a new environment variable for VRAND_AUT and add the path to your DOT shared library (.dll) to your current PATH environment variable.  It is a good idea to add this to the end of your current PATH environment variable. An in-depth guide for windows users is given further below.


2. Clone this library (command line info for Linux are provided below)
```
git clone https://github.com/MODRG/DOTWrapper.git
```

3. Change to the DOTWrapper folder
```
cd DOTWrapper
```

4. Run the example
```
python box_example.py
```

5. You should now be ready to use DOT in any of your Python projects


# Setting up DOT in Windows
Here is a step by sep Procedure for installing and setting up Dot on windows. If none of the steps below succeed, it may be that your python environment is the problem. The section after this one has some steps to help with this.

    1. Get the install files from the Visual doc Folder on the University ftp server.
    2. Accept the license agreement.
    3. Select you desired install. (this step-by-step guide used the 'typical' option)
    4. Select your desired destination folder, or just use the default.
    5. Finish the installation.

There are three different methods for linking python with dot. Here are the three different methods.The first method is recommended. But does not always work.

## Method 1

1. Place the dot shared library (.dll) in your system path.
```
The path should be (depending on what you used for step 4. above) --> C:\Program Files (x86)\vrand\dot6.0\Win64
```
To place the dot shared library in your path you need to take the following steps.
```
1. Open start menu and type **environment**. Then click the option to: **Edit the system environment variables**.
2. In the window that opens, click **Environment Variables** near the bottom of the the page.
3. In the System variables section, scroll to find *PATH* and click on it.
4. Click Edit.. just below the System variables section.
5. On thr right hand side of the popup click New.
6. Paste the path (as found previously.) in this new entry.
7. Click Ok.
```
## Method 2

Copy the dll files into your python environment.
```
The dll files are located at: C:\Program Files (x86)\vrand\dot6.0\Win64
```
To find your python environment location
```
1. Open the command prompt or anaconda prompt (if using conda environment)
2. type python -> press enter.
3. type import sys -> press enter.
4. type sys.path -> press enter.
5. In the text that shows up look for the DLLs file path. 
6. Copy the dll files into the environment dll location.
7. To close python in the command prompt.
    type exit() -> press enter.
```

## Method 3

If both of the above steps do not work, you can hardcode the dll file location into your python code. (Thanks to SB Chung for figuring this out)
```
1. Find where dot.dll is located on your pc. It should be something similar to:  C:\\Program Files (x86)\vrand\dot6.0\Win64\DOT.dll
2. Open the dot.py file and locate the line containing: self.dotlib = ct.windll.LoadLibrary("DOT.dll")
3. Replace --> ("DOT.dll"), with --> (r"C:\Program Files (x86)\vrand\\dot6.0\Win64\DOT.dll") or the equivalent on your PC.
```

# Windows Environments (python)

There are multiple different options for setting up a python environment. However, after a lot of struggling we have concluded that the simplest method is to use [Anaconda](https://www.anaconda.com/products/distribution). How to setup Anaconda is provided below. [Miniconda](https://docs.conda.io/en/latest/miniconda.html#miniconda) is an alternative, however, it has given problems with DOT in the past.

1. Download the install files.

    * The install files can be found at the [Anaconda Website](https://www.anaconda.com/products/distribution)
    * If you need a specific version it can be found at [This website](https://repo.anaconda.com/archive/)


2. Install Anaconda.
3. Open an anaconda prompt from: Start --> Anaconda Powershell Prompt.


You can now run your DOT optimization scripts in this terminal. (or in your editor of choice, such as [VSCode](https://code.visualstudio.com/))



# Authors
- Gerhard Venter - First publication 21 August 2019
- Philip Ligthart - Oct 2022
