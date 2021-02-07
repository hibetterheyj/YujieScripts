"""webcam_check_support_res.py

Check support display resolution of used webcam. 
Mainly focus on the ratio of 4:3, 5:3, 5:4, 16:9, 16:10

For more info, please refer to following links
1. List of common resolutions-Wiki
    https://en.wikipedia.org/wiki/List_of_common_resolutions
2. Graphics display resolution-Wiki
https://en.wikipedia.org/wiki/Graphics_display_resolution
3. 显示分辨率列表 - 常用显示分辨率 | Graphics display resolution-Commonly used display resolution
    https://zh.wikipedia.org/wiki/%E6%98%BE%E7%A4%BA%E5%88%86%E8%BE%A8%E7%8E%87%E5%88%97%E8%A1%A8
"""

import cv2
import time

def set_res(cap, res):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH , int(res[0]))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(res[1]))
    return [cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)]

if __name__ == "__main__":
    res1_list=[[320, 240], # 4:3
                       [640, 480],
                       [800, 600],
                       [1024, 768],
                       [1152, 864],
                       [1280, 768], # 5:3
                       [720, 576], # 5:4
                       [1280,1024],
                       [640, 360], # 16:9
                       [1280, 720],
                       [1600, 900],
                       [1920, 1080],
                       [1280, 800], # 16:10
                       [1440, 900],
                       [1920, 1200]]

    unsupported_res = []
    supported_res = []

    for res in res_list:
        # 0 stands for built-in camera, 1 stands for my usb webcam
        cap = cv2.VideoCapture(1)
        curr_res = set_res(cap, res)
        if curr_res == res:
            supported_res.append(res)
            print("[{}, {}] supported!!!".format(res[0], res[1]))
        else:
            unsupported_res.append(res)
            print("[{}, {}] not supported!!!".format(res[0], res[1]))
        cv2.namedWindow("test")
        time.sleep(2)
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    print("===== Supported lists ======")

    for res in supported_res:
        print(res, "")