# Monkeytype Solver
Author: Harry He

## Project Description
A video demo of how to use the project.

https://github.com/he-is-harry/Monkeytype-Solver/assets/69978107/340695df-bfce-4976-a414-628d0da9994e

The project will be able to use some keyboard inputs and utilize Python macros to read the screen and output the characters to ace a typing test.

### Libraries Used
- **Pytesseract**: A wrapper library for Google's pretrained Tesseract-OCR Engine to recognize text in images.
- **OpenCV**: Used to get simple programming functions for real time computer vision and as a prerequisite for Pytesseract.
- **pyscreenshot**: The library which screenshots and captures the typing test displayed.
- **pynput**: A library to quickly type out text processed capable of typing out preloaded text instantanously.
- **PyAutoGUI**: Used to locate the bounding boxes of the typing test input box with the user's cursor.

### Challenges Faced
1. **Implementing Abstractions**

   Since I had limited knowledge of the libraries necessary to process the text from images and perform the macros of capturing the screen and typing out the characters, I had to research and learn to use the Tesseract library and multiple other libraries to automate actions. This resulted in most of the time developing the project spent learning how to use the libraries to quickly implement all the complex abstraction I needed.

2. **Real Time Processing**

   Another challenge faced was being able to process a real time stream of words that had to be written. Since the text would be typed out at variable rates, since the words were not always the same length, I had to devise a strategy to figure out if new words had come up during periodic screenshots. Since the AI model cannot possibly always be correct, I used an 80% approximate comparison to check if lines of words intersected which allowed for the real time processing of the typing test.

## Installation and Running
1. Create or open the folder in which you wish to download and run the application.
2. Open the command line at that folder and download the game using the command.
	
        git clone https://github.com/he-is-harry/Monkeytype-Solver.git

3. Run one of the application files by running `python3` followed by the file name. If you wish to just regularly translate images to text run "RegularScreenTyper.py" and if you wish to do a real time typing test run "ReadingScreen.py" but note that you might need to adjust the screenshot dimensions as indicated in the demo video.

        python3 ReadingScreen.py

### Troubleshooting
If you get errors that say that you don't have modules like "pytesseract" which means that you have to install the necessary dependencies, so run the commands to install them.
```
pip install pytesseract
pip install opencv-python
pip install pyscreenshot
pip install pynput
pip install pyautogui
```
You may also have problems running the Python scripts because the macros require accessiblity access. This may differ between operating systems, but most of the time you can just go to your accessbility settings and allow screen recording with Python and possibly also keyboard access.

## Using the Project
When prompted by the command line, you will be able to press Command, which will make the program recognize the input and either start typing or set up the bounding box. The functionality of this command depends on the file as described below.
1. **ReadingScreen.py**: Press command once to have the program read in text in the hardcoded region and type it back out where the cursor lies.
2. **RegularScreenTyper.py**: Press command first to set the upper left corner of the bounding box, and press command again to set the lower right corner. Then pressing command one last time will make the program reading in all the text in the bounding box and type it back out.
3. **ScreenGuide.py**: The program runs for an indefinite amount of time where pressing command will output the pixel position of the cursor, which is used to get the bounding coordinates for the ReadingScreen.py script.

## License

MIT License

Copyright (c) 2023 Harry He

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

   
