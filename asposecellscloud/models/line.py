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


class Line(object):
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
        'style': 'str',
        'is_auto': 'bool',
        'begin_arrow_length': 'str',
        'weight': 'str',
        'gradient_fill': 'GradientFill',
        'color': 'Color',
        'compound_type': 'str',
        'weight_pt': 'float',
        'is_visible': 'bool',
        'join_type': 'str',
        'end_arrow_length': 'str',
        'is_automatic_color': 'bool',
        'dash_type': 'str',
        'begin_type': 'str',
        'cap_type': 'str',
        'end_type': 'str',
        'begin_arrow_width': 'str',
        'end_arrow_width': 'str',
        'transparency': 'float'
    }

    attribute_map = {
        'style': 'Style',
        'is_auto': 'IsAuto',
        'begin_arrow_length': 'BeginArrowLength',
        'weight': 'Weight',
        'gradient_fill': 'GradientFill',
        'color': 'Color',
        'compound_type': 'CompoundType',
        'weight_pt': 'WeightPt',
        'is_visible': 'IsVisible',
        'join_type': 'JoinType',
        'end_arrow_length': 'EndArrowLength',
        'is_automatic_color': 'IsAutomaticColor',
        'dash_type': 'DashType',
        'begin_type': 'BeginType',
        'cap_type': 'CapType',
        'end_type': 'EndType',
        'begin_arrow_width': 'BeginArrowWidth',
        'end_arrow_width': 'EndArrowWidth',
        'transparency': 'Transparency'
    }
    
    @staticmethod
    def get_swagger_types():
        return Line.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Line.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, style=None, is_auto=None, begin_arrow_length=None, weight=None, gradient_fill=None, color=None, compound_type=None, weight_pt=None, is_visible=None, join_type=None, end_arrow_length=None, is_automatic_color=None, dash_type=None, begin_type=None, cap_type=None, end_type=None, begin_arrow_width=None, end_arrow_width=None, transparency=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Line - a model defined in Swagger
        """

        self.container['style'] = None
        self.container['is_auto'] = None
        self.container['begin_arrow_length'] = None
        self.container['weight'] = None
        self.container['gradient_fill'] = None
        self.container['color'] = None
        self.container['compound_type'] = None
        self.container['weight_pt'] = None
        self.container['is_visible'] = None
        self.container['join_type'] = None
        self.container['end_arrow_length'] = None
        self.container['is_automatic_color'] = None
        self.container['dash_type'] = None
        self.container['begin_type'] = None
        self.container['cap_type'] = None
        self.container['end_type'] = None
        self.container['begin_arrow_width'] = None
        self.container['end_arrow_width'] = None
        self.container['transparency'] = None

        if style is not None:
          self.style = style
        if is_auto is not None:
          self.is_auto = is_auto
        if begin_arrow_length is not None:
          self.begin_arrow_length = begin_arrow_length
        if weight is not None:
          self.weight = weight
        if gradient_fill is not None:
          self.gradient_fill = gradient_fill
        if color is not None:
          self.color = color
        if compound_type is not None:
          self.compound_type = compound_type
        if weight_pt is not None:
          self.weight_pt = weight_pt
        if is_visible is not None:
          self.is_visible = is_visible
        if join_type is not None:
          self.join_type = join_type
        if end_arrow_length is not None:
          self.end_arrow_length = end_arrow_length
        if is_automatic_color is not None:
          self.is_automatic_color = is_automatic_color
        if dash_type is not None:
          self.dash_type = dash_type
        if begin_type is not None:
          self.begin_type = begin_type
        if cap_type is not None:
          self.cap_type = cap_type
        if end_type is not None:
          self.end_type = end_type
        if begin_arrow_width is not None:
          self.begin_arrow_width = begin_arrow_width
        if end_arrow_width is not None:
          self.end_arrow_width = end_arrow_width
        if transparency is not None:
          self.transparency = transparency

    @property
    def style(self):
        """
        Gets the style of this Line.

        :return: The style of this Line.
        :rtype: str
        """
        return self.container['style']

    @style.setter
    def style(self, style):
        """
        Sets the style of this Line.

        :param style: The style of this Line.
        :type: str
        """

        self.container['style'] = style

    @property
    def is_auto(self):
        """
        Gets the is_auto of this Line.

        :return: The is_auto of this Line.
        :rtype: bool
        """
        return self.container['is_auto']

    @is_auto.setter
    def is_auto(self, is_auto):
        """
        Sets the is_auto of this Line.

        :param is_auto: The is_auto of this Line.
        :type: bool
        """

        self.container['is_auto'] = is_auto

    @property
    def begin_arrow_length(self):
        """
        Gets the begin_arrow_length of this Line.

        :return: The begin_arrow_length of this Line.
        :rtype: str
        """
        return self.container['begin_arrow_length']

    @begin_arrow_length.setter
    def begin_arrow_length(self, begin_arrow_length):
        """
        Sets the begin_arrow_length of this Line.

        :param begin_arrow_length: The begin_arrow_length of this Line.
        :type: str
        """

        self.container['begin_arrow_length'] = begin_arrow_length

    @property
    def weight(self):
        """
        Gets the weight of this Line.

        :return: The weight of this Line.
        :rtype: str
        """
        return self.container['weight']

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this Line.

        :param weight: The weight of this Line.
        :type: str
        """

        self.container['weight'] = weight

    @property
    def gradient_fill(self):
        """
        Gets the gradient_fill of this Line.

        :return: The gradient_fill of this Line.
        :rtype: GradientFill
        """
        return self.container['gradient_fill']

    @gradient_fill.setter
    def gradient_fill(self, gradient_fill):
        """
        Sets the gradient_fill of this Line.

        :param gradient_fill: The gradient_fill of this Line.
        :type: GradientFill
        """

        self.container['gradient_fill'] = gradient_fill

    @property
    def color(self):
        """
        Gets the color of this Line.

        :return: The color of this Line.
        :rtype: Color
        """
        return self.container['color']

    @color.setter
    def color(self, color):
        """
        Sets the color of this Line.

        :param color: The color of this Line.
        :type: Color
        """

        self.container['color'] = color

    @property
    def compound_type(self):
        """
        Gets the compound_type of this Line.

        :return: The compound_type of this Line.
        :rtype: str
        """
        return self.container['compound_type']

    @compound_type.setter
    def compound_type(self, compound_type):
        """
        Sets the compound_type of this Line.

        :param compound_type: The compound_type of this Line.
        :type: str
        """

        self.container['compound_type'] = compound_type

    @property
    def weight_pt(self):
        """
        Gets the weight_pt of this Line.

        :return: The weight_pt of this Line.
        :rtype: float
        """
        return self.container['weight_pt']

    @weight_pt.setter
    def weight_pt(self, weight_pt):
        """
        Sets the weight_pt of this Line.

        :param weight_pt: The weight_pt of this Line.
        :type: float
        """

        self.container['weight_pt'] = weight_pt

    @property
    def is_visible(self):
        """
        Gets the is_visible of this Line.

        :return: The is_visible of this Line.
        :rtype: bool
        """
        return self.container['is_visible']

    @is_visible.setter
    def is_visible(self, is_visible):
        """
        Sets the is_visible of this Line.

        :param is_visible: The is_visible of this Line.
        :type: bool
        """

        self.container['is_visible'] = is_visible

    @property
    def join_type(self):
        """
        Gets the join_type of this Line.

        :return: The join_type of this Line.
        :rtype: str
        """
        return self.container['join_type']

    @join_type.setter
    def join_type(self, join_type):
        """
        Sets the join_type of this Line.

        :param join_type: The join_type of this Line.
        :type: str
        """

        self.container['join_type'] = join_type

    @property
    def end_arrow_length(self):
        """
        Gets the end_arrow_length of this Line.

        :return: The end_arrow_length of this Line.
        :rtype: str
        """
        return self.container['end_arrow_length']

    @end_arrow_length.setter
    def end_arrow_length(self, end_arrow_length):
        """
        Sets the end_arrow_length of this Line.

        :param end_arrow_length: The end_arrow_length of this Line.
        :type: str
        """

        self.container['end_arrow_length'] = end_arrow_length

    @property
    def is_automatic_color(self):
        """
        Gets the is_automatic_color of this Line.

        :return: The is_automatic_color of this Line.
        :rtype: bool
        """
        return self.container['is_automatic_color']

    @is_automatic_color.setter
    def is_automatic_color(self, is_automatic_color):
        """
        Sets the is_automatic_color of this Line.

        :param is_automatic_color: The is_automatic_color of this Line.
        :type: bool
        """

        self.container['is_automatic_color'] = is_automatic_color

    @property
    def dash_type(self):
        """
        Gets the dash_type of this Line.

        :return: The dash_type of this Line.
        :rtype: str
        """
        return self.container['dash_type']

    @dash_type.setter
    def dash_type(self, dash_type):
        """
        Sets the dash_type of this Line.

        :param dash_type: The dash_type of this Line.
        :type: str
        """

        self.container['dash_type'] = dash_type

    @property
    def begin_type(self):
        """
        Gets the begin_type of this Line.

        :return: The begin_type of this Line.
        :rtype: str
        """
        return self.container['begin_type']

    @begin_type.setter
    def begin_type(self, begin_type):
        """
        Sets the begin_type of this Line.

        :param begin_type: The begin_type of this Line.
        :type: str
        """

        self.container['begin_type'] = begin_type

    @property
    def cap_type(self):
        """
        Gets the cap_type of this Line.

        :return: The cap_type of this Line.
        :rtype: str
        """
        return self.container['cap_type']

    @cap_type.setter
    def cap_type(self, cap_type):
        """
        Sets the cap_type of this Line.

        :param cap_type: The cap_type of this Line.
        :type: str
        """

        self.container['cap_type'] = cap_type

    @property
    def end_type(self):
        """
        Gets the end_type of this Line.

        :return: The end_type of this Line.
        :rtype: str
        """
        return self.container['end_type']

    @end_type.setter
    def end_type(self, end_type):
        """
        Sets the end_type of this Line.

        :param end_type: The end_type of this Line.
        :type: str
        """

        self.container['end_type'] = end_type

    @property
    def begin_arrow_width(self):
        """
        Gets the begin_arrow_width of this Line.

        :return: The begin_arrow_width of this Line.
        :rtype: str
        """
        return self.container['begin_arrow_width']

    @begin_arrow_width.setter
    def begin_arrow_width(self, begin_arrow_width):
        """
        Sets the begin_arrow_width of this Line.

        :param begin_arrow_width: The begin_arrow_width of this Line.
        :type: str
        """

        self.container['begin_arrow_width'] = begin_arrow_width

    @property
    def end_arrow_width(self):
        """
        Gets the end_arrow_width of this Line.

        :return: The end_arrow_width of this Line.
        :rtype: str
        """
        return self.container['end_arrow_width']

    @end_arrow_width.setter
    def end_arrow_width(self, end_arrow_width):
        """
        Sets the end_arrow_width of this Line.

        :param end_arrow_width: The end_arrow_width of this Line.
        :type: str
        """

        self.container['end_arrow_width'] = end_arrow_width

    @property
    def transparency(self):
        """
        Gets the transparency of this Line.

        :return: The transparency of this Line.
        :rtype: float
        """
        return self.container['transparency']

    @transparency.setter
    def transparency(self, transparency):
        """
        Sets the transparency of this Line.

        :param transparency: The transparency of this Line.
        :type: float
        """

        self.container['transparency'] = transparency

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
        if not isinstance(other, Line):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
