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


class Title(object):
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
        'area': 'Area',
        'auto_scale_font': 'bool',
        'background_mode': 'str',
        'border': 'Line',
        'font': 'Font',
        'is_automatic_size': 'bool',
        'is_inner_mode': 'bool',
        'shadow': 'bool',
        'shape_properties': 'list[LinkElement]',
        'width': 'int',
        'height': 'int',
        'x': 'int',
        'y': 'int',
        'link': 'Link',
        'is_visible': 'bool',
        'linked_source': 'str',
        'rotation_angle': 'int',
        'text': 'str',
        'text_direction': 'str',
        'text_horizontal_alignment': 'str',
        'text_vertical_alignment': 'str'
    }

    attribute_map = {
        'area': 'Area',
        'auto_scale_font': 'AutoScaleFont',
        'background_mode': 'BackgroundMode',
        'border': 'Border',
        'font': 'Font',
        'is_automatic_size': 'IsAutomaticSize',
        'is_inner_mode': 'IsInnerMode',
        'shadow': 'Shadow',
        'shape_properties': 'ShapeProperties',
        'width': 'Width',
        'height': 'Height',
        'x': 'X',
        'y': 'Y',
        'link': 'link',
        'is_visible': 'IsVisible',
        'linked_source': 'LinkedSource',
        'rotation_angle': 'RotationAngle',
        'text': 'Text',
        'text_direction': 'TextDirection',
        'text_horizontal_alignment': 'TextHorizontalAlignment',
        'text_vertical_alignment': 'TextVerticalAlignment'
    }
    
    @staticmethod
    def get_swagger_types():
        return Title.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Title.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, area=None, auto_scale_font=None, background_mode=None, border=None, font=None, is_automatic_size=None, is_inner_mode=None, shadow=None, shape_properties=None, width=None, height=None, x=None, y=None, link=None, is_visible=None, linked_source=None, rotation_angle=None, text=None, text_direction=None, text_horizontal_alignment=None, text_vertical_alignment=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Title - a model defined in Swagger
        """

        self.container['area'] = None
        self.container['auto_scale_font'] = None
        self.container['background_mode'] = None
        self.container['border'] = None
        self.container['font'] = None
        self.container['is_automatic_size'] = None
        self.container['is_inner_mode'] = None
        self.container['shadow'] = None
        self.container['shape_properties'] = None
        self.container['width'] = None
        self.container['height'] = None
        self.container['x'] = None
        self.container['y'] = None
        self.container['link'] = None
        self.container['is_visible'] = None
        self.container['linked_source'] = None
        self.container['rotation_angle'] = None
        self.container['text'] = None
        self.container['text_direction'] = None
        self.container['text_horizontal_alignment'] = None
        self.container['text_vertical_alignment'] = None

        if area is not None:
          self.area = area
        if auto_scale_font is not None:
          self.auto_scale_font = auto_scale_font
        if background_mode is not None:
          self.background_mode = background_mode
        if border is not None:
          self.border = border
        if font is not None:
          self.font = font
        if is_automatic_size is not None:
          self.is_automatic_size = is_automatic_size
        if is_inner_mode is not None:
          self.is_inner_mode = is_inner_mode
        if shadow is not None:
          self.shadow = shadow
        if shape_properties is not None:
          self.shape_properties = shape_properties
        if width is not None:
          self.width = width
        if height is not None:
          self.height = height
        if x is not None:
          self.x = x
        if y is not None:
          self.y = y
        if link is not None:
          self.link = link
        if is_visible is not None:
          self.is_visible = is_visible
        if linked_source is not None:
          self.linked_source = linked_source
        if rotation_angle is not None:
          self.rotation_angle = rotation_angle
        if text is not None:
          self.text = text
        if text_direction is not None:
          self.text_direction = text_direction
        if text_horizontal_alignment is not None:
          self.text_horizontal_alignment = text_horizontal_alignment
        if text_vertical_alignment is not None:
          self.text_vertical_alignment = text_vertical_alignment

    @property
    def area(self):
        """
        Gets the area of this Title.

        :return: The area of this Title.
        :rtype: Area
        """
        return self.container['area']

    @area.setter
    def area(self, area):
        """
        Sets the area of this Title.

        :param area: The area of this Title.
        :type: Area
        """

        self.container['area'] = area

    @property
    def auto_scale_font(self):
        """
        Gets the auto_scale_font of this Title.

        :return: The auto_scale_font of this Title.
        :rtype: bool
        """
        return self.container['auto_scale_font']

    @auto_scale_font.setter
    def auto_scale_font(self, auto_scale_font):
        """
        Sets the auto_scale_font of this Title.

        :param auto_scale_font: The auto_scale_font of this Title.
        :type: bool
        """

        self.container['auto_scale_font'] = auto_scale_font

    @property
    def background_mode(self):
        """
        Gets the background_mode of this Title.

        :return: The background_mode of this Title.
        :rtype: str
        """
        return self.container['background_mode']

    @background_mode.setter
    def background_mode(self, background_mode):
        """
        Sets the background_mode of this Title.

        :param background_mode: The background_mode of this Title.
        :type: str
        """

        self.container['background_mode'] = background_mode

    @property
    def border(self):
        """
        Gets the border of this Title.

        :return: The border of this Title.
        :rtype: Line
        """
        return self.container['border']

    @border.setter
    def border(self, border):
        """
        Sets the border of this Title.

        :param border: The border of this Title.
        :type: Line
        """

        self.container['border'] = border

    @property
    def font(self):
        """
        Gets the font of this Title.

        :return: The font of this Title.
        :rtype: Font
        """
        return self.container['font']

    @font.setter
    def font(self, font):
        """
        Sets the font of this Title.

        :param font: The font of this Title.
        :type: Font
        """

        self.container['font'] = font

    @property
    def is_automatic_size(self):
        """
        Gets the is_automatic_size of this Title.

        :return: The is_automatic_size of this Title.
        :rtype: bool
        """
        return self.container['is_automatic_size']

    @is_automatic_size.setter
    def is_automatic_size(self, is_automatic_size):
        """
        Sets the is_automatic_size of this Title.

        :param is_automatic_size: The is_automatic_size of this Title.
        :type: bool
        """

        self.container['is_automatic_size'] = is_automatic_size

    @property
    def is_inner_mode(self):
        """
        Gets the is_inner_mode of this Title.

        :return: The is_inner_mode of this Title.
        :rtype: bool
        """
        return self.container['is_inner_mode']

    @is_inner_mode.setter
    def is_inner_mode(self, is_inner_mode):
        """
        Sets the is_inner_mode of this Title.

        :param is_inner_mode: The is_inner_mode of this Title.
        :type: bool
        """

        self.container['is_inner_mode'] = is_inner_mode

    @property
    def shadow(self):
        """
        Gets the shadow of this Title.

        :return: The shadow of this Title.
        :rtype: bool
        """
        return self.container['shadow']

    @shadow.setter
    def shadow(self, shadow):
        """
        Sets the shadow of this Title.

        :param shadow: The shadow of this Title.
        :type: bool
        """

        self.container['shadow'] = shadow

    @property
    def shape_properties(self):
        """
        Gets the shape_properties of this Title.

        :return: The shape_properties of this Title.
        :rtype: list[LinkElement]
        """
        return self.container['shape_properties']

    @shape_properties.setter
    def shape_properties(self, shape_properties):
        """
        Sets the shape_properties of this Title.

        :param shape_properties: The shape_properties of this Title.
        :type: list[LinkElement]
        """

        self.container['shape_properties'] = shape_properties

    @property
    def width(self):
        """
        Gets the width of this Title.

        :return: The width of this Title.
        :rtype: int
        """
        return self.container['width']

    @width.setter
    def width(self, width):
        """
        Sets the width of this Title.

        :param width: The width of this Title.
        :type: int
        """

        self.container['width'] = width

    @property
    def height(self):
        """
        Gets the height of this Title.

        :return: The height of this Title.
        :rtype: int
        """
        return self.container['height']

    @height.setter
    def height(self, height):
        """
        Sets the height of this Title.

        :param height: The height of this Title.
        :type: int
        """

        self.container['height'] = height

    @property
    def x(self):
        """
        Gets the x of this Title.

        :return: The x of this Title.
        :rtype: int
        """
        return self.container['x']

    @x.setter
    def x(self, x):
        """
        Sets the x of this Title.

        :param x: The x of this Title.
        :type: int
        """

        self.container['x'] = x

    @property
    def y(self):
        """
        Gets the y of this Title.

        :return: The y of this Title.
        :rtype: int
        """
        return self.container['y']

    @y.setter
    def y(self, y):
        """
        Sets the y of this Title.

        :param y: The y of this Title.
        :type: int
        """

        self.container['y'] = y

    @property
    def link(self):
        """
        Gets the link of this Title.

        :return: The link of this Title.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Title.

        :param link: The link of this Title.
        :type: Link
        """

        self.container['link'] = link

    @property
    def is_visible(self):
        """
        Gets the is_visible of this Title.

        :return: The is_visible of this Title.
        :rtype: bool
        """
        return self.container['is_visible']

    @is_visible.setter
    def is_visible(self, is_visible):
        """
        Sets the is_visible of this Title.

        :param is_visible: The is_visible of this Title.
        :type: bool
        """

        self.container['is_visible'] = is_visible

    @property
    def linked_source(self):
        """
        Gets the linked_source of this Title.

        :return: The linked_source of this Title.
        :rtype: str
        """
        return self.container['linked_source']

    @linked_source.setter
    def linked_source(self, linked_source):
        """
        Sets the linked_source of this Title.

        :param linked_source: The linked_source of this Title.
        :type: str
        """

        self.container['linked_source'] = linked_source

    @property
    def rotation_angle(self):
        """
        Gets the rotation_angle of this Title.

        :return: The rotation_angle of this Title.
        :rtype: int
        """
        return self.container['rotation_angle']

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle):
        """
        Sets the rotation_angle of this Title.

        :param rotation_angle: The rotation_angle of this Title.
        :type: int
        """

        self.container['rotation_angle'] = rotation_angle

    @property
    def text(self):
        """
        Gets the text of this Title.

        :return: The text of this Title.
        :rtype: str
        """
        return self.container['text']

    @text.setter
    def text(self, text):
        """
        Sets the text of this Title.

        :param text: The text of this Title.
        :type: str
        """

        self.container['text'] = text

    @property
    def text_direction(self):
        """
        Gets the text_direction of this Title.

        :return: The text_direction of this Title.
        :rtype: str
        """
        return self.container['text_direction']

    @text_direction.setter
    def text_direction(self, text_direction):
        """
        Sets the text_direction of this Title.

        :param text_direction: The text_direction of this Title.
        :type: str
        """

        self.container['text_direction'] = text_direction

    @property
    def text_horizontal_alignment(self):
        """
        Gets the text_horizontal_alignment of this Title.

        :return: The text_horizontal_alignment of this Title.
        :rtype: str
        """
        return self.container['text_horizontal_alignment']

    @text_horizontal_alignment.setter
    def text_horizontal_alignment(self, text_horizontal_alignment):
        """
        Sets the text_horizontal_alignment of this Title.

        :param text_horizontal_alignment: The text_horizontal_alignment of this Title.
        :type: str
        """

        self.container['text_horizontal_alignment'] = text_horizontal_alignment

    @property
    def text_vertical_alignment(self):
        """
        Gets the text_vertical_alignment of this Title.

        :return: The text_vertical_alignment of this Title.
        :rtype: str
        """
        return self.container['text_vertical_alignment']

    @text_vertical_alignment.setter
    def text_vertical_alignment(self, text_vertical_alignment):
        """
        Sets the text_vertical_alignment of this Title.

        :param text_vertical_alignment: The text_vertical_alignment of this Title.
        :type: str
        """

        self.container['text_vertical_alignment'] = text_vertical_alignment

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
        if not isinstance(other, Title):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
