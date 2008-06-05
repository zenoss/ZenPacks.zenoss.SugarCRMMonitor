######################################################################
#
# Copyright 2007, 2008 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

import Globals
import os
from Products.CMFCore.DirectoryView import registerDirectory
from Products.ZenModel.ZenPack import ZenPackBase


skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())


class ZenPack(ZenPackBase):
    """ SugarCRMMonitor Loader
    """

    packZProperties = [
            ('zSugarCRMBase', '', 'string'),
            ('zSugarCRMUsername', 'zenoss', 'string'),
            ('zSugarCRMPassword', 'zenoss123', 'string'),
            ('zSugarCRMTestAccount', 'SugarCRM', 'string'),
            ]

