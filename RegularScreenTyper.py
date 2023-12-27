import pytesseract, cv2
import pyscreenshot as ImageGrab
import os, time, random
import pyautogui
from pynput.keyboard import Key, Controller, Listener
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
# Later you should run: brew uninstall tesseract
# You should also run: pip uninstall opencv-python
# You should also run: pip uninstall pytesseract
# You should also run: pip uinstall pyscreenshot
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

def locateOverlap(s, y):
    length = len(s)
    while(length > 0):
        if(s[len(s) - length:] == y[:length]):
            break
        length -= 1
    return length

left_corner = (0, 0)
right_corner = (100, 100)
left_done = False
print("Press CMD to declare left and right corners")

def on_press_mouse(key):
    print('{0} pressed'.format(
        key))
    if key == Key.cmd:
        global left_done
        print(pyautogui.position())
        if(not left_done):
            global left_corner
            left_corner = pyautogui.position()
            left_done = True
        else:
            global right_corner
            right_corner = pyautogui.position()
            return False

def on_release_mouse(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press_mouse,
        on_release=on_release_mouse) as listener:
    listener.join()

screenshot("Text.png", left_corner[0], left_corner[1], right_corner[0], right_corner[1])

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

time.sleep(1)

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
        processed_text = processed_text.lower()

print(processed_text)

# if(processed_text[0] == "l" and "aeiou".find(processed_text[1]) < 0):
#     processed_text = processed_text[1:]
# elif(processed_text[0] == "k" and "aeiou".find(processed_text[1]) < 0):
#     processed_text = processed_text[1:]
#         # if(processed_text[len(processed_text) - 1] == ' '):
#         #     processed_text = processed_text[:len(processed_text) - 1]
#         # print(processed_text)
#
# if not text_to_process:
#     processed_text = text
#
# new_words_index = locateOverlap(all_words, processed_text)
# possible_insertion = all_words[:curLetter] + "l" + all_words[curLetter:]
# possible_higher = locateOverlap(possible_insertion, processed_text)
# if(new_words_index < possible_higher):
#     new_words_index = possible_higher
#
#         # possible_insertion = all_words[:curLetter] + "|" + all_words[curLetter:]
#         # possible_higher = locateOverlap(possible_insertion, processed_text)
#         # new_words_index = max(new_words_index, possile_higher)
#
#         # chopped = []
# new_words = processed_text[new_words_index:]
#         # print(new_words)
#         # testing_file = open("RandomText.txt", "a")
#
# for i in range(0, len(new_words)):
#     chopped_queue.append(new_words[i])
#     all_words += new_words[i]
#             # testing_file.write(new_words[i])
#         # testing_file.write("\n")
#         # testing_file.close()

for i in range(0, len(processed_text)):
    chopped_queue.append(processed_text[i])
    all_words += processed_text[i];

while(curLetter < len(chopped_queue)):
    ch = chopped_queue[curLetter]
    keyboard.type(ch)
    delay = random.uniform(0, 2)
    time.sleep(delay / 40) #40
    curLetter += 1
