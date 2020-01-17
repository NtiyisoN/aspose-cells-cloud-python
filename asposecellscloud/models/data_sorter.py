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


class DataSorter(object):
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
        'case_sensitive': 'bool',
        'key_list': 'list[SortKey]',
        'has_headers': 'bool',
        'sort_left_to_right': 'bool'
    }

    attribute_map = {
        'case_sensitive': 'CaseSensitive',
        'key_list': 'KeyList',
        'has_headers': 'HasHeaders',
        'sort_left_to_right': 'SortLeftToRight'
    }
    
    @staticmethod
    def get_swagger_types():
        return DataSorter.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return DataSorter.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, case_sensitive=None, key_list=None, has_headers=None, sort_left_to_right=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        DataSorter - a model defined in Swagger
        """

        self.container['case_sensitive'] = None
        self.container['key_list'] = None
        self.container['has_headers'] = None
        self.container['sort_left_to_right'] = None

        if case_sensitive is not None:
          self.case_sensitive = case_sensitive
        if key_list is not None:
          self.key_list = key_list
        if has_headers is not None:
          self.has_headers = has_headers
        if sort_left_to_right is not None:
          self.sort_left_to_right = sort_left_to_right

    @property
    def case_sensitive(self):
        """
        Gets the case_sensitive of this DataSorter.

        :return: The case_sensitive of this DataSorter.
        :rtype: bool
        """
        return self.container['case_sensitive']

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        """
        Sets the case_sensitive of this DataSorter.

        :param case_sensitive: The case_sensitive of this DataSorter.
        :type: bool
        """

        self.container['case_sensitive'] = case_sensitive

    @property
    def key_list(self):
        """
        Gets the key_list of this DataSorter.

        :return: The key_list of this DataSorter.
        :rtype: list[SortKey]
        """
        return self.container['key_list']

    @key_list.setter
    def key_list(self, key_list):
        """
        Sets the key_list of this DataSorter.

        :param key_list: The key_list of this DataSorter.
        :type: list[SortKey]
        """

        self.container['key_list'] = key_list

    @property
    def has_headers(self):
        """
        Gets the has_headers of this DataSorter.

        :return: The has_headers of this DataSorter.
        :rtype: bool
        """
        return self.container['has_headers']

    @has_headers.setter
    def has_headers(self, has_headers):
        """
        Sets the has_headers of this DataSorter.

        :param has_headers: The has_headers of this DataSorter.
        :type: bool
        """

        self.container['has_headers'] = has_headers

    @property
    def sort_left_to_right(self):
        """
        Gets the sort_left_to_right of this DataSorter.

        :return: The sort_left_to_right of this DataSorter.
        :rtype: bool
        """
        return self.container['sort_left_to_right']

    @sort_left_to_right.setter
    def sort_left_to_right(self, sort_left_to_right):
        """
        Sets the sort_left_to_right of this DataSorter.

        :param sort_left_to_right: The sort_left_to_right of this DataSorter.
        :type: bool
        """

        self.container['sort_left_to_right'] = sort_left_to_right

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
        if not isinstance(other, DataSorter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
