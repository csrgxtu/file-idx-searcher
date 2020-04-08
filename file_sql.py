#!/usr/bin/env python3
import os
import sys
from moz_sql_parser import parse
from file_scanner import FileScaner
from bst import BinarySearchTree


class FileSqlManager(object):
    """
    sql parser and executer
    """
    def __init__(self, bst):
        """
        bst is binary search tree
        """
        self.bst = bst

    def executer(self, sql_cmd):
        """
        parse the sql cmd and execute it
        """
        parsed_sql = parse(sql_cmd)
        if 'select' not in parsed_sql:
            raise ValueError('FileSqlManager not support non-select sql yet!')
        self.__query_executor(parsed_sql.get('select', {}), parsed_sql.get('where', {}))

    def __query_executor(self, fields, conditions):
        """
        query the table and return the params
        :param fields: dict or str
        :param conditions: dict
        # :param bst: object
        :return: list
        """
        if not conditions:
            # traverse get all data
            rtv = []
        else:
            rtv = self.bst.get(conditions.get('eq')[1].get('literal'))
            rtv = [rtv]
        if rtv:
            print('Found {} result'.format(len(rtv)))
            print('{}'.format(rtv))


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
        print('Usage: python3 file_sql.py target_root_dir sql')
        os._exit(1)

    fs = FileSql(sys.argv[1])
    fs.indexer()
    fsm = FileSqlManager(fs.bst)
    print(sys.argv[2])
    fsm.executer(sys.argv[2])
    # fs.searcher(sys.argv[2])