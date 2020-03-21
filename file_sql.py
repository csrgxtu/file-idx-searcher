# -*- coding: utf8 -*-
import os
import sys
from file_scanner import FileScaner
from bst import BinarySearchTree


class FileSql(object):
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.bst = BinarySearchTree()

    def indexer(self):
        fs = FileScaner(self.target_dir)
        total_entries = 0
        for ele in fs.scan():  # name, path
            self.bst[ele[0]] = ele[1]
            total_entries += 1
        print('Indexer done, total {} file or dirs'.format(total_entries))

    def searcher(self, key):
        rtv = self.bst.get(key)
        if rtv:
            print('Searcher done, {}'.format(rtv))
        else:
            print('Searcher done, cant find {}'.format(key))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python3 file_sql.py target_root_dir key_to_search')
        os.exit(1)

    fs = FileSql(sys.argv[1])
    fs.indexer()
    fs.searcher(sys.argv[2])