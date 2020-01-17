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


class ConditionalFormattingValue(object):
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
        'is_gte': 'bool',
        'type': 'str',
        'value': 'object'
    }

    attribute_map = {
        'is_gte': 'IsGTE',
        'type': 'Type',
        'value': 'Value'
    }
    
    @staticmethod
    def get_swagger_types():
        return ConditionalFormattingValue.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return ConditionalFormattingValue.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, is_gte=None, type=None, value=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        ConditionalFormattingValue - a model defined in Swagger
        """

        self.container['is_gte'] = None
        self.container['type'] = None
        self.container['value'] = None

        if is_gte is not None:
          self.is_gte = is_gte
        if type is not None:
          self.type = type
        if value is not None:
          self.value = value

    @property
    def is_gte(self):
        """
        Gets the is_gte of this ConditionalFormattingValue.
        Get or set the Greater Than Or Equal flag. Use only for icon sets, determines    whether this threshold value uses the greater than or equal to operator.    'false' indicates 'greater than' is used instead of 'greater than or equal    to'.  Default value is true.             

        :return: The is_gte of this ConditionalFormattingValue.
        :rtype: bool
        """
        return self.container['is_gte']

    @is_gte.setter
    def is_gte(self, is_gte):
        """
        Sets the is_gte of this ConditionalFormattingValue.
        Get or set the Greater Than Or Equal flag. Use only for icon sets, determines    whether this threshold value uses the greater than or equal to operator.    'false' indicates 'greater than' is used instead of 'greater than or equal    to'.  Default value is true.             

        :param is_gte: The is_gte of this ConditionalFormattingValue.
        :type: bool
        """

        self.container['is_gte'] = is_gte

    @property
    def type(self):
        """
        Gets the type of this ConditionalFormattingValue.
        Get or set the type of this conditional formatting value object.  Setting      the type to FormatConditionValueType.Min or FormatConditionValueType.Max      will auto set \"Value\" to null.  

        :return: The type of this ConditionalFormattingValue.
        :rtype: str
        """
        return self.container['type']

    @type.setter
    def type(self, type):
        """
        Sets the type of this ConditionalFormattingValue.
        Get or set the type of this conditional formatting value object.  Setting      the type to FormatConditionValueType.Min or FormatConditionValueType.Max      will auto set \"Value\" to null.  

        :param type: The type of this ConditionalFormattingValue.
        :type: str
        """

        self.container['type'] = type

    @property
    def value(self):
        """
        Gets the value of this ConditionalFormattingValue.
        Get or set the value of this conditional formatting value object.  It should     be used in conjunction with Type.

        :return: The value of this ConditionalFormattingValue.
        :rtype: object
        """
        return self.container['value']

    @value.setter
    def value(self, value):
        """
        Sets the value of this ConditionalFormattingValue.
        Get or set the value of this conditional formatting value object.  It should     be used in conjunction with Type.

        :param value: The value of this ConditionalFormattingValue.
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
        if not isinstance(other, ConditionalFormattingValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
