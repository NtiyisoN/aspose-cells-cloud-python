# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest
import warnings

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import Validation
from asposecellscloud.models import CellArea


class TestCellsWorksheetValidationsApi(unittest.TestCase):
    """ CellsWorksheetValidationsApi unit test stubs """

    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)
        # self.api_client = AuthUtil.GetApiClient()
        self.api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey())

    def tearDown(self):
        pass

    def test_cells_worksheet_validations_delete_worksheet_validation(self):
        """
        Test case for cells_worksheet_validations_delete_worksheet_validation

        Delete worksheet validation by index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        validationIndex = 0
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_worksheet_validations_delete_worksheet_validation(name, sheet_name, validationIndex, folder=folder)
        pass

    def test_cells_worksheet_validations_get_worksheet_validation(self):
        """
        Test case for cells_worksheet_validations_get_worksheet_validation

        Get worksheet validation by index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        validationIndex = 0
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_worksheet_validations_get_worksheet_validation(name, sheet_name, validationIndex, folder=folder)
        pass

    def test_cells_worksheet_validations_get_worksheet_validations(self):
        """
        Test case for cells_worksheet_validations_get_worksheet_validations

        Get worksheet validations.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        validationIndex = 0
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_worksheet_validations_get_worksheet_validations(name, sheet_name, folder=folder)
        pass

    def test_cells_worksheet_validations_post_worksheet_validation(self):
        """
        Test case for cells_worksheet_validations_post_worksheet_validation

        Update worksheet validation by index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        validationIndex = 0
        validation = Validation()

        area = CellArea(start_row = 0, start_column = 0, end_row = 0, end_column = 0)
        validation.area_list = [area]
        validation.formula1 = "=(OR(A1=\"Yes\",A1=\"No\"))"
        validation.type = "Custom"
        validation.ignore_blank = True
        
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_worksheet_validations_post_worksheet_validation(name, sheet_name,validationIndex, validation=validation,folder=folder)
        pass

    def test_cells_worksheet_validations_put_worksheet_validation(self):
        """
        Test case for cells_worksheet_validations_put_worksheet_validation

        Add worksheet validation at index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        _range = 'A1:c10'      
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_worksheet_validations_put_worksheet_validation(name, sheet_name,range=_range,folder=folder)
        pass


if __name__ == '__main__':
    unittest.main()
