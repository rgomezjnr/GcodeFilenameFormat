#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import inspect
import unittest

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0,parent_dir)

import Resources

class TestResources(unittest.TestCase):
    #def test_getPrintsettings(self):

    def test_parseFilenameFormat_return_is_str(self):
        filename_format = "[base_name] [brand] [material] lw [line_width]mm lh [layer_height]mm if [infill_sparse_density]% ext1 [material_print_temperature]C bed [material_bed_temperature]C"
        print_settings = {
            "base_name":"paperclip",
            "brand":"Generic",
            "material":"PLA",
            "line_width":"0.4",
            "layer_height":"0.2",
            "infill_sparse_density":"20",
            "material_print_temperature":"200",
            "material_bed_temperature":"60"
        }

        output = Resources.parseFilenameFormat(filename_format, print_settings)

        self.assertIs(type(output), str)

    def test_parseFilenameFormat_default_format(self):
        filename_format = "[base_name] [brand] [material] lw [line_width]mm lh [layer_height]mm if [infill_sparse_density]% ext1 [material_print_temperature]C bed [material_bed_temperature]C"
        expected_output = "paperclip Generic PLA lw 0.4mm lh 0.2mm if 20% ext1 200C bed 60C"
        print_settings = {
            "base_name":"paperclip",
            "brand":"Generic",
            "material":"PLA",
            "line_width":"0.4",
            "layer_height":"0.2",
            "infill_sparse_density":"20",
            "material_print_temperature":"200",
            "material_bed_temperature":"60"
        }

        output = Resources.parseFilenameFormat(filename_format, print_settings)

        self.assertEqual(output, expected_output)

    def test_parseFilenameFormat_nonalphanumeric_format(self):
        filename_format = "[base_name] [[material]] | Infill-[[infill_sparse_density]]% | NozDiam-[[machine_nozzle_size]] | LH-[[layer_height]] | LW-[[line_width]] | ExtTemp-[[material_print_temperature]]°C | BedTemp-[[material_bed_temperature]]°C"
        expected_output = "paperclip [PLA] | Infill-[20]% | NozDiam-[1.0] | LH-[0.32] | LW-[1.0] | ExtTemp-[220]°C | BedTemp-[65]°C"
        print_settings = {
            "base_name":"paperclip",
            "material":"PLA",
            "infill_sparse_density":"20",
            "machine_nozzle_size":"1.0",
            "layer_height":"0.32",
            "line_width":"1.0",
            "material_print_temperature":"220",
            "material_bed_temperature":"65"
        }

        output = Resources.parseFilenameFormat(filename_format, print_settings)

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
