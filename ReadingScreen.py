import pytesseract, cv2
import pyscreenshot as ImageGrab
import os, time, random
from pynput.keyboard import Key, Controller, Listener
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
# Later you should run: brew uninstall tesseract
# You should also run: pip uninstall opencv-python
# You should also run: pip uninstall pytesseract
# You should also run: pip install pyscreenshot
# Also edit security preferences: Accessiblity, Screen recording

def load_image(path):
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    fullname = os.path.join(main_dir, path)
    img = cv2.imread(fullname)
    return img

def screenshot(path, x1, y1, x2, y2):
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    fullname = os.path.join(main_dir, path)
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    im.save(fullname)
    # ImageGrab.grab_to_file(fullname)

def on_press(key):
    if key == Key.cmd:
        return False

# Sometimes the text will be misread, so here we will just match
# if 80% of the characters match and if the length of the strings
# match by 95% (just in case spaces are missing)
def approxMatch(str1, str2):
    if (len(str1) / len(str2)) < 0.95 or (len(str1) / len(str2)) > 1.05:
        return False
    mismatch = 0
    for i in range(0, min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            mismatch += 1
    return not (mismatch / min(len(str1), len(str2)) > 0.2)


def locateOverlap(s, y):
    length = len(s)
    while(length > 0):
        # if(s[len(s) - length:] == y[:length]):
        if approxMatch(s[len(s) - length:], y[:length]):
            break
        length -= 1
    return length

text_to_process = False
chopped_queue = []
all_words = ""
keyboard = Controller()
curLetter = 0

print("Waiting for CMD")
# Collect events until released
with Listener(
        on_press=on_press) as listener:
    listener.join()

time.sleep(2)

while(True):
    if (curLetter == 0) or (curLetter >= 130 and curLetter % 65 == 0):
    # if (curLetter == 0) or (curLetter >= 50 and curLetter % 25 == 0):
        # Full Screen
        screenshot("Text.png", 286, 475, 1489, 651)
        # Side Screen
        # screenshot("Text.png", 885, 437, 1716, 590)
        # screenshot("Text.png", 1207, 111, 1774, 980)

        print("Processing Image")
        image_path = 'Text.png'
        img = load_image(image_path)

        text = pytesseract.image_to_string(img)
        print(text)

        processed_text = ""
        for ch in text:
            if(ch == '\n'):
                processed_text += " "
            elif(ch.isalpha()):
                processed_text += ch
            elif(ch == ' '):
                processed_text += ch
            else:
                # Special value, we will enter
                # a special character which should
                # not exist, we can get rid of those later
                processed_text += "#"
        processed_text = processed_text.lower()

        # if(processed_text[0] == "l" and "aeiou".find(processed_text[1]) < 0):
        #     processed_text = processed_text[1:]
        # elif(processed_text[0] == "k" and "aeiou".find(processed_text[1]) < 0):
        #     processed_text = processed_text[1:]
        # if(processed_text[len(processed_text) - 1] == ' '):
        #     processed_text = processed_text[:len(processed_text) - 1]

        # print(processed_text)

        # Probably should not uncomment this as we actually want processed text
        # if not text_to_process:
        #     processed_text = text

        new_words_index = locateOverlap(all_words, processed_text)

        # possible_insertion = all_words[:curLetter] + "l" + all_words[curLetter:]
        # possible_insertion = all_words[:curLetter] + all_words[curLetter:]
        # possible_higher = locateOverlap(possible_insertion, processed_text)
        # if(new_words_index < possible_higher):
        #     new_words_index = possible_higher

        # possible_insertion = all_words[:curLetter] + "|" + all_words[curLetter:]
        # possible_higher = locateOverlap(possible_insertion, processed_text)
        # new_words_index = max(new_words_index, possible_higher)

        # chopped = []
        new_words = processed_text[new_words_index:]
        # print(new_words)
        # testing_file = open("RandomText.txt", "a")
        for i in range(0, len(new_words)):
            chopped_queue.append(new_words[i])
            all_words += new_words[i]
            # testing_file.write(new_words[i])
        # print(chopped_queue)
        # testing_file.write("\n")
        # testing_file.close()

    ch = chopped_queue[curLetter]
    keyboard.type(ch)
    delay = random.uniform(0, 2)
    time.sleep(delay / 160) #40
    curLetter += 1

    if (curLetter >= len(chopped_queue)):
        break

print(curLetter)