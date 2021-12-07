#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# =============================================================================
"""
@Author        :   Yujie He
@File          :   mpy_test.py
@Date created  :   2021/12/07
@Maintainer    :   Yujie He
@Email         :   yujie.he@epfl.ch
"""
# =============================================================================
"""
The module provides snippet to convert image sequence to video and gif
"""
# =============================================================================

import os
import fnmatch

# python -m pip install ez_setup
# python -m pip install moviepy
import moviepy.editor as mpy

img_folder = "./test/"
img_files = sorted(fnmatch.filter(os.listdir(img_folder), "*.png"))
print("{} frames detected".format(len(img_files)))
img_seq = [img_folder + img for img in img_files]

#%% Test sample1
print("## Test sample1: from image sequence to video & gif")
clip1 = mpy.ImageSequenceClip(img_seq, fps=30)

clip1.write_videofile(img_folder+"test_example.mp4", fps=15)

# 720 x 480
clip1.resize((720, 480)).write_gif(img_folder+"test_example.gif", fps=15)

#%% Test sample2
print("## Test sample2: from video file to gif")
clip2 = mpy.VideoFileClip(img_folder+"test2.mp4")
clip2.write_gif(img_folder+"test2.gif", fps=30)
