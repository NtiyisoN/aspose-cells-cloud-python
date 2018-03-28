# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Border(object):
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
        'line_style': 'str',
        'color': 'Color',
        'border_type': 'str'
    }

    attribute_map = {
        'line_style': 'LineStyle',
        'color': 'Color',
        'border_type': 'BorderType'
    }
    
    @staticmethod
    def get_swagger_types():
        return Border.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Border.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, line_style=None, color=None, border_type=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Border - a model defined in Swagger
        """

        self.container['line_style'] = None
        self.container['color'] = None
        self.container['border_type'] = None

        if line_style is not None:
          self.line_style = line_style
        if color is not None:
          self.color = color
        if border_type is not None:
          self.border_type = border_type

    @property
    def line_style(self):
        """
        Gets the line_style of this Border.

        :return: The line_style of this Border.
        :rtype: str
        """
        return self.container['line_style']

    @line_style.setter
    def line_style(self, line_style):
        """
        Sets the line_style of this Border.

        :param line_style: The line_style of this Border.
        :type: str
        """

        self.container['line_style'] = line_style

    @property
    def color(self):
        """
        Gets the color of this Border.

        :return: The color of this Border.
        :rtype: Color
        """
        return self.container['color']

    @color.setter
    def color(self, color):
        """
        Sets the color of this Border.

        :param color: The color of this Border.
        :type: Color
        """

        self.container['color'] = color

    @property
    def border_type(self):
        """
        Gets the border_type of this Border.

        :return: The border_type of this Border.
        :rtype: str
        """
        return self.container['border_type']

    @border_type.setter
    def border_type(self, border_type):
        """
        Sets the border_type of this Border.

        :param border_type: The border_type of this Border.
        :type: str
        """

        self.container['border_type'] = border_type

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
        if not isinstance(other, Border):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
