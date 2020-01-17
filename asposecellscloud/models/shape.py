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


class Shape(object):
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
        'link': 'Link',
        'alternative_text': 'str',
        'bottom': 'int',
        'top': 'int',
        'width': 'int',
        'html_text': 'str',
        'text_vertical_alignment': 'str',
        'auto_shape_type': 'str',
        'is_printable': 'bool',
        'upper_left_column': 'int',
        'is_lock_aspect_ratio': 'bool',
        'is_group': 'bool',
        'rotation_angle': 'float',
        'z_order_position': 'int',
        'text_horizontal_overflow': 'str',
        'mso_drawing_type': 'str',
        'text_orientation_type': 'str',
        'placement': 'str',
        'name': 'str',
        'is_word_art': 'bool',
        'linked_cell': 'str',
        'upper_left_row': 'int',
        'is_locked': 'bool',
        'lower_right_row': 'int',
        'is_text_wrapped': 'bool',
        'y': 'int',
        'x': 'int',
        'is_hidden': 'bool',
        'left': 'int',
        'right': 'int',
        'text': 'str',
        'lower_right_column': 'int',
        'height': 'int',
        'text_horizontal_alignment': 'str',
        'text_vertical_overflow': 'str'
    }

    attribute_map = {
        'link': 'link',
        'alternative_text': 'AlternativeText',
        'bottom': 'Bottom',
        'top': 'Top',
        'width': 'Width',
        'html_text': 'HtmlText',
        'text_vertical_alignment': 'TextVerticalAlignment',
        'auto_shape_type': 'AutoShapeType',
        'is_printable': 'IsPrintable',
        'upper_left_column': 'UpperLeftColumn',
        'is_lock_aspect_ratio': 'IsLockAspectRatio',
        'is_group': 'IsGroup',
        'rotation_angle': 'RotationAngle',
        'z_order_position': 'ZOrderPosition',
        'text_horizontal_overflow': 'TextHorizontalOverflow',
        'mso_drawing_type': 'MsoDrawingType',
        'text_orientation_type': 'TextOrientationType',
        'placement': 'Placement',
        'name': 'Name',
        'is_word_art': 'IsWordArt',
        'linked_cell': 'LinkedCell',
        'upper_left_row': 'UpperLeftRow',
        'is_locked': 'IsLocked',
        'lower_right_row': 'LowerRightRow',
        'is_text_wrapped': 'IsTextWrapped',
        'y': 'Y',
        'x': 'X',
        'is_hidden': 'IsHidden',
        'left': 'Left',
        'right': 'Right',
        'text': 'Text',
        'lower_right_column': 'LowerRightColumn',
        'height': 'Height',
        'text_horizontal_alignment': 'TextHorizontalAlignment',
        'text_vertical_overflow': 'TextVerticalOverflow'
    }
    
    @staticmethod
    def get_swagger_types():
        return Shape.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Shape.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, alternative_text=None, bottom=None, top=None, width=None, html_text=None, text_vertical_alignment=None, auto_shape_type=None, is_printable=None, upper_left_column=None, is_lock_aspect_ratio=None, is_group=None, rotation_angle=None, z_order_position=None, text_horizontal_overflow=None, mso_drawing_type=None, text_orientation_type=None, placement=None, name=None, is_word_art=None, linked_cell=None, upper_left_row=None, is_locked=None, lower_right_row=None, is_text_wrapped=None, y=None, x=None, is_hidden=None, left=None, right=None, text=None, lower_right_column=None, height=None, text_horizontal_alignment=None, text_vertical_overflow=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Shape - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['alternative_text'] = None
        self.container['bottom'] = None
        self.container['top'] = None
        self.container['width'] = None
        self.container['html_text'] = None
        self.container['text_vertical_alignment'] = None
        self.container['auto_shape_type'] = None
        self.container['is_printable'] = None
        self.container['upper_left_column'] = None
        self.container['is_lock_aspect_ratio'] = None
        self.container['is_group'] = None
        self.container['rotation_angle'] = None
        self.container['z_order_position'] = None
        self.container['text_horizontal_overflow'] = None
        self.container['mso_drawing_type'] = None
        self.container['text_orientation_type'] = None
        self.container['placement'] = None
        self.container['name'] = None
        self.container['is_word_art'] = None
        self.container['linked_cell'] = None
        self.container['upper_left_row'] = None
        self.container['is_locked'] = None
        self.container['lower_right_row'] = None
        self.container['is_text_wrapped'] = None
        self.container['y'] = None
        self.container['x'] = None
        self.container['is_hidden'] = None
        self.container['left'] = None
        self.container['right'] = None
        self.container['text'] = None
        self.container['lower_right_column'] = None
        self.container['height'] = None
        self.container['text_horizontal_alignment'] = None
        self.container['text_vertical_overflow'] = None

        if link is not None:
          self.link = link
        if alternative_text is not None:
          self.alternative_text = alternative_text
        if bottom is not None:
          self.bottom = bottom
        if top is not None:
          self.top = top
        if width is not None:
          self.width = width
        if html_text is not None:
          self.html_text = html_text
        if text_vertical_alignment is not None:
          self.text_vertical_alignment = text_vertical_alignment
        if auto_shape_type is not None:
          self.auto_shape_type = auto_shape_type
        if is_printable is not None:
          self.is_printable = is_printable
        if upper_left_column is not None:
          self.upper_left_column = upper_left_column
        if is_lock_aspect_ratio is not None:
          self.is_lock_aspect_ratio = is_lock_aspect_ratio
        if is_group is not None:
          self.is_group = is_group
        if rotation_angle is not None:
          self.rotation_angle = rotation_angle
        if z_order_position is not None:
          self.z_order_position = z_order_position
        if text_horizontal_overflow is not None:
          self.text_horizontal_overflow = text_horizontal_overflow
        if mso_drawing_type is not None:
          self.mso_drawing_type = mso_drawing_type
        if text_orientation_type is not None:
          self.text_orientation_type = text_orientation_type
        if placement is not None:
          self.placement = placement
        if name is not None:
          self.name = name
        if is_word_art is not None:
          self.is_word_art = is_word_art
        if linked_cell is not None:
          self.linked_cell = linked_cell
        if upper_left_row is not None:
          self.upper_left_row = upper_left_row
        if is_locked is not None:
          self.is_locked = is_locked
        if lower_right_row is not None:
          self.lower_right_row = lower_right_row
        if is_text_wrapped is not None:
          self.is_text_wrapped = is_text_wrapped
        if y is not None:
          self.y = y
        if x is not None:
          self.x = x
        if is_hidden is not None:
          self.is_hidden = is_hidden
        if left is not None:
          self.left = left
        if right is not None:
          self.right = right
        if text is not None:
          self.text = text
        if lower_right_column is not None:
          self.lower_right_column = lower_right_column
        if height is not None:
          self.height = height
        if text_horizontal_alignment is not None:
          self.text_horizontal_alignment = text_horizontal_alignment
        if text_vertical_overflow is not None:
          self.text_vertical_overflow = text_vertical_overflow

    @property
    def link(self):
        """
        Gets the link of this Shape.

        :return: The link of this Shape.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Shape.

        :param link: The link of this Shape.
        :type: Link
        """

        self.container['link'] = link

    @property
    def alternative_text(self):
        """
        Gets the alternative_text of this Shape.

        :return: The alternative_text of this Shape.
        :rtype: str
        """
        return self.container['alternative_text']

    @alternative_text.setter
    def alternative_text(self, alternative_text):
        """
        Sets the alternative_text of this Shape.

        :param alternative_text: The alternative_text of this Shape.
        :type: str
        """

        self.container['alternative_text'] = alternative_text

    @property
    def bottom(self):
        """
        Gets the bottom of this Shape.

        :return: The bottom of this Shape.
        :rtype: int
        """
        return self.container['bottom']

    @bottom.setter
    def bottom(self, bottom):
        """
        Sets the bottom of this Shape.

        :param bottom: The bottom of this Shape.
        :type: int
        """

        self.container['bottom'] = bottom

    @property
    def top(self):
        """
        Gets the top of this Shape.

        :return: The top of this Shape.
        :rtype: int
        """
        return self.container['top']

    @top.setter
    def top(self, top):
        """
        Sets the top of this Shape.

        :param top: The top of this Shape.
        :type: int
        """

        self.container['top'] = top

    @property
    def width(self):
        """
        Gets the width of this Shape.

        :return: The width of this Shape.
        :rtype: int
        """
        return self.container['width']

    @width.setter
    def width(self, width):
        """
        Sets the width of this Shape.

        :param width: The width of this Shape.
        :type: int
        """

        self.container['width'] = width

    @property
    def html_text(self):
        """
        Gets the html_text of this Shape.

        :return: The html_text of this Shape.
        :rtype: str
        """
        return self.container['html_text']

    @html_text.setter
    def html_text(self, html_text):
        """
        Sets the html_text of this Shape.

        :param html_text: The html_text of this Shape.
        :type: str
        """

        self.container['html_text'] = html_text

    @property
    def text_vertical_alignment(self):
        """
        Gets the text_vertical_alignment of this Shape.

        :return: The text_vertical_alignment of this Shape.
        :rtype: str
        """
        return self.container['text_vertical_alignment']

    @text_vertical_alignment.setter
    def text_vertical_alignment(self, text_vertical_alignment):
        """
        Sets the text_vertical_alignment of this Shape.

        :param text_vertical_alignment: The text_vertical_alignment of this Shape.
        :type: str
        """

        self.container['text_vertical_alignment'] = text_vertical_alignment

    @property
    def auto_shape_type(self):
        """
        Gets the auto_shape_type of this Shape.

        :return: The auto_shape_type of this Shape.
        :rtype: str
        """
        return self.container['auto_shape_type']

    @auto_shape_type.setter
    def auto_shape_type(self, auto_shape_type):
        """
        Sets the auto_shape_type of this Shape.

        :param auto_shape_type: The auto_shape_type of this Shape.
        :type: str
        """

        self.container['auto_shape_type'] = auto_shape_type

    @property
    def is_printable(self):
        """
        Gets the is_printable of this Shape.

        :return: The is_printable of this Shape.
        :rtype: bool
        """
        return self.container['is_printable']

    @is_printable.setter
    def is_printable(self, is_printable):
        """
        Sets the is_printable of this Shape.

        :param is_printable: The is_printable of this Shape.
        :type: bool
        """

        self.container['is_printable'] = is_printable

    @property
    def upper_left_column(self):
        """
        Gets the upper_left_column of this Shape.

        :return: The upper_left_column of this Shape.
        :rtype: int
        """
        return self.container['upper_left_column']

    @upper_left_column.setter
    def upper_left_column(self, upper_left_column):
        """
        Sets the upper_left_column of this Shape.

        :param upper_left_column: The upper_left_column of this Shape.
        :type: int
        """

        self.container['upper_left_column'] = upper_left_column

    @property
    def is_lock_aspect_ratio(self):
        """
        Gets the is_lock_aspect_ratio of this Shape.

        :return: The is_lock_aspect_ratio of this Shape.
        :rtype: bool
        """
        return self.container['is_lock_aspect_ratio']

    @is_lock_aspect_ratio.setter
    def is_lock_aspect_ratio(self, is_lock_aspect_ratio):
        """
        Sets the is_lock_aspect_ratio of this Shape.

        :param is_lock_aspect_ratio: The is_lock_aspect_ratio of this Shape.
        :type: bool
        """

        self.container['is_lock_aspect_ratio'] = is_lock_aspect_ratio

    @property
    def is_group(self):
        """
        Gets the is_group of this Shape.

        :return: The is_group of this Shape.
        :rtype: bool
        """
        return self.container['is_group']

    @is_group.setter
    def is_group(self, is_group):
        """
        Sets the is_group of this Shape.

        :param is_group: The is_group of this Shape.
        :type: bool
        """

        self.container['is_group'] = is_group

    @property
    def rotation_angle(self):
        """
        Gets the rotation_angle of this Shape.

        :return: The rotation_angle of this Shape.
        :rtype: float
        """
        return self.container['rotation_angle']

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle):
        """
        Sets the rotation_angle of this Shape.

        :param rotation_angle: The rotation_angle of this Shape.
        :type: float
        """

        self.container['rotation_angle'] = rotation_angle

    @property
    def z_order_position(self):
        """
        Gets the z_order_position of this Shape.

        :return: The z_order_position of this Shape.
        :rtype: int
        """
        return self.container['z_order_position']

    @z_order_position.setter
    def z_order_position(self, z_order_position):
        """
        Sets the z_order_position of this Shape.

        :param z_order_position: The z_order_position of this Shape.
        :type: int
        """

        self.container['z_order_position'] = z_order_position

    @property
    def text_horizontal_overflow(self):
        """
        Gets the text_horizontal_overflow of this Shape.

        :return: The text_horizontal_overflow of this Shape.
        :rtype: str
        """
        return self.container['text_horizontal_overflow']

    @text_horizontal_overflow.setter
    def text_horizontal_overflow(self, text_horizontal_overflow):
        """
        Sets the text_horizontal_overflow of this Shape.

        :param text_horizontal_overflow: The text_horizontal_overflow of this Shape.
        :type: str
        """

        self.container['text_horizontal_overflow'] = text_horizontal_overflow

    @property
    def mso_drawing_type(self):
        """
        Gets the mso_drawing_type of this Shape.

        :return: The mso_drawing_type of this Shape.
        :rtype: str
        """
        return self.container['mso_drawing_type']

    @mso_drawing_type.setter
    def mso_drawing_type(self, mso_drawing_type):
        """
        Sets the mso_drawing_type of this Shape.

        :param mso_drawing_type: The mso_drawing_type of this Shape.
        :type: str
        """

        self.container['mso_drawing_type'] = mso_drawing_type

    @property
    def text_orientation_type(self):
        """
        Gets the text_orientation_type of this Shape.

        :return: The text_orientation_type of this Shape.
        :rtype: str
        """
        return self.container['text_orientation_type']

    @text_orientation_type.setter
    def text_orientation_type(self, text_orientation_type):
        """
        Sets the text_orientation_type of this Shape.

        :param text_orientation_type: The text_orientation_type of this Shape.
        :type: str
        """

        self.container['text_orientation_type'] = text_orientation_type

    @property
    def placement(self):
        """
        Gets the placement of this Shape.

        :return: The placement of this Shape.
        :rtype: str
        """
        return self.container['placement']

    @placement.setter
    def placement(self, placement):
        """
        Sets the placement of this Shape.

        :param placement: The placement of this Shape.
        :type: str
        """

        self.container['placement'] = placement

    @property
    def name(self):
        """
        Gets the name of this Shape.

        :return: The name of this Shape.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this Shape.

        :param name: The name of this Shape.
        :type: str
        """

        self.container['name'] = name

    @property
    def is_word_art(self):
        """
        Gets the is_word_art of this Shape.

        :return: The is_word_art of this Shape.
        :rtype: bool
        """
        return self.container['is_word_art']

    @is_word_art.setter
    def is_word_art(self, is_word_art):
        """
        Sets the is_word_art of this Shape.

        :param is_word_art: The is_word_art of this Shape.
        :type: bool
        """

        self.container['is_word_art'] = is_word_art

    @property
    def linked_cell(self):
        """
        Gets the linked_cell of this Shape.

        :return: The linked_cell of this Shape.
        :rtype: str
        """
        return self.container['linked_cell']

    @linked_cell.setter
    def linked_cell(self, linked_cell):
        """
        Sets the linked_cell of this Shape.

        :param linked_cell: The linked_cell of this Shape.
        :type: str
        """

        self.container['linked_cell'] = linked_cell

    @property
    def upper_left_row(self):
        """
        Gets the upper_left_row of this Shape.

        :return: The upper_left_row of this Shape.
        :rtype: int
        """
        return self.container['upper_left_row']

    @upper_left_row.setter
    def upper_left_row(self, upper_left_row):
        """
        Sets the upper_left_row of this Shape.

        :param upper_left_row: The upper_left_row of this Shape.
        :type: int
        """

        self.container['upper_left_row'] = upper_left_row

    @property
    def is_locked(self):
        """
        Gets the is_locked of this Shape.

        :return: The is_locked of this Shape.
        :rtype: bool
        """
        return self.container['is_locked']

    @is_locked.setter
    def is_locked(self, is_locked):
        """
        Sets the is_locked of this Shape.

        :param is_locked: The is_locked of this Shape.
        :type: bool
        """

        self.container['is_locked'] = is_locked

    @property
    def lower_right_row(self):
        """
        Gets the lower_right_row of this Shape.

        :return: The lower_right_row of this Shape.
        :rtype: int
        """
        return self.container['lower_right_row']

    @lower_right_row.setter
    def lower_right_row(self, lower_right_row):
        """
        Sets the lower_right_row of this Shape.

        :param lower_right_row: The lower_right_row of this Shape.
        :type: int
        """

        self.container['lower_right_row'] = lower_right_row

    @property
    def is_text_wrapped(self):
        """
        Gets the is_text_wrapped of this Shape.

        :return: The is_text_wrapped of this Shape.
        :rtype: bool
        """
        return self.container['is_text_wrapped']

    @is_text_wrapped.setter
    def is_text_wrapped(self, is_text_wrapped):
        """
        Sets the is_text_wrapped of this Shape.

        :param is_text_wrapped: The is_text_wrapped of this Shape.
        :type: bool
        """

        self.container['is_text_wrapped'] = is_text_wrapped

    @property
    def y(self):
        """
        Gets the y of this Shape.

        :return: The y of this Shape.
        :rtype: int
        """
        return self.container['y']

    @y.setter
    def y(self, y):
        """
        Sets the y of this Shape.

        :param y: The y of this Shape.
        :type: int
        """

        self.container['y'] = y

    @property
    def x(self):
        """
        Gets the x of this Shape.

        :return: The x of this Shape.
        :rtype: int
        """
        return self.container['x']

    @x.setter
    def x(self, x):
        """
        Sets the x of this Shape.

        :param x: The x of this Shape.
        :type: int
        """

        self.container['x'] = x

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this Shape.

        :return: The is_hidden of this Shape.
        :rtype: bool
        """
        return self.container['is_hidden']

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this Shape.

        :param is_hidden: The is_hidden of this Shape.
        :type: bool
        """

        self.container['is_hidden'] = is_hidden

    @property
    def left(self):
        """
        Gets the left of this Shape.

        :return: The left of this Shape.
        :rtype: int
        """
        return self.container['left']

    @left.setter
    def left(self, left):
        """
        Sets the left of this Shape.

        :param left: The left of this Shape.
        :type: int
        """

        self.container['left'] = left

    @property
    def right(self):
        """
        Gets the right of this Shape.

        :return: The right of this Shape.
        :rtype: int
        """
        return self.container['right']

    @right.setter
    def right(self, right):
        """
        Sets the right of this Shape.

        :param right: The right of this Shape.
        :type: int
        """

        self.container['right'] = right

    @property
    def text(self):
        """
        Gets the text of this Shape.

        :return: The text of this Shape.
        :rtype: str
        """
        return self.container['text']

    @text.setter
    def text(self, text):
        """
        Sets the text of this Shape.

        :param text: The text of this Shape.
        :type: str
        """

        self.container['text'] = text

    @property
    def lower_right_column(self):
        """
        Gets the lower_right_column of this Shape.

        :return: The lower_right_column of this Shape.
        :rtype: int
        """
        return self.container['lower_right_column']

    @lower_right_column.setter
    def lower_right_column(self, lower_right_column):
        """
        Sets the lower_right_column of this Shape.

        :param lower_right_column: The lower_right_column of this Shape.
        :type: int
        """

        self.container['lower_right_column'] = lower_right_column

    @property
    def height(self):
        """
        Gets the height of this Shape.

        :return: The height of this Shape.
        :rtype: int
        """
        return self.container['height']

    @height.setter
    def height(self, height):
        """
        Sets the height of this Shape.

        :param height: The height of this Shape.
        :type: int
        """

        self.container['height'] = height

    @property
    def text_horizontal_alignment(self):
        """
        Gets the text_horizontal_alignment of this Shape.

        :return: The text_horizontal_alignment of this Shape.
        :rtype: str
        """
        return self.container['text_horizontal_alignment']

    @text_horizontal_alignment.setter
    def text_horizontal_alignment(self, text_horizontal_alignment):
        """
        Sets the text_horizontal_alignment of this Shape.

        :param text_horizontal_alignment: The text_horizontal_alignment of this Shape.
        :type: str
        """

        self.container['text_horizontal_alignment'] = text_horizontal_alignment

    @property
    def text_vertical_overflow(self):
        """
        Gets the text_vertical_overflow of this Shape.

        :return: The text_vertical_overflow of this Shape.
        :rtype: str
        """
        return self.container['text_vertical_overflow']

    @text_vertical_overflow.setter
    def text_vertical_overflow(self, text_vertical_overflow):
        """
        Sets the text_vertical_overflow of this Shape.

        :param text_vertical_overflow: The text_vertical_overflow of this Shape.
        :type: str
        """

        self.container['text_vertical_overflow'] = text_vertical_overflow

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
        if not isinstance(other, Shape):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
