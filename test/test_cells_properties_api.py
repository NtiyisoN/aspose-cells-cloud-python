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
from asposecellscloud.models import CellsDocumentProperty
global_api = None

class TestCellsPropertiesApi(unittest.TestCase):
    """ CellsPropertiesApi unit test stubs """

    def setUp(self):
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey(),"v3.0")
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_properties_delete_document_properties(self):
        """
        Test case for cells_properties_delete_document_properties

        Delete all custom document properties and clean built-in ones.
        """
        name ='Book1.xlsx'      
        folder = "Temp"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_properties_delete_document_properties(name,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_properties_delete_document_property(self):
        """
        Test case for cells_properties_delete_document_property

        Delete document property.
        """
        name ='Book1.xlsx' 
        propertyName = "Author"    
        folder = "Temp"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_properties_delete_document_property(name, propertyName ,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_properties_get_document_properties(self):
        """
        Test case for cells_properties_get_document_properties

        Read document properties.
        """
        name ='Book1.xlsx'       
        folder = "Temp"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_properties_get_document_properties(name,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_properties_get_document_property(self):
        """
        Test case for cells_properties_get_document_property

        Read document property by name.
        """
        name ='Book1.xlsx'
        propertyName = "Author"       
        folder = "Temp"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_properties_get_document_property(name,propertyName,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_properties_put_document_property(self):
        """
        Test case for cells_properties_put_document_property

        Set/create document property.
        """
        name ='Book1.xlsx'
        propertyName = "Name"
        _property = CellsDocumentProperty()  
        _property.name = "Author"
        _property.value = "Val"
        folder = "Temp"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_properties_put_document_property(name,propertyName,_property=_property,folder=folder)
        self.assertEqual(result.code,201)
        pass


if __name__ == '__main__':
    unittest.main()
