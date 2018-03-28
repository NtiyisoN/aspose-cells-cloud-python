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


class Column(object):
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
        'group_level': 'int',
        'index': 'int',
        'is_hidden': 'bool',
        'width': 'float',
        'style': 'LinkElement'
    }

    attribute_map = {
        'link': 'link',
        'group_level': 'GroupLevel',
        'index': 'Index',
        'is_hidden': 'IsHidden',
        'width': 'Width',
        'style': 'Style'
    }
    
    @staticmethod
    def get_swagger_types():
        return Column.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Column.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, group_level=None, index=None, is_hidden=None, width=None, style=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Column - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['group_level'] = None
        self.container['index'] = None
        self.container['is_hidden'] = None
        self.container['width'] = None
        self.container['style'] = None

        if link is not None:
          self.link = link
        if group_level is not None:
          self.group_level = group_level
        if index is not None:
          self.index = index
        if is_hidden is not None:
          self.is_hidden = is_hidden
        if width is not None:
          self.width = width
        if style is not None:
          self.style = style

    @property
    def link(self):
        """
        Gets the link of this Column.

        :return: The link of this Column.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Column.

        :param link: The link of this Column.
        :type: Link
        """

        self.container['link'] = link

    @property
    def group_level(self):
        """
        Gets the group_level of this Column.

        :return: The group_level of this Column.
        :rtype: int
        """
        return self.container['group_level']

    @group_level.setter
    def group_level(self, group_level):
        """
        Sets the group_level of this Column.

        :param group_level: The group_level of this Column.
        :type: int
        """

        self.container['group_level'] = group_level

    @property
    def index(self):
        """
        Gets the index of this Column.

        :return: The index of this Column.
        :rtype: int
        """
        return self.container['index']

    @index.setter
    def index(self, index):
        """
        Sets the index of this Column.

        :param index: The index of this Column.
        :type: int
        """

        self.container['index'] = index

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this Column.

        :return: The is_hidden of this Column.
        :rtype: bool
        """
        return self.container['is_hidden']

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this Column.

        :param is_hidden: The is_hidden of this Column.
        :type: bool
        """

        self.container['is_hidden'] = is_hidden

    @property
    def width(self):
        """
        Gets the width of this Column.

        :return: The width of this Column.
        :rtype: float
        """
        return self.container['width']

    @width.setter
    def width(self, width):
        """
        Sets the width of this Column.

        :param width: The width of this Column.
        :type: float
        """

        self.container['width'] = width

    @property
    def style(self):
        """
        Gets the style of this Column.

        :return: The style of this Column.
        :rtype: LinkElement
        """
        return self.container['style']

    @style.setter
    def style(self, style):
        """
        Sets the style of this Column.

        :param style: The style of this Column.
        :type: LinkElement
        """

        self.container['style'] = style

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
        if not isinstance(other, Column):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
