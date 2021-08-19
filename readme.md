# The Honeycomb Web

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

