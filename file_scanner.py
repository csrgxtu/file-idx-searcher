# -*- coding: utf8 -*-
import os
import time


class FileScaner(object):
    def __init__(self, root_dir):
        if not os.path.isdir(root_dir):
            raise ValueError('root_dir: {} is not directory'.format(root_dir))
        self.root_dir = root_dir
        self.folders = [root_dir]

    def scan(self):
        # print('self.folders: {}'.format(self.folders))
        while self.folders:
            for entry in os.scandir(self.folders.pop()):
                # print('{} {}'.format(entry.name, entry.is_dir()))
                if entry.is_dir():
                    self.folders.append(entry.path)
                yield entry.name, entry.path


if __name__ == "__main__":
    fs = FileScaner('/home/archer/Documents/Python/micro-wsgi-server')
    for item in fs.scan():
        # print(item)
        time.sleep(1)
