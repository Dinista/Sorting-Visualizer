# Sorting-Visualizer

## Introduction

A basic Bubble Sort, Insertion Sort and Selection Sort Visualizer applying matplotlib in Python. The main goal of this project is the use of data and procedure abstraction in the creation of an extensible program.

An portuguese article was written explaining in details the implementation, it can be found in the folder <i>/docs</i>

<b> Second project of the class Imperative and Object Oriented Programming Paradigm.</b>

## <div id = "fea" >Features</div>

<ul>
  <li>Allow the user to select a predefined arrangement configuration (random, in reverse order, grows and participates);</li>
  <li>Allow the user to select the algorithms to be viewed;</li>
  <li>Allow the user to choose between an automatic animation or a walkthrough;</li>
  <li>Displays the name of the selected algorithms, the execution time and the number of exchanges made for each algorithm so far.</li>
</ul>

<b>The program is extensible</b>, allows the addition of a new algorithm to be visualize by adding a maximum of two lines to the existing code: one to import the new algorithm and the other to link the new algorithm to the system.


### Applying extensibility
In order for a new algorithm to be added to the software, it is necessary to add an import it into the <i>main.py</i> file.
Example:
```python
import QuickSort as Quick
```
After that add in line 101 (between 100 to 103) the following command:
```python
elif int(algoritmo) == 3: Frames = Quick.Quick_Sort(A)
```
That was an example using a fictional <i>Quick_Sort</i> Algorithm.

## How to use
As mentioned matplotlib was used, so is necessary to install it.

### Input
It has a menu where the user are able to select the preferences mentioned on the <a href="#fea"><i>features</i></a> section.
### Output
The output will be a windown showing the visualization, the execution time and the number of exchanges made through execution.

## Unit tests
Each sort algorithm has unit tests implemented.
