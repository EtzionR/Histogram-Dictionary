# Histogram-Dictionary
Produces a histogram dictionary, in which each bin specifies the frequency of its occurrences.

## introduction
The code receives an iterable object consisting of numbers, and produces for it a computer dictionary the frequency of occurrences for each bin. 
If a **"name"** string variable is also inserted, then the code will also generate a plot (instructions below).

![picture](https://github.com/EtzionData/Histogram-Dictionary/blob/master/Output/normal%20distribution%20histogram%20bin%3D4.png)

## libraries
The code uses the following libraries in Python:

**matplotlib**

**pandas** (only in the implementation.py code)

## application
An application of the code is attached to this page under the name: 

**"implementation.py"** 
the examples outputs are also attached here.

## Using the code
To use this code, you just need to import it as follows:
``` sh
# import
from histogram_dct import hd

# define variables
lst = [11, 17.6, 3.4, ... , 9.7, 21.3, 6.9]
bin = 5             # bin size (number) 
name= "my_plot"     # you not need to add ".png"

# application
hd.histogram_dct(lst, bin, name)

```

When the variables displayed are:

**lst:** iterable object composed by numbers

**bin:** bin size

**name:** string which represents the filename of the plot you want to save
