# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'Info@infas-LT.de'
__date__ = '2022-09-05'
__copyright__ = 'Copyright 2022, infas LT GmbH'

import unittest

from qgis.PyQt.QtGui import QDockWidget

from infas_lt_geocoder_dockwidget import infasLtGeocoderDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class infasLtGeocoderDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = infasLtGeocoderDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(infasLtGeocoderDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

