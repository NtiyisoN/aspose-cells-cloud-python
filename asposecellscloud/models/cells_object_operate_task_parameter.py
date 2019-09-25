# coding: utf-8

"""
Copyright (c) 2019 Aspose.Cells Cloud
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
"""


from pprint import pformat
from six import iteritems
import re
from . import TaskParameter

class CellsObjectOperateTaskParameter(TaskParameter):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'operate_parameter': 'OperateParameter',
        'destination_workbook': 'FileSource',
        'operate_object': 'OperateObject'
    }

    attribute_map = {
        'operate_parameter': 'OperateParameter',
        'destination_workbook': 'DestinationWorkbook',
        'operate_object': 'OperateObject'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(CellsObjectOperateTaskParameter.swagger_types, **TaskParameter.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(CellsObjectOperateTaskParameter.attribute_map, **TaskParameter.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, operate_parameter=None, destination_workbook=None, operate_object=None, **kw):
        super(CellsObjectOperateTaskParameter, self).__init__(**kw)
		    
        """
        CellsObjectOperateTaskParameter - a model defined in Swagger
        """

        self.container['operate_parameter'] = None
        self.container['destination_workbook'] = None
        self.container['operate_object'] = None

        if operate_parameter is not None:
          self.operate_parameter = operate_parameter
        if destination_workbook is not None:
          self.destination_workbook = destination_workbook
        if operate_object is not None:
          self.operate_object = operate_object

    @property
    def operate_parameter(self):
        """
        Gets the operate_parameter of this CellsObjectOperateTaskParameter.

        :return: The operate_parameter of this CellsObjectOperateTaskParameter.
        :rtype: OperateParameter
        """
        return self.container['operate_parameter']

    @operate_parameter.setter
    def operate_parameter(self, operate_parameter):
        """
        Sets the operate_parameter of this CellsObjectOperateTaskParameter.

        :param operate_parameter: The operate_parameter of this CellsObjectOperateTaskParameter.
        :type: OperateParameter
        """

        self.container['operate_parameter'] = operate_parameter

    @property
    def destination_workbook(self):
        """
        Gets the destination_workbook of this CellsObjectOperateTaskParameter.

        :return: The destination_workbook of this CellsObjectOperateTaskParameter.
        :rtype: FileSource
        """
        return self.container['destination_workbook']

    @destination_workbook.setter
    def destination_workbook(self, destination_workbook):
        """
        Sets the destination_workbook of this CellsObjectOperateTaskParameter.

        :param destination_workbook: The destination_workbook of this CellsObjectOperateTaskParameter.
        :type: FileSource
        """

        self.container['destination_workbook'] = destination_workbook

    @property
    def operate_object(self):
        """
        Gets the operate_object of this CellsObjectOperateTaskParameter.

        :return: The operate_object of this CellsObjectOperateTaskParameter.
        :rtype: OperateObject
        """
        return self.container['operate_object']

    @operate_object.setter
    def operate_object(self, operate_object):
        """
        Sets the operate_object of this CellsObjectOperateTaskParameter.

        :param operate_object: The operate_object of this CellsObjectOperateTaskParameter.
        :type: OperateObject
        """

        self.container['operate_object'] = operate_object

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CellsObjectOperateTaskParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
