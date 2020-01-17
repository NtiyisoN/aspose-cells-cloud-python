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


class AutoFitterOptions(object):
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
        'ignore_hidden': 'bool',
        'only_auto': 'bool',
        'auto_fit_merged_cells': 'bool'
    }

    attribute_map = {
        'ignore_hidden': 'IgnoreHidden',
        'only_auto': 'OnlyAuto',
        'auto_fit_merged_cells': 'AutoFitMergedCells'
    }
    
    @staticmethod
    def get_swagger_types():
        return AutoFitterOptions.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return AutoFitterOptions.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, ignore_hidden=None, only_auto=None, auto_fit_merged_cells=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        AutoFitterOptions - a model defined in Swagger
        """

        self.container['ignore_hidden'] = None
        self.container['only_auto'] = None
        self.container['auto_fit_merged_cells'] = None

        self.ignore_hidden = ignore_hidden
        self.only_auto = only_auto
        self.auto_fit_merged_cells = auto_fit_merged_cells

    @property
    def ignore_hidden(self):
        """
        Gets the ignore_hidden of this AutoFitterOptions.

        :return: The ignore_hidden of this AutoFitterOptions.
        :rtype: bool
        """
        return self.container['ignore_hidden']

    @ignore_hidden.setter
    def ignore_hidden(self, ignore_hidden):
        """
        Sets the ignore_hidden of this AutoFitterOptions.

        :param ignore_hidden: The ignore_hidden of this AutoFitterOptions.
        :type: bool
        """
        """
        if ignore_hidden is None:
            raise ValueError("Invalid value for `ignore_hidden`, must not be `None`")
        """

        self.container['ignore_hidden'] = ignore_hidden

    @property
    def only_auto(self):
        """
        Gets the only_auto of this AutoFitterOptions.

        :return: The only_auto of this AutoFitterOptions.
        :rtype: bool
        """
        return self.container['only_auto']

    @only_auto.setter
    def only_auto(self, only_auto):
        """
        Sets the only_auto of this AutoFitterOptions.

        :param only_auto: The only_auto of this AutoFitterOptions.
        :type: bool
        """
        """
        if only_auto is None:
            raise ValueError("Invalid value for `only_auto`, must not be `None`")
        """

        self.container['only_auto'] = only_auto

    @property
    def auto_fit_merged_cells(self):
        """
        Gets the auto_fit_merged_cells of this AutoFitterOptions.

        :return: The auto_fit_merged_cells of this AutoFitterOptions.
        :rtype: bool
        """
        return self.container['auto_fit_merged_cells']

    @auto_fit_merged_cells.setter
    def auto_fit_merged_cells(self, auto_fit_merged_cells):
        """
        Sets the auto_fit_merged_cells of this AutoFitterOptions.

        :param auto_fit_merged_cells: The auto_fit_merged_cells of this AutoFitterOptions.
        :type: bool
        """
        """
        if auto_fit_merged_cells is None:
            raise ValueError("Invalid value for `auto_fit_merged_cells`, must not be `None`")
        """

        self.container['auto_fit_merged_cells'] = auto_fit_merged_cells

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
        if not isinstance(other, AutoFitterOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
