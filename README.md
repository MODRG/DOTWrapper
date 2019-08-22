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
On Windows, you need to define a new environment variable for VRAND_AUT and add the path to your DOT shared library (.dll) to your current PATH environment variable.  It is a good idea to add this to the end of your current PATH environment variable.

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

# Authors
- Gerhard Venter - First publication 21 August 2019
