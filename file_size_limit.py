# coding=utf-8

import codecs
from os.path import getsize,exists,dirname,basename
import os

class File():
    
    # maxsize为单文件最大大小,单位为MiB
    def __init__(self,filename,mode='rb',maxsize=None,encoding='utf-8'):
        self.filename = filename
        self.basename = basename(filename)
        self.mode = mode
        self.maxsize = maxsize
        self.encoding = encoding
        self.__open(filename)

    def __open(self,filename):
        file = codecs.open(filename,self.mode,self.encoding)
        self.file = file

    def file(self):
        return self.file

    #def readline(self):
        #line = self.file.readline()
        #while line:
        #    yield line
        #    line = self.file.readline()
        #self.close()
        #for line in self.file:
        #    yield line
        #yield None

    def write(self,info):
        if self.maxsize:
            filename = self.file.name
            if not exists(filename):
                with open(filename,'wb'):
                    pass

            if getsize(filename) >= self.maxsize*1024*1024:
                path = dirname(filename)
                files = os.walk(path).next()[2]
                files_num = len(files)
                for count in xrange(1,files_num + 1):
                    name = "%d_%s"%(count,self.basename)
                    filename = os.path.join(path,name)
                    
                    if exists(filename):
                        if getsize(filename) >= self.maxsize*1024*1024:
                            continue
                    self.file.close()
                    self.__open(filename)
                    break
        self.file.write(info)

    def close(self):
        self.file.close()
