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


class VerticalPageBreak(object):
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
        'column': 'int',
        'start_row': 'int',
        'end_row': 'int'
    }

    attribute_map = {
        'column': 'Column',
        'start_row': 'StartRow',
        'end_row': 'EndRow'
    }
    
    @staticmethod
    def get_swagger_types():
        return VerticalPageBreak.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return VerticalPageBreak.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, column=None, start_row=None, end_row=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        VerticalPageBreak - a model defined in Swagger
        """

        self.container['column'] = None
        self.container['start_row'] = None
        self.container['end_row'] = None

        self.column = column
        self.start_row = start_row
        self.end_row = end_row

    @property
    def column(self):
        """
        Gets the column of this VerticalPageBreak.

        :return: The column of this VerticalPageBreak.
        :rtype: int
        """
        return self.container['column']

    @column.setter
    def column(self, column):
        """
        Sets the column of this VerticalPageBreak.

        :param column: The column of this VerticalPageBreak.
        :type: int
        """
        """
        if column is None:
            raise ValueError("Invalid value for `column`, must not be `None`")
        """

        self.container['column'] = column

    @property
    def start_row(self):
        """
        Gets the start_row of this VerticalPageBreak.

        :return: The start_row of this VerticalPageBreak.
        :rtype: int
        """
        return self.container['start_row']

    @start_row.setter
    def start_row(self, start_row):
        """
        Sets the start_row of this VerticalPageBreak.

        :param start_row: The start_row of this VerticalPageBreak.
        :type: int
        """
        """
        if start_row is None:
            raise ValueError("Invalid value for `start_row`, must not be `None`")
        """

        self.container['start_row'] = start_row

    @property
    def end_row(self):
        """
        Gets the end_row of this VerticalPageBreak.

        :return: The end_row of this VerticalPageBreak.
        :rtype: int
        """
        return self.container['end_row']

    @end_row.setter
    def end_row(self, end_row):
        """
        Sets the end_row of this VerticalPageBreak.

        :param end_row: The end_row of this VerticalPageBreak.
        :type: int
        """
        """
        if end_row is None:
            raise ValueError("Invalid value for `end_row`, must not be `None`")
        """

        self.container['end_row'] = end_row

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
        if not isinstance(other, VerticalPageBreak):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
