#coding=utf-8
import requests
import traceback
import re
from bs4 import BeautifulSoup

class DownLoader:
    imageDir = "E:\\worktest\\tuigirl2"
    imageCount = 0
    hasDownloadedImgUrl = set()
    def __init__(self):
        print (self)

    '''下载网页'''

    @staticmethod
    def downLoadPage(pageUrl):
        try:
            response = requests.get(pageUrl)
            if response.status_code == 200:
                print ("download page %s success" % (pageUrl))
                page_content = response.content
                return page_content
        except Exception, e:
            print ("download page %s error " %(pageUrl))
            print ("download page error due to %s" % (e.message))
            print 'repr(e):\t', repr(e)
            print 'traceback.print_exc():';
            traceback.print_exc()
            print 'traceback.format_exc():\n%s' % traceback.format_exc()

        print ("try to download page %s" %(pageUrl))


    '''下载图片'''

    @staticmethod
    def downloadImage(imgUrl):
        if imgUrl in DownLoader.hasDownloadedImgUrl:
            print ("imgUrl %s has been downloaded ." %(imgUrl))
            return

        print ("try to download image %s" %(imgUrl))
        try:
            response = requests.get(imgUrl)
            img = response.content
            if response.status_code == 200:
                try:
                    path = "E:\\worktest\\tuigirl2\\%d.jpg" % DownLoader.imageCount
                    DownLoader.imageCount += 1
                    with open(path, 'wb') as f:
                        f.write(img)
                        DownLoader.hasDownloadedImgUrl.add(imgUrl)
                except Exception, e:
                    print ("...error but we go on...")
                    print ("write error due to %s" % (e.message))
                    print 'repr(e):\t', repr(e)
                    print 'traceback.print_exc():';
                    traceback.print_exc()
                    print 'traceback.format_exc():\n%s' % traceback.format_exc()
            else:
                print ("can not get image %s" % (imgUrl))
        except Exception, e:
            print ("download %s error" %(imgUrl))
            print ("error due to %s" %(e.message))
            print 'repr(e):\t', repr(e)
            print 'traceback.print_exc():';
            traceback.print_exc()
            print 'traceback.format_exc():\n%s' % traceback.format_exc()




    @staticmethod
    def getBigImage(url):
        bigImgPageContent = DownLoader.downLoadPage(url)
        bigImgPageSoup = BeautifulSoup(bigImgPageContent, 'html.parser')
        imgList = bigImgPageSoup.find_all('img')
        for image in imgList:
            src = image.get('src')
            if 'images' in src:
                print ("haha src %s" % (src))





