from dl_utilis import download_file

if __name__ == "__main__":
    #video link example: https://ras.papercept.net/proceedings/IROS20/0001_PV.mp4
    paperID = ['0103', '0201', '0240', '0386', '0390', '0493', 
            '0496', '0631', '0988', '1015', '0914', '1031', 
            '1065', '2826', '2808', '0457', '1358', '1877', 
            '0079', '0241', '0683', '1988', '2861', '0128', 
            '0249', '0919', '1576', '2325', '1220', '2314', 
            '0857', '0132', '0566', '1741', '0097', '1569']
    paperIDTest = ['1566']
    url =  "https://ras.papercept.net/proceedings/IROS20/"
    ext = '_PV.mp4'
    testset = paperID
    for i in range(len(testset)):
        idx = testset[i]
        videoName = idx + ext
        videoURL = url + videoName
        print('[{}/{}] {} Started !'.format(i+1, len(testset), videoName))
        download_file(videoURL)
        print('[{}/{}] {} Finished !'.format(i+1, len(testset), videoName))


# https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py