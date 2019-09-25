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


class TestCellsPageBreaksApi(unittest.TestCase):
    """ CellsPageBreaksApi unit test stubs """

    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)
        # self.api_client = AuthUtil.GetApiClient()
        self.api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey())

    def tearDown(self):
        pass

    def test_cells_page_breaks_delete_horizontal_page_break(self):
        """
        Test case for cells_page_breaks_delete_horizontal_page_break

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_page_breaks_delete_horizontal_page_break(name, sheet_name,index,folder=folder)
        pass

    def test_cells_page_breaks_delete_horizontal_page_breaks(self):
        """
        Test case for cells_page_breaks_delete_horizontal_page_breaks

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        row = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_page_breaks_delete_horizontal_page_breaks(name, sheet_name,row=row,folder=folder)
        pass

    def test_cells_page_breaks_delete_vertical_page_break(self):
        """
        Test case for cells_page_breaks_delete_vertical_page_break

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_page_breaks_delete_vertical_page_break(name, sheet_name,index,folder=folder)
        pass

    def test_cells_page_breaks_delete_vertical_page_breaks(self):
        """
        Test case for cells_page_breaks_delete_vertical_page_breaks

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        column = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_page_breaks_delete_vertical_page_breaks(name, sheet_name,column=column,folder=folder)
        pass

    def test_cells_page_breaks_get_horizontal_page_break(self):
        """
        Test case for cells_page_breaks_get_horizontal_page_break

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_page_breaks_get_horizontal_page_break(name, sheet_name,index,folder=folder)
        pass

    def test_cells_page_breaks_get_horizontal_page_breaks(self):
        """
        Test case for cells_page_breaks_get_horizontal_page_breaks

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'  
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_page_breaks_get_horizontal_page_breaks(name, sheet_name,folder=folder)
        pass

    def test_cells_page_breaks_get_vertical_page_break(self):
        """
        Test case for cells_page_breaks_get_vertical_page_break

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_page_breaks_get_vertical_page_break(name, sheet_name,index,folder=folder)
        pass

    def test_cells_page_breaks_get_vertical_page_breaks(self):
        """
        Test case for cells_page_breaks_get_vertical_page_breaks

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        index = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_page_breaks_get_vertical_page_breaks(name, sheet_name,folder=folder)
        pass

    def test_cells_page_breaks_put_horizontal_page_break(self):
        """
        Test case for cells_page_breaks_put_horizontal_page_break

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellname = 'A1'     
        row = 1  
        column = 1  
        startColumn = 1  
        endColumn = 1      
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_page_breaks_put_horizontal_page_break(name, sheet_name, cellname=cellname,row=row, column=column ,start_column=startColumn,end_column=endColumn,folder=folder)
        pass

    def test_cells_page_breaks_put_vertical_page_break(self):
        """
        Test case for cells_page_breaks_put_vertical_page_break

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        cellname = 'A1'     
        row = 1  
        column = 1  
        startRow = 1  
        endRow = 1      
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_page_breaks_put_vertical_page_break(name, sheet_name, cellname=cellname,column=column, row=row ,start_row=startRow,end_row=endRow,folder=folder)
        pass


if __name__ == '__main__':
    unittest.main()
