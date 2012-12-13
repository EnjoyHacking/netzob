# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Standard library imports
#+---------------------------------------------------------------------------+
from locale import gettext as _
import logging

#+---------------------------------------------------------------------------+
#| Related third party imports
#+---------------------------------------------------------------------------+
from gi.repository import Gtk, Gdk
import gi
from netzob.UI.Vocabulary.Views.Clustering.ClusteringProfilesView import ClusteringProfilesView
gi.require_version('Gtk', '3.0')
from gi.repository import GObject

#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+


class ClusteringProfilesController(object):
    """Manages the selection of the available clustering profiles"""

    def __init__(self, vocabularyController, fields=[]):
        self.vocabularyController = vocabularyController
        self.fields = fields
        self.profiles = []
        self.profiles.extend(vocabularyController.getCurrentWorkspace().getClusteringProfiles())
        self._view = ClusteringProfilesView(self, self.profiles)
        self.log = logging.getLogger(__name__)

    @property
    def view(self):
        return self._view

    def algorithmsComboBox_changed_cb(self, widget):
        """Callback executed when the algorithms has changed"""
        currentAlgorithm = self._view.getSelectedAlgorithmClassToAdd()
        self._view.updateButtonsWithSelectedAlgorithm(currentAlgorithm)

    def availableClusteringProfilesComboBox_changed_cb(self, widget):
        """Callback executed when the user changes the current profile"""
        currentProfile = self._view.getCurrentProfile()
        self._view.updateFieldWithCurrentProfile(currentProfile)

    def addAlgorithmButton_clicked_cb(self, widget):
        currentAlgorithmClass = self._view.getSelectedAlgorithmClassToAdd()
        currentProfile = self._view.getCurrentProfile()

        currentProfile.addAlgorithm(currentAlgorithmClass())
        self._view.updateFieldWithCurrentProfile(currentProfile)

    def currentAlgorithmsTreeView_cursor_changed_cb(self, widget):
        currentAlgorithm = self._view.getCurrentAlgorithmSelected()
        self._view.updateViewWithSelectedAlgorithmInCurrentProfile(currentAlgorithm)

        if currentAlgorithm is not None:
            controller = currentAlgorithm.getConfigurationController()
            controller.run(self._view.configureCurrentAlgorithmViewport)

    def deleteCurrentAlgorithmButton_clicked_cb(self, widget):
        currentProfil = self._view.getCurrentProfile()
        currentAlgorithm = self._view.getCurrentAlgorithmSelected()
        if currentProfil is not None and currentAlgorithm is not None:
            currentProfil.removeAlgorithm(currentAlgorithm)
        self._view.updateFieldWithCurrentProfile(currentProfil)

    def downCurrentAlgorithmButton_clicked_cb(self, widget):
        self.log.info("Down the selected algorithm")

    def upCurrentAlgorithmButton_clicked_cb(self, widget):
        self.log.info("Up the selected algorithm")

    def deleteProfileButton_clicked_cb(self, widget):
        self.log.info("Delete selected profile")

    def saveProfileButton_clicked_cb(self, widget):
        self.log.info("Save selected profile")

    def executeProfileButton_clicked_cb(self, widget):
        currentProfile = self._view.getCurrentProfile()
        currentProfile.execute(self.fields)

    def closeButton_clicked_cb(self, widget):
        self.destroy()

    def run(self):
        self._view.run()

    def destroy(self):
        self._view.destroy()