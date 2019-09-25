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
from asposecellscloud.models import OleObject


class TestCellsOleObjectsApi(unittest.TestCase):
    """ CellsOleObjectsApi unit test stubs """

    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)
        # self.api_client = AuthUtil.GetApiClient()
        self.api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey())

    def tearDown(self):
        pass

    def test_cells_ole_objects_delete_worksheet_ole_object(self):
        """
        Test case for cells_ole_objects_delete_worksheet_ole_object

        Delete OLE object.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        oleObjectIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_ole_objects_delete_worksheet_ole_object(name, sheet_name,oleObjectIndex,folder=folder)
        pass

    def test_cells_ole_objects_delete_worksheet_ole_objects(self):
        """
        Test case for cells_ole_objects_delete_worksheet_ole_objects

        Delete all OLE objects.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        oleObjectIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_ole_objects_delete_worksheet_ole_objects(name, sheet_name,folder=folder)
        pass

    def test_cells_ole_objects_get_worksheet_ole_object(self):
        """
        Test case for cells_ole_objects_get_worksheet_ole_object

        Get OLE object info.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        oleObjectIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_ole_objects_get_worksheet_ole_object(name, sheet_name,oleObjectIndex,folder=folder)
        pass

    def test_cells_ole_objects_get_worksheet_ole_object_format(self):
        """
        Test case for cells_ole_objects_get_worksheet_ole_object_format

        Get OLE object info.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        oleObjectIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_ole_objects_get_worksheet_ole_object(name, sheet_name,oleObjectIndex,format="png",folder=folder)
        pass

    def test_cells_ole_objects_get_worksheet_ole_objects(self):
        """
        Test case for cells_ole_objects_get_worksheet_ole_objects

        Get worksheet OLE objects info.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        oleObjectIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_ole_objects_get_worksheet_ole_objects(name, sheet_name,folder=folder)
        pass

    def test_cells_ole_objects_post_update_worksheet_ole_object(self):
        """
        Test case for cells_ole_objects_post_update_worksheet_ole_object

        Update OLE object.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        oleObjectIndex = 0  
        ole = OleObject()  
        ole.left = 10
        ole.right = 10
        ole.height = 90
        ole.width = 78
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_ole_objects_post_update_worksheet_ole_object(name, sheet_name,oleObjectIndex,ole=ole,folder=folder)
        pass

    def test_cells_ole_objects_put_worksheet_ole_object(self):
        """
        Test case for cells_ole_objects_put_worksheet_ole_object

        Add OLE object
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        ole = None
        upperLeftRow = 1         
        upperLeftColumn = 1  
        height = 100  
        width = 80  
        oleFile = 'OLEDoc.docx'  
        imageFile = 'word.jpg'  
        folder = "Temp"
        AuthUtil.Ready(self.api, name, folder)
        result = self.api.cells_ole_objects_put_worksheet_ole_object(name, sheet_name, ole_object=ole,upper_left_row=upperLeftRow,upper_left_column=upperLeftColumn,height=height,width=width,ole_file=oleFile, image_file=imageFile,folder=folder)
        pass


if __name__ == '__main__':
    unittest.main()
