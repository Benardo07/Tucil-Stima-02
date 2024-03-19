<h1 align="center">Tugas Kecil 2 IF2211 Strategi Algoritma</h1>
<h1 align="center">Kelompok 78</h3>
<h3 align="center">Building Bézier Curves with Midpoint Algorithm based on Divide and Conquer Algorithm</p>

## Table of Contents

- [Overview](#overview)
- [Abstraction](#abstraction)
- [Built With](#built-with)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [File Structures Overview](#file-structures-overview)
- [Links](#links)


## Overview
![Foto](https://github.com/Benardo07/Tucil2_13522019_13522055/blob/main/test/testcase3.jpg)
Our Team members :
- 13522019 - Wilson Yusda
- 13522055 - Benardo

<p>Our Lecturer : Dr. Ir. Rinaldi Munir, M.T.</p>

Here is the purpose of making this project :
- To fulfill the requirements of the second small assignment for the course IF2211 Algorithm Strategy.
- To implement Divide And Conquer Algorithm in building a Bezier curve.
- To compare between Divide And Conquer to Brute Force Algorithm in building a Bezier curve.

## Abstraction

This project compares Divide and Conquer algorithm with the Brute Force algorithm in terms of computational efficiency and accuracy in building a Bezier Curve. The results demonstrate that the Midpoint Divide and Conquer algorithm outperforms the Brute Force algorithm, especially for curves with a large number of control points. However, if the test is conducted in a smaller case, it will led to a similar run time as both perform quite well on smaller test cases.

## Built With

- [Python](https://www.python.org/)

## Prerequisites

To run this project, you will need to perform several installations, including:
- `Python3` : Python3 is programming language that used to implement the bot and handle all the logic in this game

## Installation

- Make sure you have the following python library installed
```
pip install numpy
```
```
pip install matplotlib
```
- To run our project GUI, simply navigate to `src`  directory and run
```
python main.py
```

## How to Use
Make sure your input format is as below:
- Enter control points in the format (x1,y1),(x2,y2),(x3,y3),...,(xn,yn) without spaces before or after the input, where xn and yn are integers.
- The length of the control points must be at least 3.
- The input for the number of iterations must be an integer greater than 0, and without spaces before or after the input for the number of iterations.
Failing in fulfilling the format required for the app will result in error message.

## File Structures Overview
This repository contains main folder structure such as _doc_, _public_, and _src_.
- `doc`: This folder contains documents that provide accountability for the development of this project, as part of a major assignment. In other words, the "doc" folder will contain reports created for this project.
- `src`: This folder contains the primary codebase for building this project, consistings of the main file and also the algorithm for both Brute Force and Divide And Conquer Algorithm
- `test`: This folder contain every capture of test case available and evaluated by us on our project.

## Links
- Repository : https://github.com/Benardo07/Tucil2_13522019_13522055 
- Issue tracker :
   - If you encounter any issues with the program, come across any disruptive bugs, or have any suggestions for improvement, please don't hesitate to tell the author
- Github main contributor :
   - Contributor 1 (Wilson Yusda-13522019) - https://github.com/Razark-Y
   - Contributor 2 (Benardo-13522055) - https://github.com/Benardo07
