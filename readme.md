# The Honeycomb Web

Welcome to the Honeycomb Web Project GitHub!

The documentation is on its way, and Readme is constantly getting updated.

The project is maintained/developed by stt0421-jsk, Justpumpkin, mmt-1234, and jiduck0814.

For any questions, feel free to contact: gotohell.covid19@gmail.com


## Introduction

The basic concept of the Honeycomb Web is to remake what we call "the Web" from scratch.
Nowdays, people use normal Web Browsers to load HTML/JS/CSS based webpages. 

But we thought that we could be able to remake the concept of the Web, much more securely/effectively, but also very differently.
The conclusion of this project will be a demo of the Honeycomb Web, which will require users to be fixed in a hexagon-shaped network. See below documentation for more information about the concept.

## How it works

The Honeycomb Web binds 6 network users into one group of Hexagon.
Let's call this a Hex.

Between these users inside the same Hex, they can search each other's hidden local files. 
These hidden local files consist of "HCPF" files(for more information on HCPF files, see HCPF files below) of static webpages.

![alt text](https://github.com/stt0421-jsk/honeycomb/blob/main/img/Honeycomb_model_1.png?raw=true)

Simple model of the Honeycomb Web connection

When a user requests Data, the request is sent to the Class 1, or the 3 closest users. 
Since 3 Hexes meet on a single edge(where users reside), a single point(user) will be connected to 3 users, and they will be the Class 1.

The Class 1 users will run search on their devices(in the background), and if a match is found, the matched Data will be sent to the original user.

If a match isn't found, Class 1 passes the task onto Class 2.
This method continues until Class 3.


## HCPF/HCAF

A HCPF file is a HoneyComb Page File, and a HCAF is a HoneyComb Action File.

### HCPF

HCPF is similar to the current HTML, but is tied with CSS.
It is conceptually a new type of Web programming language, which is intended to load fast and be connected with a design by default.

When you create an element, you will have to give it a design option.
(Write more about this later)


## Honeycomb Security

One of the biggest and the main feature of this Web concept is Security.
Today's web systems can be exploited using packet sniffers to examine non-secure connections.

And we made a solution with the HCSec.

For specific information, check out "Honeycomb Sec.pdf".

#### Prequisites

Let's say that A is the one sending the Data, and B is the one recieving it.

The Data is an integer.

There are three routes, each labled 1, 2, 3.

The 1st route goes through 10 individual users; 2nd route goes through 4; 3rd route goes through 6.

#### Step 1

A will count the length of the routes 1, 2, 3.

It will define Data Prime as:
(Data ** (length of 3)) * (length of 1) * (length of 2)

#### Step 2

A sends these Data through specific lines.

Route 1: Sends the length of 3

Route 2: Sends the value of Data Prime

Route 3: Sends the length of 1 & 2

#### Step 3

When carrying the value of Data Prime through Route 2, each individual that it passes will subtract 1 from its value.
 
 Therefore, the value of which B gets from Route 2 will be ( Data Prime - (length of Route 2) ).
 
 #### Step 4
 
 Now B has recieved every data it needs.
 
 The value of original Data can be achieved by solving the equation below:
 
 (image of equation)
 
 
 ### Why is this method Secure?
 
 Well, for example, if someone was to obtain data from the Route 2, they still wouldn't be able to dechiper it.
 
As long as they do not know where the data originated from and which Route it took, they can't get the original Data.
