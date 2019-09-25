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


class PivotItem(object):
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
        'index': 'int',
        'is_hidden': 'bool',
        'name': 'str',
        'value': 'object'
    }

    attribute_map = {
        'index': 'Index',
        'is_hidden': 'IsHidden',
        'name': 'Name',
        'value': 'Value'
    }
    
    @staticmethod
    def get_swagger_types():
        return PivotItem.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return PivotItem.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, index=None, is_hidden=None, name=None, value=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        PivotItem - a model defined in Swagger
        """

        self.container['index'] = None
        self.container['is_hidden'] = None
        self.container['name'] = None
        self.container['value'] = None

        if index is not None:
          self.index = index
        if is_hidden is not None:
          self.is_hidden = is_hidden
        if name is not None:
          self.name = name
        if value is not None:
          self.value = value

    @property
    def index(self):
        """
        Gets the index of this PivotItem.

        :return: The index of this PivotItem.
        :rtype: int
        """
        return self.container['index']

    @index.setter
    def index(self, index):
        """
        Sets the index of this PivotItem.

        :param index: The index of this PivotItem.
        :type: int
        """

        self.container['index'] = index

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this PivotItem.
        Represents whether the specified item visible.

        :return: The is_hidden of this PivotItem.
        :rtype: bool
        """
        return self.container['is_hidden']

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this PivotItem.
        Represents whether the specified item visible.

        :param is_hidden: The is_hidden of this PivotItem.
        :type: bool
        """

        self.container['is_hidden'] = is_hidden

    @property
    def name(self):
        """
        Gets the name of this PivotItem.
        Gets the name

        :return: The name of this PivotItem.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this PivotItem.
        Gets the name

        :param name: The name of this PivotItem.
        :type: str
        """

        self.container['name'] = name

    @property
    def value(self):
        """
        Gets the value of this PivotItem.
        Gets the value of the specified item.

        :return: The value of this PivotItem.
        :rtype: object
        """
        return self.container['value']

    @value.setter
    def value(self, value):
        """
        Sets the value of this PivotItem.
        Gets the value of the specified item.

        :param value: The value of this PivotItem.
        :type: object
        """

        self.container['value'] = value

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
        if not isinstance(other, PivotItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
