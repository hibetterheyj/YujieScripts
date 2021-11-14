# -*-coding:utf-8 -*-
"""
@File    :   test_timer.py
@Time    :   2021/11/14 13:06:24
@Author  :   Yujie He
@Version :   1.0
@Contact :   yujie.he@epfl.ch
@State   :   Dev
"""


from os import times
import numpy as np


def cputime(T0=(0.0, 0.0)):
    """
    Returns tuple (utime, stime) with CPU time spent since start.

    CPU time since T0 = (utime0, stime0) is returned if
    the optional argument T0 is supplied.
    """
    T = times()
    return (T[0] - T0[0], T[1] - T0[1])


def main():
    Tstart = cputime()

    a = np.random.rand(1000, 1000)
    b = np.random.rand(1000, 1000)
    c = np.linalg.inv(a) @ b

    Tend = cputime(Tstart)
    print("utime = %f, stime = %f." % Tend)
    print("alltime = %f" % sum(Tend))


if __name__ == "__main__":
    main()
