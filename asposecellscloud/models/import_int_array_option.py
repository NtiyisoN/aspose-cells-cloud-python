# coding: utf-8

"""
Copyright (c) 2020 Aspose.Cells Cloud
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
from . import ImportOption

class ImportIntArrayOption(ImportOption):
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
        'data': 'list[int]',
        'is_vertical': 'bool',
        'first_row': 'int',
        'first_column': 'int'
    }

    attribute_map = {
        'data': 'Data',
        'is_vertical': 'IsVertical',
        'first_row': 'FirstRow',
        'first_column': 'FirstColumn'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(ImportIntArrayOption.swagger_types, **ImportOption.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(ImportIntArrayOption.attribute_map, **ImportOption.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, data=None, is_vertical=None, first_row=None, first_column=None, **kw):
        super(ImportIntArrayOption, self).__init__(**kw)
		    
        """
        ImportIntArrayOption - a model defined in Swagger
        """

        self.container['data'] = None
        self.container['is_vertical'] = None
        self.container['first_row'] = None
        self.container['first_column'] = None

        if data is not None:
          self.data = data
        if is_vertical is not None:
          self.is_vertical = is_vertical
        if first_row is not None:
          self.first_row = first_row
        if first_column is not None:
          self.first_column = first_column

    @property
    def data(self):
        """
        Gets the data of this ImportIntArrayOption.

        :return: The data of this ImportIntArrayOption.
        :rtype: list[int]
        """
        return self.container['data']

    @data.setter
    def data(self, data):
        """
        Sets the data of this ImportIntArrayOption.

        :param data: The data of this ImportIntArrayOption.
        :type: list[int]
        """

        self.container['data'] = data

    @property
    def is_vertical(self):
        """
        Gets the is_vertical of this ImportIntArrayOption.

        :return: The is_vertical of this ImportIntArrayOption.
        :rtype: bool
        """
        return self.container['is_vertical']

    @is_vertical.setter
    def is_vertical(self, is_vertical):
        """
        Sets the is_vertical of this ImportIntArrayOption.

        :param is_vertical: The is_vertical of this ImportIntArrayOption.
        :type: bool
        """

        self.container['is_vertical'] = is_vertical

    @property
    def first_row(self):
        """
        Gets the first_row of this ImportIntArrayOption.

        :return: The first_row of this ImportIntArrayOption.
        :rtype: int
        """
        return self.container['first_row']

    @first_row.setter
    def first_row(self, first_row):
        """
        Sets the first_row of this ImportIntArrayOption.

        :param first_row: The first_row of this ImportIntArrayOption.
        :type: int
        """

        self.container['first_row'] = first_row

    @property
    def first_column(self):
        """
        Gets the first_column of this ImportIntArrayOption.

        :return: The first_column of this ImportIntArrayOption.
        :rtype: int
        """
        return self.container['first_column']

    @first_column.setter
    def first_column(self, first_column):
        """
        Sets the first_column of this ImportIntArrayOption.

        :param first_column: The first_column of this ImportIntArrayOption.
        :type: int
        """

        self.container['first_column'] = first_column

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
        if not isinstance(other, ImportIntArrayOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
