#!/usr/bin/env powerscript
# -*- mode: python; coding: utf-8 -*-
# $Id: custom_update_template.py 112039 2014-07-15 15:30:32Z frank $
#
# Copyright (C) 1990 - 2012 CONTACT Software GmbH
# All rights reserved.
# http://www.contact.de/
#
# File:     custom_update_template.py
# Author:   CONTACT
# Purpose:  Template to create a CIM DATABASE Updateskript
#           in a way that has been used before cdb.10
#           In cdb.10 you have to use the tools of the
#           component architecture to provide updates.

import sys
from cdb import InstallScript


class CustomUpdate (InstallScript.CDBCustomUpdateScript):
    """
    Description of the update
    """

    def __init__(self):
        InstallScript.CDBCustomUpdateScript.__init__(self, __file__.decode(sys.getfilesystemencoding()), self.__doc__)
        # To ensure the consistency of the object dictionary
        # `util.ObjectDictionary.cleanup` is called during the
        # update. In some installations this is a very expensive call.
        # You can improve the performance by calling `set_affected_oid_tables`
        # with a list of database tables that are affected by the update.
        # If you do so `util.ObjectDictionary.cleanup` will be called
        # only for this tables. If you set `affected_tables` to ``[]`` the
        # cleanup is skipped.

        # self.set_affected_oid_tables(["<relation1>", "<relation2>"])

    def requires_control_file(self):
        """
        The control file is necessary if you use the ClassExporter
        """
        return True

    def get_export_ctrl(self):
        """
        Returns a list of configuration data that should be exported in addition
        to the data exported by the ClassExporter. All elements listed here will
        be removed when calling the script before the new data will be inserted.
        """
        my_ctrl = []
        return my_ctrl

    def get_export_ctrl_files(self):
        """
        Returns a list of statements that are used to identify
        objects that aggregates blobs. E.g. if you want to export
        all blobs assigned to documents of the category ``example``
        you have to return ``["zeichnung where z_categ1 = 'example'"]``.
        """
        return []

    def get_additional_backup_ctrl(self):
        """
        Return a list of control lines for data that should be backuped but
        not exported.
        """
        return []

    def pre_import(self, session):
        """
        This function is called before the script starts to remove and insert
        data from the exp-files. Return ``False`` if you want to cancel the
        update.
        """
        return True

    def post_import(self, session):
        """
        This function is called after the import is done.
        """
        pass


# Factory Method
def getInstance():
    return CustomUpdate()

if __name__ == "__main__":
    # Change sys.argv to unicode
    sys.argv = [arg.decode("utf-8") for arg in sys.argv]
    InstallScript.run(sys.argv, getInstance())
