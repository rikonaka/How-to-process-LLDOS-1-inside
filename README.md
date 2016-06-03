# How-to-process-LLDOS_1_inside
Use Introduction

## Let's talk about how to process the LLDOS_1.0_inside tcpdump file

This file is download here 
* [door](http://www.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0.html)

this page have lot of information about the LLS_DDOS data
then use some IDS to run the tcpdum file and output the alert file

I use the open source IDS Snort

and then, you can find a file name `alert`
and copy it from /var/log/snort to you Document directory

#### First run the `LLDOS_1_inside_1step.py` programs

it will output a neat data

#### Then run the `LLDOS_1_inside_2step.py` programs

it will remove some unnectessary data

#### Then run the `LLDOS_1_inside_3step.py` programs

and it will cut the times and some symbol

#### Now you can take the final dataset to the Spark use FP-Growth

#### and maybe someone want to do more things in the dataset
So, let's look up what can we do with it

#### Maybe we can choice some given IP in the dataset
#### and extract specific IP in LLS_DDOS dataset
So, use the the next programs
`extract_specific_ip.py`
Put you ip in the programs list and it will generate a file which only have ip you given
now you can do lot of things with it
![image](https://github.com/SuperSuperSuperSuper5/How-to-process-LLDOS_1_inside/blob/master/172hou20.png)
here is some pic i draw with matplotlib
![image](https://github.com/SuperSuperSuperSuper5/How-to-process-LLDOS_1_inside/blob/master/20277-2.png)
![image](https://github.com/SuperSuperSuperSuper5/How-to-process-LLDOS_1_inside/blob/master/all.png)
![image](https://github.com/SuperSuperSuperSuper5/How-to-process-LLDOS_1_inside/blob/master/all-2.png)

### So, it's so funny with it, is it?

### Now let's talk about how to process the data to draw a picture

* Fistly, you must ensure you have been install the `matplotlib` and `numpy` and `pandas`
* If not
```
sudo apt-get python-pip python-dev build-essential
```
And then
```
pip install matplotlib numpy pandas
```
Untill you do this, it far from the use of data to drawing
We still have lot of work to do with this data

#### run the `draw_1step.py` with you last step result

This step will make sure the dataset which last step output have right time label
and get the current time label

#### run the `draw_2step.py` with the output of `draw_1step.py`

This step will calculate the absolute time and replace the alert type as value
also output a file name `same_list`, and this file is the all kinds of labels

#### In here, I strongly recommended you run the `draw_2step.py` and `draw_finalstep.py` in same directory

##### Just do it

##### Beacuse the `draw_2step.py` will output a file named `same_list` and the `draw_finalstep.py` will use it

#### Then run the `draw_finalstep.py`
This code have 3 type chart, choice  one and remove the # in front of line at main()

#### But you have to be careful of time

* I use The EDT NOT EST, But the LLDOS is EST, so i minus 1 at time
* If you are EST user or some else time zone, i suggest you be care for in  time processing

#### If you have any question in my code, welcome to email me at super_big_hero@sina.com
