# Text-compare application

A GUI application made with python module Tkinter which compares two text files, and shows you their similarity in percentages.

![textcompare](https://user-images.githubusercontent.com/59142427/88962933-6f7c2600-d2a7-11ea-9724-c8a7c9fa1c92.gif)

## Features

* App has 6 buttons, 2 of them that load .txt files from your machine, 2 clear buttons (they clear their loaded file respectively and result label), "reset" button that clears all labels (two loaded files and result label) and there is "compare" button that runs the comparing algorithm and writes result label that shows similarity in percentages
* There are 12 functions in total, 6 functions each dedicated to its own button, and 6 functions that are doing all the comparing
* Comparing functions work on the next principle, first part: it loads file, than it eliminates all the punctuation signs and separates whole text into words and store all of them into list, and at last, store those words into dictionary (key-value pairs) where key is a distinct word and value is how many times that word appears in the loaded text file
* Second part of comparing algorithm loads two dictionaries and do an inner product that is called by last function that uses the formula for vector dot product to get an angle between two vectors, and returns value in percentages at the end (that final value is nothing more than the cosine of an angle between two vectors(text dictionaries) multiplied by 100), that everyone can see in result label
