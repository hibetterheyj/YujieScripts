"""all_files_dl.py
## Description: download all files of given type from url

## Example
- one pdf
    python all_files_dl.py -l https://memento.epfl.ch/academic-calendar/ --save-here
- many pdf and zip
    python all_files_dl.py -l http://rpg.ifi.uzh.ch/teaching.html --save-here
    # only download zip
    python all_files_dl.py -l http://rpg.ifi.uzh.ch/teaching.html --save-here -t zip
    # only download pdf
    python all_files_dl.py -l http://rpg.ifi.uzh.ch/teaching.html --save-here -t pdf

## Download all files given a specific type in ubuntu can also use
# only download zip
wget -r -l1 -H -t1 -nd -N -np -A.zip -erobots=off http://rpg.ifi.uzh.ch/teaching.html
# only download pdf
wget -r -l1 -H -t1 -nd -N -np -A.pdf -erobots=off http://rpg.ifi.uzh.ch/teaching.html
"""

import os
# pip install requests
import requests
from urllib.parse import urljoin
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import argparse

#%% Functions
def type_all_download(args, soup, type_i, folder_path):
    print("====== 1. Start searching ======")
    search_res = soup.select("a[href$='.{}']".format(type_i))
    print("{} files found!!!".format(len(search_res)))
    print("====== 2. Start downloading ======")
    for counter, link in enumerate(search_res):
        #Name the pdf files using the last portion of each link which are unique in this case
        filename = link['href'].split('/')[-1]
        file_save_path = os.path.join(folder_path,link['href'].split('/')[-1])
        if args.print_all:
            print("[{}/{}] {}".format(counter+1, len(search_res), filename))
        with open(file_save_path, 'wb') as f:
            f.write(requests.get(urljoin(args.link,link['href'])).content)
    print("====== 3. Finished!!! ======")

if __name__ == "__main__":
    print("############ all_files_dl.py ############")
    parser = argparse.ArgumentParser(description='Test argparse')
    ## Main option
    # -l/--link
    parser.add_argument('-l', '--link', required=True, type=str,
                        help='write down site name')
    # --print-all
    parser.add_argument('--print-all', dest='print_all', action='store_true',
                        help="print all filename")
    parser.set_defaults(print_all=True)
    # --save-here
    parser.add_argument('--save-here', dest='save_here', action='store_true',
                        help="save files here")
    parser.set_defaults(save_here=False)
    # --save--folder
    # default setting -> Downloads/ in user’s home directory obtained by (os.path.expanduser('~'))
    parser.add_argument('-f', '--folder_path', default=r""+os.path.join(os.path.expanduser('~'), "Downloads"), 
                        type=str, help='save files in the given folder')
    ## type list
    parser.add_argument('-t', '--type', action='store', dest='type_list',
                        type=str, nargs='*', default=['pdf', 'zip', 'rar'],
                        help="the type of saved files. examples: -t pdf zip rar")

    args = parser.parse_args()

    print("LINK: ", args.link)
    if args.save_here:
        folder_path = os.getcwd()
    else:
        folder_path = args.folder_path
        if not os.path.exists(args.folder_path):os.mkdir(args.folder_path)
    print("SAVE_PATH: ", folder_path)
    response = requests.get(args.link, headers={'User-Agent': 'Custom'})
    soup= BeautifulSoup(response.text, "html.parser")

    print("TYPE_LIST: ", args.type_list)
    for i, type_i in enumerate(args.type_list):
        print("############ ({}/{}) *.{} ############".format(i+1, len(args.type_list), type_i))
        type_all_download(args, soup, type_i, folder_path)

#%% TODO
# rewrite as a function [okay]
# add argparse [okay]
# print all name  [okay]
# update running examples [okay]
# detect and categorize other file types, e.g., zip, rar, code template (such as .py, .m files) [okay]
#   set save folder
    # windows default [okay]
    # TODO: linux default
#   TODO: download all files or not
# TODO: merge files with the same name
# TODO: save subfoldname as webpagename -> change all webpage as underscore case
# TODO: download files with name containing non-latin characters
# TODO: add tqdm viz
# TODO: add file selection
# TODO: add log-in
# TODO: modify according to style guide