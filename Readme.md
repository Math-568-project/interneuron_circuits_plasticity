# Environment setup
Here are some steps that can help you set up your environment
## Python
If you are using Python>=3.6, then it is fine, if not, please create and activate a new virtual environment with Python 3.7 via the following command:
```
conda create -n name_of_your_virtual_environment python=3.7
conda activate name_of_your_virtual_environment
```
Notice that ```name_of_your_virtual_environment``` is the name of your virtual environment.
## Dependencies
Here are several sets of dependenceis that you should install:
### brian2
Here is the installation steps that works for me, if you have problem, you can refer to the [offical installation docoument](https://brian2.readthedocs.io/en/stable/introduction/install.html) or just text me.
First install brian2 and the tool library for it
```
pip install brian2 brian2tools scipy
```
Then, brian2 also compile the code in C++ to improve the speed of simulation, thus, necessary dependencies should be installed.
```
pip install cpython
pip install --upgrade setuptools
```
Then, you have to install the compiler for c++, and the official installation document recommend you to install visual studio if you are using Windows. But I think it is the visual studio is too big, and you only use the compiler. Thus, I recommend you to install the MinGW. Here is a [good installation guidelines](https://www.ics.uci.edu/~pattis/common/handouts/mingweclipse/mingw.html), it may work. If it does not work, you can text me.


# Running
## Simulation
Currently, the code is still not very readable but runnable. I do not understand all the details of the code and I will try to improve it later.\
Notice that the code is extremely memory-hungry !!!!!\
As for running, you just run the ```main.py```\
If you prefer to run in the command line, you just run ```python main.py``` in the root directory of this project.\
## Plotting
Currently, the ```plot_Spikingmodel.py``` is runnable, but the size of figure may not be good. And I create a ```plot.ipynb``` for the plottings in the project update.