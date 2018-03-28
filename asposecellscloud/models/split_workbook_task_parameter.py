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
from . import TaskParameter

class SplitWorkbookTaskParameter(TaskParameter):
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
        'workbook': 'FileSource',
        'destination_file_position': 'FileSource',
        'destination_file_format': 'str',
        'split_name_rule': 'str',
        'vertical_resolution': 'int',
        'horizontal_resolution': 'int'
    }

    attribute_map = {
        'workbook': 'Workbook',
        'destination_file_position': 'DestinationFilePosition',
        'destination_file_format': 'DestinationFileFormat',
        'split_name_rule': 'SplitNameRule',
        'vertical_resolution': 'VerticalResolution',
        'horizontal_resolution': 'HorizontalResolution'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(SplitWorkbookTaskParameter.swagger_types, **TaskParameter.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(SplitWorkbookTaskParameter.attribute_map, **TaskParameter.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, workbook=None, destination_file_position=None, destination_file_format=None, split_name_rule=None, vertical_resolution=None, horizontal_resolution=None, **kw):
        super(SplitWorkbookTaskParameter, self).__init__(**kw)
		    
        """
        SplitWorkbookTaskParameter - a model defined in Swagger
        """

        self.container['workbook'] = None
        self.container['destination_file_position'] = None
        self.container['destination_file_format'] = None
        self.container['split_name_rule'] = None
        self.container['vertical_resolution'] = None
        self.container['horizontal_resolution'] = None

        if workbook is not None:
          self.workbook = workbook
        if destination_file_position is not None:
          self.destination_file_position = destination_file_position
        if destination_file_format is not None:
          self.destination_file_format = destination_file_format
        if split_name_rule is not None:
          self.split_name_rule = split_name_rule
        if vertical_resolution is not None:
          self.vertical_resolution = vertical_resolution
        if horizontal_resolution is not None:
          self.horizontal_resolution = horizontal_resolution

    @property
    def workbook(self):
        """
        Gets the workbook of this SplitWorkbookTaskParameter.

        :return: The workbook of this SplitWorkbookTaskParameter.
        :rtype: FileSource
        """
        return self.container['workbook']

    @workbook.setter
    def workbook(self, workbook):
        """
        Sets the workbook of this SplitWorkbookTaskParameter.

        :param workbook: The workbook of this SplitWorkbookTaskParameter.
        :type: FileSource
        """

        self.container['workbook'] = workbook

    @property
    def destination_file_position(self):
        """
        Gets the destination_file_position of this SplitWorkbookTaskParameter.

        :return: The destination_file_position of this SplitWorkbookTaskParameter.
        :rtype: FileSource
        """
        return self.container['destination_file_position']

    @destination_file_position.setter
    def destination_file_position(self, destination_file_position):
        """
        Sets the destination_file_position of this SplitWorkbookTaskParameter.

        :param destination_file_position: The destination_file_position of this SplitWorkbookTaskParameter.
        :type: FileSource
        """

        self.container['destination_file_position'] = destination_file_position

    @property
    def destination_file_format(self):
        """
        Gets the destination_file_format of this SplitWorkbookTaskParameter.

        :return: The destination_file_format of this SplitWorkbookTaskParameter.
        :rtype: str
        """
        return self.container['destination_file_format']

    @destination_file_format.setter
    def destination_file_format(self, destination_file_format):
        """
        Sets the destination_file_format of this SplitWorkbookTaskParameter.

        :param destination_file_format: The destination_file_format of this SplitWorkbookTaskParameter.
        :type: str
        """

        self.container['destination_file_format'] = destination_file_format

    @property
    def split_name_rule(self):
        """
        Gets the split_name_rule of this SplitWorkbookTaskParameter.

        :return: The split_name_rule of this SplitWorkbookTaskParameter.
        :rtype: str
        """
        return self.container['split_name_rule']

    @split_name_rule.setter
    def split_name_rule(self, split_name_rule):
        """
        Sets the split_name_rule of this SplitWorkbookTaskParameter.

        :param split_name_rule: The split_name_rule of this SplitWorkbookTaskParameter.
        :type: str
        """

        self.container['split_name_rule'] = split_name_rule

    @property
    def vertical_resolution(self):
        """
        Gets the vertical_resolution of this SplitWorkbookTaskParameter.

        :return: The vertical_resolution of this SplitWorkbookTaskParameter.
        :rtype: int
        """
        return self.container['vertical_resolution']

    @vertical_resolution.setter
    def vertical_resolution(self, vertical_resolution):
        """
        Sets the vertical_resolution of this SplitWorkbookTaskParameter.

        :param vertical_resolution: The vertical_resolution of this SplitWorkbookTaskParameter.
        :type: int
        """

        self.container['vertical_resolution'] = vertical_resolution

    @property
    def horizontal_resolution(self):
        """
        Gets the horizontal_resolution of this SplitWorkbookTaskParameter.

        :return: The horizontal_resolution of this SplitWorkbookTaskParameter.
        :rtype: int
        """
        return self.container['horizontal_resolution']

    @horizontal_resolution.setter
    def horizontal_resolution(self, horizontal_resolution):
        """
        Sets the horizontal_resolution of this SplitWorkbookTaskParameter.

        :param horizontal_resolution: The horizontal_resolution of this SplitWorkbookTaskParameter.
        :type: int
        """

        self.container['horizontal_resolution'] = horizontal_resolution

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
        if not isinstance(other, SplitWorkbookTaskParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
