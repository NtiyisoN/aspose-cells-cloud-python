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


class Top10Filter(object):
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
        'items': 'int',
        'is_percent': 'bool',
        'is_top': 'bool',
        'criteria': 'str'
    }

    attribute_map = {
        'items': 'Items',
        'is_percent': 'IsPercent',
        'is_top': 'IsTop',
        'criteria': 'Criteria'
    }
    
    @staticmethod
    def get_swagger_types():
        return Top10Filter.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Top10Filter.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, items=None, is_percent=None, is_top=None, criteria=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Top10Filter - a model defined in Swagger
        """

        self.container['items'] = None
        self.container['is_percent'] = None
        self.container['is_top'] = None
        self.container['criteria'] = None

        self.items = items
        self.is_percent = is_percent
        self.is_top = is_top
        if criteria is not None:
          self.criteria = criteria

    @property
    def items(self):
        """
        Gets the items of this Top10Filter.

        :return: The items of this Top10Filter.
        :rtype: int
        """
        return self.container['items']

    @items.setter
    def items(self, items):
        """
        Sets the items of this Top10Filter.

        :param items: The items of this Top10Filter.
        :type: int
        """
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")
        """

        self.container['items'] = items

    @property
    def is_percent(self):
        """
        Gets the is_percent of this Top10Filter.

        :return: The is_percent of this Top10Filter.
        :rtype: bool
        """
        return self.container['is_percent']

    @is_percent.setter
    def is_percent(self, is_percent):
        """
        Sets the is_percent of this Top10Filter.

        :param is_percent: The is_percent of this Top10Filter.
        :type: bool
        """
        """
        if is_percent is None:
            raise ValueError("Invalid value for `is_percent`, must not be `None`")
        """

        self.container['is_percent'] = is_percent

    @property
    def is_top(self):
        """
        Gets the is_top of this Top10Filter.

        :return: The is_top of this Top10Filter.
        :rtype: bool
        """
        return self.container['is_top']

    @is_top.setter
    def is_top(self, is_top):
        """
        Sets the is_top of this Top10Filter.

        :param is_top: The is_top of this Top10Filter.
        :type: bool
        """
        """
        if is_top is None:
            raise ValueError("Invalid value for `is_top`, must not be `None`")
        """

        self.container['is_top'] = is_top

    @property
    def criteria(self):
        """
        Gets the criteria of this Top10Filter.

        :return: The criteria of this Top10Filter.
        :rtype: str
        """
        return self.container['criteria']

    @criteria.setter
    def criteria(self, criteria):
        """
        Sets the criteria of this Top10Filter.

        :param criteria: The criteria of this Top10Filter.
        :type: str
        """

        self.container['criteria'] = criteria

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
        if not isinstance(other, Top10Filter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
