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


class TextOptions(object):
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
        'color': 'Color',
        'double_size': 'float',
        'is_bold': 'bool',
        'is_italic': 'bool',
        'is_strikeout': 'bool',
        'is_subscript': 'bool',
        'is_superscript': 'bool',
        'name': 'str',
        'size': 'int',
        'underline': 'str',
        'fill': 'FillFormat',
        'kerning': 'float',
        'outline': 'LineFormat',
        'shadow': 'ShadowEffect',
        'spacing': 'float',
        'underline_color': 'CellsColor'
    }

    attribute_map = {
        'color': 'Color',
        'double_size': 'DoubleSize',
        'is_bold': 'IsBold',
        'is_italic': 'IsItalic',
        'is_strikeout': 'IsStrikeout',
        'is_subscript': 'IsSubscript',
        'is_superscript': 'IsSuperscript',
        'name': 'Name',
        'size': 'Size',
        'underline': 'Underline',
        'fill': 'Fill',
        'kerning': 'Kerning',
        'outline': 'Outline',
        'shadow': 'Shadow',
        'spacing': 'Spacing',
        'underline_color': 'UnderlineColor'
    }
    
    @staticmethod
    def get_swagger_types():
        return TextOptions.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return TextOptions.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, color=None, double_size=None, is_bold=None, is_italic=None, is_strikeout=None, is_subscript=None, is_superscript=None, name=None, size=None, underline=None, fill=None, kerning=None, outline=None, shadow=None, spacing=None, underline_color=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        TextOptions - a model defined in Swagger
        """

        self.container['color'] = None
        self.container['double_size'] = None
        self.container['is_bold'] = None
        self.container['is_italic'] = None
        self.container['is_strikeout'] = None
        self.container['is_subscript'] = None
        self.container['is_superscript'] = None
        self.container['name'] = None
        self.container['size'] = None
        self.container['underline'] = None
        self.container['fill'] = None
        self.container['kerning'] = None
        self.container['outline'] = None
        self.container['shadow'] = None
        self.container['spacing'] = None
        self.container['underline_color'] = None

        if color is not None:
          self.color = color
        if double_size is not None:
          self.double_size = double_size
        if is_bold is not None:
          self.is_bold = is_bold
        if is_italic is not None:
          self.is_italic = is_italic
        if is_strikeout is not None:
          self.is_strikeout = is_strikeout
        if is_subscript is not None:
          self.is_subscript = is_subscript
        if is_superscript is not None:
          self.is_superscript = is_superscript
        if name is not None:
          self.name = name
        if size is not None:
          self.size = size
        if underline is not None:
          self.underline = underline
        if fill is not None:
          self.fill = fill
        if kerning is not None:
          self.kerning = kerning
        if outline is not None:
          self.outline = outline
        if shadow is not None:
          self.shadow = shadow
        if spacing is not None:
          self.spacing = spacing
        if underline_color is not None:
          self.underline_color = underline_color

    @property
    def color(self):
        """
        Gets the color of this TextOptions.

        :return: The color of this TextOptions.
        :rtype: Color
        """
        return self.container['color']

    @color.setter
    def color(self, color):
        """
        Sets the color of this TextOptions.

        :param color: The color of this TextOptions.
        :type: Color
        """

        self.container['color'] = color

    @property
    def double_size(self):
        """
        Gets the double_size of this TextOptions.

        :return: The double_size of this TextOptions.
        :rtype: float
        """
        return self.container['double_size']

    @double_size.setter
    def double_size(self, double_size):
        """
        Sets the double_size of this TextOptions.

        :param double_size: The double_size of this TextOptions.
        :type: float
        """

        self.container['double_size'] = double_size

    @property
    def is_bold(self):
        """
        Gets the is_bold of this TextOptions.

        :return: The is_bold of this TextOptions.
        :rtype: bool
        """
        return self.container['is_bold']

    @is_bold.setter
    def is_bold(self, is_bold):
        """
        Sets the is_bold of this TextOptions.

        :param is_bold: The is_bold of this TextOptions.
        :type: bool
        """

        self.container['is_bold'] = is_bold

    @property
    def is_italic(self):
        """
        Gets the is_italic of this TextOptions.

        :return: The is_italic of this TextOptions.
        :rtype: bool
        """
        return self.container['is_italic']

    @is_italic.setter
    def is_italic(self, is_italic):
        """
        Sets the is_italic of this TextOptions.

        :param is_italic: The is_italic of this TextOptions.
        :type: bool
        """

        self.container['is_italic'] = is_italic

    @property
    def is_strikeout(self):
        """
        Gets the is_strikeout of this TextOptions.

        :return: The is_strikeout of this TextOptions.
        :rtype: bool
        """
        return self.container['is_strikeout']

    @is_strikeout.setter
    def is_strikeout(self, is_strikeout):
        """
        Sets the is_strikeout of this TextOptions.

        :param is_strikeout: The is_strikeout of this TextOptions.
        :type: bool
        """

        self.container['is_strikeout'] = is_strikeout

    @property
    def is_subscript(self):
        """
        Gets the is_subscript of this TextOptions.

        :return: The is_subscript of this TextOptions.
        :rtype: bool
        """
        return self.container['is_subscript']

    @is_subscript.setter
    def is_subscript(self, is_subscript):
        """
        Sets the is_subscript of this TextOptions.

        :param is_subscript: The is_subscript of this TextOptions.
        :type: bool
        """

        self.container['is_subscript'] = is_subscript

    @property
    def is_superscript(self):
        """
        Gets the is_superscript of this TextOptions.

        :return: The is_superscript of this TextOptions.
        :rtype: bool
        """
        return self.container['is_superscript']

    @is_superscript.setter
    def is_superscript(self, is_superscript):
        """
        Sets the is_superscript of this TextOptions.

        :param is_superscript: The is_superscript of this TextOptions.
        :type: bool
        """

        self.container['is_superscript'] = is_superscript

    @property
    def name(self):
        """
        Gets the name of this TextOptions.

        :return: The name of this TextOptions.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this TextOptions.

        :param name: The name of this TextOptions.
        :type: str
        """

        self.container['name'] = name

    @property
    def size(self):
        """
        Gets the size of this TextOptions.

        :return: The size of this TextOptions.
        :rtype: int
        """
        return self.container['size']

    @size.setter
    def size(self, size):
        """
        Sets the size of this TextOptions.

        :param size: The size of this TextOptions.
        :type: int
        """

        self.container['size'] = size

    @property
    def underline(self):
        """
        Gets the underline of this TextOptions.

        :return: The underline of this TextOptions.
        :rtype: str
        """
        return self.container['underline']

    @underline.setter
    def underline(self, underline):
        """
        Sets the underline of this TextOptions.

        :param underline: The underline of this TextOptions.
        :type: str
        """

        self.container['underline'] = underline

    @property
    def fill(self):
        """
        Gets the fill of this TextOptions.

        :return: The fill of this TextOptions.
        :rtype: FillFormat
        """
        return self.container['fill']

    @fill.setter
    def fill(self, fill):
        """
        Sets the fill of this TextOptions.

        :param fill: The fill of this TextOptions.
        :type: FillFormat
        """

        self.container['fill'] = fill

    @property
    def kerning(self):
        """
        Gets the kerning of this TextOptions.

        :return: The kerning of this TextOptions.
        :rtype: float
        """
        return self.container['kerning']

    @kerning.setter
    def kerning(self, kerning):
        """
        Sets the kerning of this TextOptions.

        :param kerning: The kerning of this TextOptions.
        :type: float
        """

        self.container['kerning'] = kerning

    @property
    def outline(self):
        """
        Gets the outline of this TextOptions.

        :return: The outline of this TextOptions.
        :rtype: LineFormat
        """
        return self.container['outline']

    @outline.setter
    def outline(self, outline):
        """
        Sets the outline of this TextOptions.

        :param outline: The outline of this TextOptions.
        :type: LineFormat
        """

        self.container['outline'] = outline

    @property
    def shadow(self):
        """
        Gets the shadow of this TextOptions.

        :return: The shadow of this TextOptions.
        :rtype: ShadowEffect
        """
        return self.container['shadow']

    @shadow.setter
    def shadow(self, shadow):
        """
        Sets the shadow of this TextOptions.

        :param shadow: The shadow of this TextOptions.
        :type: ShadowEffect
        """

        self.container['shadow'] = shadow

    @property
    def spacing(self):
        """
        Gets the spacing of this TextOptions.

        :return: The spacing of this TextOptions.
        :rtype: float
        """
        return self.container['spacing']

    @spacing.setter
    def spacing(self, spacing):
        """
        Sets the spacing of this TextOptions.

        :param spacing: The spacing of this TextOptions.
        :type: float
        """

        self.container['spacing'] = spacing

    @property
    def underline_color(self):
        """
        Gets the underline_color of this TextOptions.

        :return: The underline_color of this TextOptions.
        :rtype: CellsColor
        """
        return self.container['underline_color']

    @underline_color.setter
    def underline_color(self, underline_color):
        """
        Sets the underline_color of this TextOptions.

        :param underline_color: The underline_color of this TextOptions.
        :type: CellsColor
        """

        self.container['underline_color'] = underline_color

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
        if not isinstance(other, TextOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
