from module import frame_capture, color_utils, template_matcher
from objects import game
import pyautogui
import random
import time
import os

# game variables
threshold = 190  # 160 is fine
game = game.Game(x=166, y=187, x2=1441, y2=904, strategy=None)


def feature_matcher(input_image, match_image):
    # input_image = os.getcwd() + '/images/' + 'beginning2.png'
    compass_template_image = os.getcwd() + '/images/pilkki/' + match_image
    target_point = template_matcher.find_matching_position(
        input_image, compass_template_image, ['cv.TM_SQDIFF_NORMED'], plot=True, im_show=False
    )
    print('target point frame: ' + str(target_point))
    return target_point


# window frame capture
window_frame = frame_capture.capture_window_frame(game.x, game.y, game.x2, game.y2, im_show=False)

# gives point where tool head exists
tp = feature_matcher(window_frame, 'basic_tool.png')
diff = abs(tp[3] - tp[1])
tp_ = [
    tp[0] + game.x,
    tp[1] + game.y + diff,
    tp[2] + game.x,
    tp[3] + game.y + diff
]

# gives point where tool handle is
handle = feature_matcher(window_frame, 'basic_tool_handle.png')

# window frame capture
while 1:
    window_frame = frame_capture.capture_window_frame_continuous(tp_[0], tp_[1], tp_[2], tp_[3], im_show=False)
    avg_color = color_utils.get_avg_color(window_frame)
    if avg_color < threshold:
        print('Fish!')
        pyautogui.moveTo(x=handle[0], y=handle[1])
        pyautogui.dragTo(x=handle[0], y=handle[1] - 100, duration=0.2, button='left')  # focus the window
        pyautogui.moveTo(x=handle[0], y=handle[1])
        time.sleep(2)
    elif random.randint(0, 400) is 18:
        print('Random swing')
        # noinspection DuplicatedCode
        pyautogui.moveTo(x=handle[0], y=handle[1])
        pyautogui.dragTo(x=handle[0], y=handle[1] - 100, duration=0.2, button='left')  # focus the window
        pyautogui.moveTo(x=handle[0], y=handle[1])
        time.sleep(2)
