#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# =============================================================================
"""
@Author        :   Yujie He
@File          :   test_argparse.py
@Date created  :   2021/11/21
@Maintainer    :   Yujie He
@Email         :   yujie.he@epfl.ch
"""
# =============================================================================
"""
The module provides snippets to use argparse
Example:
> python test_argparse.py -n A
====== Experiment: test_argparse ======
A only extract set1
with feature; training set ratio: 0.5
with GPU: False

> python test_argparse.py -n Yujie --useGPU --extract-all --no-feature
====== Experiment: test_argparse ======
Yujie extract all
w/o feature; training set ratio: 0.5
with GPU: True
"""
# =============================================================================


import argparse

## Secondary option
def set_other_options(parser):
    """general settings"""
    parser.add_argument(
        "-o",
        "--output_folder",
        default=None,
        type=str,
        help="if None, will not write the images to disk",
    )
    parser.add_argument("--dataset", default="test_argparse", type=str)
    """ GPU """
    parser.add_argument("--useGPU", dest="useGPU", action="store_true")
    parser.set_defaults(useGPU=False)
    """ Display """
    parser.add_argument("--display", dest="display", action="store_true")
    parser.set_defaults(display=False)


## Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test argparse")
    ####################################
    ############ ALL OPTION ############
    ## Main option
    # string: required; using two tags ('-n', '--name')
    parser.add_argument(
        "-n", "--name", required=True, type=str, help="write down your name"
    )
    # boolean: False; with default
    parser.add_argument(
        "--extract-all",
        dest="extA",
        action="store_true",
        help="Extract frames from all sets of videos",
    )
    parser.set_defaults(extA=False)
    # int: with default
    parser.add_argument(
        "--set", default=1, type=int, help="Set index. Ignored if --extract-all=True"
    )
    # float: with default; using two tags ('-r', '--train_ratio')
    parser.add_argument(
        "-r", "--train_ratio", default=0.5, type=float, help="Ratio of training set"
    )
    # boolean: True/False; with default
    parser.add_argument("--feature", dest="feature", action="store_true")
    parser.add_argument("--no-feature", dest="feature", action="store_false")
    parser.set_defaults(feature=True)

    ## Secondary option
    # for more details, please refer to `set_other_options`.
    set_other_options(parser)

    ########################################
    ############ PARSING OPTION ############
    args = parser.parse_args()
    print("====== Experiment: {} ======".format(args.dataset))
    if args.extA:
        print(args.name + " extract all")
    else:
        print(args.name + " only extract set" + str(args.set))
    if args.feature:
        print("with feature; training set ratio:", args.train_ratio)
    else:
        print("w/o feature; training set ratio:", args.train_ratio)
    print("with GPU: True" if args.useGPU else "with GPU: False")

## REFERENCE:
# Official doc
# https://docs.python.org/3/library/argparse.html
# https://docs.python.org/zh-cn/3/library/argparse.html
# Applicantion example
# https://github.com/uzh-rpg/rpg_e2vid/blob/master/run_reconstruction.py
# https://github.com/uzh-rpg/rpg_e2vid/blob/master/options/inference_options.py
