# -*- coding: utf-8 -*-

"""FileSystem class"""

import ConfigParser
import StringIO
import os

from .exceptions import FileSystemError


class FileSystem:
    """FileSystem class"""

    @staticmethod
    def read(filename):
        """ read txt file """

        file = os.path.join(os.getcwd(), filename)
        if not os.path.isfile(file):
            raise FileSystemError("{0} is not a file ".format(file))
        if not os.access(file, os.R_OK):
            raise FileSystemError("Configuration file {0} can not be read. Setup chmod 0644".format(file))

        return file

    @staticmethod
    def readcfg(filename):
        """ read .cfg file """

        file = os.path.join(os.getcwd(), filename)
        if not os.path.isfile(file):
            raise FileSystemError("{0} is not a file ".format(file))
        if not os.access(file, os.R_OK):
            raise FileSystemError("Configuration file {0} can not be read. Setup chmod 0644".format(file))

        try:
            config = ConfigParser.RawConfigParser()
            config.read(file)
            return config
        except ConfigParser.ParsingError as e:
            raise FileSystemError(e.message)

    @staticmethod
    def readraw(data):
        """ read raw data """

        buf = StringIO.StringIO(data)
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(buf)
            return config
        except ConfigParser.Error as e:
            raise FileSystemError(e.message)
