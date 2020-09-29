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
from asposecellscloud.models import PivotTableFieldRequest
from asposecellscloud.models import PivotFilter
from asposecellscloud.models import PivotField
from asposecellscloud.models import AutoFilter
from asposecellscloud.models import FilterColumn
from asposecellscloud.models import Top10Filter
from asposecellscloud.models import Style
from asposecellscloud.models import Font
from asposecellscloud.models import CreatePivotTableRequest
global_api = None

class TestCellsPivotTablesApi(unittest.TestCase):
    """ CellsPivotTablesApi unit test stubs """

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_pivot_tables_delete_pivot_table_field(self):
        """
        Test case for cells_pivot_tables_delete_pivot_table_field

        Delete pivot field into into pivot table
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        pivotFieldType = "row"
        request = PivotTableFieldRequest()
        request.data = [1]
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_delete_pivot_table_field(name, sheet_name, pivot_table_index=pivotTableIndex, pivot_field_type=pivotFieldType,request=request,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_delete_worksheet_pivot_table(self):
        """
        Test case for cells_pivot_tables_delete_worksheet_pivot_table

        Delete worksheet pivot table by index
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        pivotFieldType = "row"
        request = PivotTableFieldRequest()
        request.data = [1]
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_delete_worksheet_pivot_table(name, sheet_name, pivotTableIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass


    def test_cells_pivot_tables_delete_worksheet_pivot_table_filters(self):
        """
        Test case for cells_pivot_tables_delete_worksheet_pivot_table_filters

        delete all pivot filters for piovt table
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        fieldIndex = 0
        needReCalculate = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_delete_worksheet_pivot_table_filters(name, sheet_name,pivotTableIndex,need_re_calculate=needReCalculate, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_delete_worksheet_pivot_tables(self):
        """
        Test case for cells_pivot_tables_delete_worksheet_pivot_tables

        Delete worksheet pivot tables
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        fieldIndex = 0
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_delete_worksheet_pivot_tables(name, sheet_name, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_get_pivot_table_field(self):
        """
        Test case for cells_pivot_tables_get_pivot_table_field

        Get pivot field into into pivot table
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        pivotFieldIndex = 0
        pivotFieldType = "Row"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_get_pivot_table_field(name, sheet_name,pivotTableIndex, pivotFieldIndex,pivotFieldType,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_get_worksheet_pivot_table(self):
        """
        Test case for cells_pivot_tables_get_worksheet_pivot_table

        Get worksheet pivottable info by index.
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        fieldIndex = 0
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_get_worksheet_pivot_table(name, sheet_name,pivotTableIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_get_worksheet_pivot_table_filter(self):
        """
        Test case for cells_pivot_tables_get_worksheet_pivot_table_filter

        
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        filterIndex = 0
        needReCalculate = 'true'
        folder = "PythonTest"
        pivotFilter = PivotFilter()
        pivotFilter.field_index = 1
        pivotFilter.filter_type = "Count"
        
        filterColumn = FilterColumn(field_index = 0)
        filterColumn.filter_type = "Top10"
        top10filter = Top10Filter(is_percent = False, is_top = True, items = 1)
        filterColumn.top10_filter = top10filter

        autoFilter = AutoFilter()
        autoFilter.filter_columns = [filterColumn]
        pivotFilter.auto_filter = autoFilter

        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_put_worksheet_pivot_table_filter(name, sheet_name,pivotTableIndex, filter=pivotFilter, need_re_calculate=needReCalculate,folder=folder)
        self.assertEqual(result.code,200)
        result = self.api.cells_pivot_tables_get_worksheet_pivot_table_filter(name, sheet_name,pivotTableIndex, filterIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_get_worksheet_pivot_table_filters(self):
        """
        Test case for cells_pivot_tables_get_worksheet_pivot_table_filters

        
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        fieldIndex = 0
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_get_worksheet_pivot_table_filters(name, sheet_name,pivotTableIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_get_worksheet_pivot_tables(self):
        """
        Test case for cells_pivot_tables_get_worksheet_pivot_tables

        Get worksheet pivottables info.
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        fieldIndex = 0
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_get_worksheet_pivot_tables(name, sheet_name, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_post_pivot_table_cell_style(self):
        """
        Test case for cells_pivot_tables_post_pivot_table_cell_style

        Update cell style for pivot table
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        column = 1
        row = 1
        style = Style()
        font = Font()
        font.size = 17
        style.font = font
        needReCalculate = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_post_pivot_table_cell_style(name, sheet_name, pivotTableIndex ,column,row ,style=style,need_re_calculate=needReCalculate  ,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_post_pivot_table_field_hide_item(self):
        """
        Test case for cells_pivot_tables_post_pivot_table_field_hide_item

        
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        pivotFieldType = "Row"
        fieldIndex = 0
        itemIndex = 1
        isHide = True
        needReCalculate = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_post_pivot_table_field_hide_item(name, sheet_name, pivotTableIndex ,pivotFieldType,fieldIndex ,itemIndex,isHide,need_re_calculate=needReCalculate  ,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_post_pivot_table_field_move_to(self):
        """
        Test case for cells_pivot_tables_post_pivot_table_field_move_to

        
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        fieldIndex = 0
        _from = "Row"
        to = "Column"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_post_pivot_table_field_move_to(name, sheet_name, pivotTableIndex ,fieldIndex ,_from,to ,folder=folder)
        self.assertEqual(result.code,200)
        pass
    def test_cells_pivot_tables_post_pivot_table_update_pivot_field(self):
        """
        Test case for cells_pivot_tables_post_pivot_table_update_pivot_field

        
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        fieldIndex = 0
        pivotField = PivotField()
        pivotField.number = 5
        to = "Column"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_post_pivot_table_update_pivot_field(name, sheet_name, pivotTableIndex ,fieldIndex ,"Row", pivotField,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_post_pivot_table_style(self):
        """
        Test case for cells_pivot_tables_post_pivot_table_style

        Update style for pivot table
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        style = Style()
        font = Font()
        font.size = 17
        style.font = font
        needReCalculate = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_post_pivot_table_style(name, sheet_name, pivotTableIndex ,style=style,need_re_calculate=needReCalculate,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_post_worksheet_pivot_table_calculate(self):
        """
        Test case for cells_pivot_tables_post_worksheet_pivot_table_calculate

        Calculates pivottable's data to cells.
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_post_worksheet_pivot_table_calculate(name, sheet_name, pivotTableIndex ,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_post_worksheet_pivot_table_move(self):
        """
        Test case for cells_pivot_tables_post_worksheet_pivot_table_move

        
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        column = 1
        row = 1
        destCellName = 'C10'
        needReCalculate = 'true'
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_post_worksheet_pivot_table_move(name, sheet_name, pivotTableIndex ,row=row, column=column,dest_cell_name=destCellName ,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_put_pivot_table_field(self):
        """
        Test case for cells_pivot_tables_put_pivot_table_field

        Add pivot field into into pivot table
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        pivotFieldType = "row"
        request = PivotTableFieldRequest()
        request.data = [1]
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_put_pivot_table_field(name, sheet_name, pivotTableIndex, pivotFieldType,request=request,need_re_calculate=True,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_put_worksheet_pivot_table(self):
        """
        Test case for cells_pivot_tables_put_worksheet_pivot_table

        Add a pivot table into worksheet.
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        request = CreatePivotTableRequest(use_same_source=True)
        request.name = "TestPivot"
        request.dest_cell_name = "C1"
        request.source_data = "Sheet1!C6:E13"
        sourceData = "Sheet1!C6:E13"
        destCellName = "C1"
        tableName = "TestPivot"
        useSameSource = 'true'
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_put_worksheet_pivot_table(name, sheet_name, request=None, folder=folder,source_data=sourceData,dest_cell_name=destCellName,table_name=tableName,use_same_source=useSameSource)
        self.assertEqual(result.code,200)
        pass

    def test_cells_pivot_tables_put_worksheet_pivot_table_filter(self):
        """
        Test case for cells_pivot_tables_put_worksheet_pivot_table_filter

        Add pivot filter for piovt table index
        """
        name ='TestCase.xlsx'
        sheet_name ='Sheet4'
        pivotTableIndex = 0
        fieldIndex = 0
        needReCalculate = True
        folder = "PythonTest"
        pivotFilter = PivotFilter()
        pivotFilter.field_index = 1
        pivotFilter.filter_type = "Count"
       
        filterColumn = FilterColumn(field_index = 0)
        filterColumn.filter_type = "Top10"

        top10filter = Top10Filter(is_percent = False, is_top = True, items = 1)
        filterColumn.top10_filter = top10filter
        
        autoFilter = AutoFilter()
        autoFilter.filter_columns = [filterColumn]
        pivotFilter.auto_filter = autoFilter

        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_pivot_tables_put_worksheet_pivot_table_filter(name, sheet_name,pivotTableIndex, filter=pivotFilter, need_re_calculate=needReCalculate,folder=folder)
        self.assertEqual(result.code,200)
        result = self.api.cells_pivot_tables_delete_worksheet_pivot_table_filter(name, sheet_name, pivotTableIndex,  fieldIndex,need_re_calculate=needReCalculate,folder=folder)
        self.assertEqual(result.code,200)
        pass


if __name__ == '__main__':
    unittest.main()
