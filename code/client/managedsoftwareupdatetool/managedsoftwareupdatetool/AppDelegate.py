# -*- coding: utf-8 -*-
#
#  AppDelegate.py
#  managedsoftwareupdatetool
#
#  Created by Greg Neagle on 8/5/15.
#  Copyright (c) 2015 The Munki Project. All rights reserved.
#

from Foundation import *
from AppKit import *

import managedsoftwareupdate

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        #NSLog("Application did finish launching.")
        #NSLog("Args: %@", sys.argv)
        #NSLog("Info dict: %@", NSBundle.mainBundle().infoDictionary())
        try:
            managedsoftwareupdate.main()
            NSApp.terminate_(self)
        except (SystemExit, KeyboardInterrupt):
            NSApp.terminate_(self)
