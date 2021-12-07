#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# =============================================================================
"""
@Author        :   Yujie He
@File          :   test_sound.py
@Date created  :   2020/11/21
@Maintainer    :   Yujie He
@Email         :   yujie.he@epfl.ch
"""
# =============================================================================
"""
The module provides snippets to produce sound using with python
"""
# =============================================================================

from Sound.sound_utilis import startRing, endRing
import time

def test():
    print("#### Start ####")
    startRing()

    print("After 2.5 seconds ...")
    time.sleep(2.5)

    print("#### End ####")
    endRing()

    print("After 2.5 seconds ...")
    time.sleep(2.5)

    print("#### Start lasting 2 seconds ####")
    startRing(duration=2)

if __name__ == "__main__":
    test()
