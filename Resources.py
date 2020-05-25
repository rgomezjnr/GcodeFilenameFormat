# LGPLv3

import os
import sys
import re

from typing import cast

#from UM.Logger import Logger
#from UM.Application import Application
#from UM.Qt.Duration import DurationFormat
#from UM.Scene.Iterator.DepthFirstIterator import DepthFirstIterator
#from UM.Version import Version
#
#from cura.CuraApplication import CuraApplication
#from cura.Settings.ExtruderManager import ExtruderManager
#from cura.UI.ObjectsModel import ObjectsModel

#def getPrintSettings(self, filename_format, file_name) -> dict:
#    first_extruder_stack = ExtruderManager.getInstance().getActiveExtruderStacks()[0]
#    print_information = application.getPrintInformation()
#    machine_manager = application.getMachineManager()
#    print_settings = dict()
#
#    tokens = re.split(r'\W+', filename_format)      # TODO: split on brackets only
#    Logger.log("d", "tokens = %s", tokens)
#
#    # Perform first pass of determining setting values from Cura stacks
#    for t in tokens:
#        stack1 = first_extruder_stack.material.getMetaData().get(t, "")
#        stack2 = global_stack.userChanges.getProperty(t, "value")
#        stack3 = first_extruder_stack.getProperty(t, "value")
#
#        if stack1 is not None and stack1 is not "":
#            print_settings[t] = stack1
#        elif stack2 is not None and stack2 is not "":
#            print_settings[t] = stack2
#        elif stack3 is not None and stack3 is not "":
#            print_settings[t] = stack3
#        else:
#            print_settings[t] = None
#
#    # Manually retrieve remaining setting values
#    job_name = print_information.jobName
#    printer_name = global_stack.getName()
#    profile_name = machine_manager.activeQualityOrQualityChangesName
#    print_time = print_information.currentPrintTime.getDisplayString(DurationFormat.Format.ISO8601)
#    print_time_days = print_information.currentPrintTime.days
#    print_time_hours = print_information.currentPrintTime.hours
#    print_time_hours_all = print_time_days * 24 + print_time_hours
#    print_time_minutes = print_information.currentPrintTime.minutes
#    print_time_seconds = print_information.currentPrintTime.seconds
#    material_weight = print_information.materialWeights
#    material_length = print_information.materialLengths
#    material_cost = print_information.materialCosts
#    object_count = self.getObjectCount()
#    cura_version = Version(Application.getInstance().getVersion())
#
#    print_settings["base_name"] = file_name
#    print_settings["job_name"] = job_name
#    print_settings["printer_name"] = printer_name
#    print_settings["profile_name"] = profile_name
#    print_settings["print_time"] = print_time
#    print_settings["print_time_days"] = print_time_days
#    print_settings["print_time_hours"] = print_time_hours
#    print_settings["print_time_hours_all"] = print_time_hours_all
#    print_settings["print_time_minutes"] = print_time_minutes
#    print_settings["print_time_seconds"] = print_time_seconds
#    print_settings["material_weight"] = int(material_weight[0])
#    print_settings["material_length"] = round(float(material_length[0]), 1)
#    print_settings["material_cost"] = round(float(material_cost[0]), 2)
#    print_settings["object_count"] = object_count
#    print_settings["cura_version"] = cura_version
#
#    return print_settings

# Perform lookup and replacement of print setting values in filename format
def parseFilenameFormat(filename_format, print_settings) -> str:
    for setting, value in print_settings.items():
        filename_format = filename_format.replace("[" + setting + "]", str(value))

    # Sanitize filename for saving
    filename_format = re.sub('[^A-Za-z0-9._\-%°$£€\[\]\(\)\| ]+', '', filename_format)
    #Logger.log("d", "filename_format = %s", filename_format)

    return filename_format

#def getObjectCount(self) -> int:
#    count = 0
#
#    for node in DepthFirstIterator(Application.getInstance().getController().getScene().getRoot()):
#        if not ObjectsModel()._shouldNodeBeHandled(node):
#            continue
#
#        count += 1
#
#    return count

# Get list of modified print settings using SliceInfoPlugin
#def getModifiedPrintSettings(self, application, global_stack):
#    slice_info = application._plugin_registry.getPluginObject("SliceInfoPlugin")
#    modified_print_settings = slice_info._getUserModifiedSettingKeys()
#
#    machine_id = global_stack.definition.getId()
#    manufacturer = global_stack.definition.getMetaDataEntry("manufacturer", "")

# Structure captured print settings into a tack on for file name
def filenameTackOn(self, print_setting):
    tack_on = ""
    for setting, value in print_setting.items():
        tack_on += " " + setting + " " + str(value)

    return tack_on
