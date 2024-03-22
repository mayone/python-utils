# -*- coding: utf-8 -*-

import csv
from prettytable import PrettyTable


class CSV:
    def __init__(self, file_path, *args):
        self.lines = None
        self.__fp = None
        self.__writer = None
        try:
            self.__fp = open(file_path, *args)
            self.read()
        except Exception as e:
            print(f"Error: {e}")

    def __repr__(self):
        if not self.lines:
            return None
        table = PrettyTable()

        # Add header
        table.field_names = self.lines[0]
        # Add rows
        table.add_rows(self.lines[1:])

        return table.get_string()

    def read(self):
        if not self.__fp or not self.__fp.readable():
            return
        self.__fp.seek(0)
        lines = csv.reader(self.__fp, delimiter=",")
        self.lines = [row for row in lines]

    def write(self, row):
        if not self.__fp or not self.__fp.writable():
            return
        if not self.__writer:
            self.__writer = csv.writer(self.__fp)
        self.__writer.writerow(row)

    def close(self):
        if self.__fp:
            self.__fp.close()
            self.__fp = None
            self.__writer = None
