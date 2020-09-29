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
from asposecellscloud.models import FormatCondition
global_api = None
class TestCellsConditionalFormattingsApi(unittest.TestCase):
    """ CellsConditionalFormattingsApi unit test stubs """

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_conditional_formattings_delete_worksheet_conditional_formatting(self):
        """
        Test case for cells_conditional_formattings_delete_worksheet_conditional_formatting

        Remove conditional formatting
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_conditional_formattings_delete_worksheet_conditional_formatting(name, sheet_name,index,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_conditional_formattings_delete_worksheet_conditional_formatting_area(self):
        """
        Test case for cells_conditional_formattings_delete_worksheet_conditional_formatting_area

        Remove cell area from conditional formatting.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        startRow = 1    
        startColumn = 1
        totalRows = 4
        totalColumns = 6     
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_conditional_formattings_delete_worksheet_conditional_formatting_area(name, sheet_name,startRow,startColumn, totalRows,totalColumns,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_conditional_formattings_delete_worksheet_conditional_formattings(self):
        """
        Test case for cells_conditional_formattings_delete_worksheet_conditional_formattings

        Clear all condition formattings
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'   
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_conditional_formattings_delete_worksheet_conditional_formattings(name, sheet_name,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_conditional_formattings_get_worksheet_conditional_formatting(self):
        """
        Test case for cells_conditional_formattings_get_worksheet_conditional_formatting

        Get conditional formatting
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_conditional_formattings_get_worksheet_conditional_formatting(name, sheet_name,index,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_conditional_formattings_get_worksheet_conditional_formattings(self):
        """
        Test case for cells_conditional_formattings_get_worksheet_conditional_formattings

        Get conditional formattings 
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_conditional_formattings_get_worksheet_conditional_formattings(name, sheet_name,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_conditional_formattings_put_worksheet_conditional_formatting(self):
        """
        Test case for cells_conditional_formattings_put_worksheet_conditional_formatting

        Add a condition formatting.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellArea = "A1:C10"         
        formatcondition = FormatCondition()
        formatcondition.type = "CellValue"
        formatcondition.operator = "Between"
        formatcondition.formula1 = "v1"
        formatcondition.formula2 = "v2"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_conditional_formattings_put_worksheet_conditional_formatting(name, sheet_name,cellArea,format_condition=formatcondition,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_conditional_formattings_put_worksheet_format_condition(self):
        """
        Test case for cells_conditional_formattings_put_worksheet_format_condition

        Add a format condition.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0     
        cellArea = "A1:C10"     
        type = "CellValue"     
        operatorType = "Between"     
        formula1 = "v1"     
        formula2 = "v2"         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_conditional_formattings_put_worksheet_format_condition(name, sheet_name,index , cellArea,   type,  operatorType ,formula1,formula2, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_conditional_formattings_put_worksheet_format_condition_area(self):
        """
        Test case for cells_conditional_formattings_put_worksheet_format_condition_area

        add a cell area for format condition             
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0       
        cellArea = "A1:C10"       
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_conditional_formattings_put_worksheet_format_condition_area(name, sheet_name, index, cellArea , folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_conditional_formattings_put_worksheet_format_condition_condition(self):
        """
        Test case for cells_conditional_formattings_put_worksheet_format_condition_condition

        Add a condition for format condition.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0      
        type = "CellValue"     
        operatorType = "Between"     
        formula1 = "v1"     
        formula2 = "v2"         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_conditional_formattings_put_worksheet_format_condition_condition(name, sheet_name, index , type,  operatorType ,formula1,formula2, folder=folder)
        self.assertEqual(result.code,200)
        pass


if __name__ == '__main__':
    unittest.main()
