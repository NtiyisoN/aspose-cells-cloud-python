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


class PatternFill(object):
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
        'foreground_color': 'Color',
        'pattern': 'str',
        'background_color': 'Color',
        'back_transparency': 'float',
        'background_cells_color': 'CellsColor',
        'fore_transparency': 'float',
        'foreground_cells_color': 'CellsColor'
    }

    attribute_map = {
        'foreground_color': 'ForegroundColor',
        'pattern': 'Pattern',
        'background_color': 'BackgroundColor',
        'back_transparency': 'BackTransparency',
        'background_cells_color': 'BackgroundCellsColor',
        'fore_transparency': 'ForeTransparency',
        'foreground_cells_color': 'ForegroundCellsColor'
    }
    
    @staticmethod
    def get_swagger_types():
        return PatternFill.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return PatternFill.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, foreground_color=None, pattern=None, background_color=None, back_transparency=None, background_cells_color=None, fore_transparency=None, foreground_cells_color=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        PatternFill - a model defined in Swagger
        """

        self.container['foreground_color'] = None
        self.container['pattern'] = None
        self.container['background_color'] = None
        self.container['back_transparency'] = None
        self.container['background_cells_color'] = None
        self.container['fore_transparency'] = None
        self.container['foreground_cells_color'] = None

        if foreground_color is not None:
          self.foreground_color = foreground_color
        if pattern is not None:
          self.pattern = pattern
        if background_color is not None:
          self.background_color = background_color
        if back_transparency is not None:
          self.back_transparency = back_transparency
        if background_cells_color is not None:
          self.background_cells_color = background_cells_color
        if fore_transparency is not None:
          self.fore_transparency = fore_transparency
        if foreground_cells_color is not None:
          self.foreground_cells_color = foreground_cells_color

    @property
    def foreground_color(self):
        """
        Gets the foreground_color of this PatternFill.

        :return: The foreground_color of this PatternFill.
        :rtype: Color
        """
        return self.container['foreground_color']

    @foreground_color.setter
    def foreground_color(self, foreground_color):
        """
        Sets the foreground_color of this PatternFill.

        :param foreground_color: The foreground_color of this PatternFill.
        :type: Color
        """

        self.container['foreground_color'] = foreground_color

    @property
    def pattern(self):
        """
        Gets the pattern of this PatternFill.

        :return: The pattern of this PatternFill.
        :rtype: str
        """
        return self.container['pattern']

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this PatternFill.

        :param pattern: The pattern of this PatternFill.
        :type: str
        """

        self.container['pattern'] = pattern

    @property
    def background_color(self):
        """
        Gets the background_color of this PatternFill.

        :return: The background_color of this PatternFill.
        :rtype: Color
        """
        return self.container['background_color']

    @background_color.setter
    def background_color(self, background_color):
        """
        Sets the background_color of this PatternFill.

        :param background_color: The background_color of this PatternFill.
        :type: Color
        """

        self.container['background_color'] = background_color

    @property
    def back_transparency(self):
        """
        Gets the back_transparency of this PatternFill.

        :return: The back_transparency of this PatternFill.
        :rtype: float
        """
        return self.container['back_transparency']

    @back_transparency.setter
    def back_transparency(self, back_transparency):
        """
        Sets the back_transparency of this PatternFill.

        :param back_transparency: The back_transparency of this PatternFill.
        :type: float
        """

        self.container['back_transparency'] = back_transparency

    @property
    def background_cells_color(self):
        """
        Gets the background_cells_color of this PatternFill.

        :return: The background_cells_color of this PatternFill.
        :rtype: CellsColor
        """
        return self.container['background_cells_color']

    @background_cells_color.setter
    def background_cells_color(self, background_cells_color):
        """
        Sets the background_cells_color of this PatternFill.

        :param background_cells_color: The background_cells_color of this PatternFill.
        :type: CellsColor
        """

        self.container['background_cells_color'] = background_cells_color

    @property
    def fore_transparency(self):
        """
        Gets the fore_transparency of this PatternFill.

        :return: The fore_transparency of this PatternFill.
        :rtype: float
        """
        return self.container['fore_transparency']

    @fore_transparency.setter
    def fore_transparency(self, fore_transparency):
        """
        Sets the fore_transparency of this PatternFill.

        :param fore_transparency: The fore_transparency of this PatternFill.
        :type: float
        """

        self.container['fore_transparency'] = fore_transparency

    @property
    def foreground_cells_color(self):
        """
        Gets the foreground_cells_color of this PatternFill.

        :return: The foreground_cells_color of this PatternFill.
        :rtype: CellsColor
        """
        return self.container['foreground_cells_color']

    @foreground_cells_color.setter
    def foreground_cells_color(self, foreground_cells_color):
        """
        Sets the foreground_cells_color of this PatternFill.

        :param foreground_cells_color: The foreground_cells_color of this PatternFill.
        :type: CellsColor
        """

        self.container['foreground_cells_color'] = foreground_cells_color

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
        if not isinstance(other, PatternFill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
