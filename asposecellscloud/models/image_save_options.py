# coding: utf-8

"""
Copyright (c) 2019 Aspose.Cells Cloud
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
from . import SaveOptions

class ImageSaveOptions(SaveOptions):
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
        'chart_image_type': 'str',
        'embeded_image_name_in_svg': 'str',
        'horizontal_resolution': 'int',
        'image_format': 'str',
        'is_cell_auto_fit': 'bool',
        'one_page_per_sheet': 'bool',
        'only_area': 'bool',
        'printing_page': 'str',
        'print_with_status_dialog': 'int',
        'quality': 'int',
        'tiff_compression': 'str',
        'vertical_resolution': 'int'
    }

    attribute_map = {
        'chart_image_type': 'ChartImageType',
        'embeded_image_name_in_svg': 'EmbededImageNameInSvg',
        'horizontal_resolution': 'HorizontalResolution',
        'image_format': 'ImageFormat',
        'is_cell_auto_fit': 'IsCellAutoFit',
        'one_page_per_sheet': 'OnePagePerSheet',
        'only_area': 'OnlyArea',
        'printing_page': 'PrintingPage',
        'print_with_status_dialog': 'PrintWithStatusDialog',
        'quality': 'Quality',
        'tiff_compression': 'TiffCompression',
        'vertical_resolution': 'VerticalResolution'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(ImageSaveOptions.swagger_types, **SaveOptions.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(ImageSaveOptions.attribute_map, **SaveOptions.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, chart_image_type=None, embeded_image_name_in_svg=None, horizontal_resolution=None, image_format=None, is_cell_auto_fit=None, one_page_per_sheet=None, only_area=None, printing_page=None, print_with_status_dialog=None, quality=None, tiff_compression=None, vertical_resolution=None, **kw):
        super(ImageSaveOptions, self).__init__(**kw)
		    
        """
        ImageSaveOptions - a model defined in Swagger
        """

        self.container['chart_image_type'] = None
        self.container['embeded_image_name_in_svg'] = None
        self.container['horizontal_resolution'] = None
        self.container['image_format'] = None
        self.container['is_cell_auto_fit'] = None
        self.container['one_page_per_sheet'] = None
        self.container['only_area'] = None
        self.container['printing_page'] = None
        self.container['print_with_status_dialog'] = None
        self.container['quality'] = None
        self.container['tiff_compression'] = None
        self.container['vertical_resolution'] = None

        if chart_image_type is not None:
          self.chart_image_type = chart_image_type
        if embeded_image_name_in_svg is not None:
          self.embeded_image_name_in_svg = embeded_image_name_in_svg
        if horizontal_resolution is not None:
          self.horizontal_resolution = horizontal_resolution
        if image_format is not None:
          self.image_format = image_format
        if is_cell_auto_fit is not None:
          self.is_cell_auto_fit = is_cell_auto_fit
        if one_page_per_sheet is not None:
          self.one_page_per_sheet = one_page_per_sheet
        if only_area is not None:
          self.only_area = only_area
        if printing_page is not None:
          self.printing_page = printing_page
        if print_with_status_dialog is not None:
          self.print_with_status_dialog = print_with_status_dialog
        if quality is not None:
          self.quality = quality
        if tiff_compression is not None:
          self.tiff_compression = tiff_compression
        if vertical_resolution is not None:
          self.vertical_resolution = vertical_resolution

    @property
    def chart_image_type(self):
        """
        Gets the chart_image_type of this ImageSaveOptions.

        :return: The chart_image_type of this ImageSaveOptions.
        :rtype: str
        """
        return self.container['chart_image_type']

    @chart_image_type.setter
    def chart_image_type(self, chart_image_type):
        """
        Sets the chart_image_type of this ImageSaveOptions.

        :param chart_image_type: The chart_image_type of this ImageSaveOptions.
        :type: str
        """

        self.container['chart_image_type'] = chart_image_type

    @property
    def embeded_image_name_in_svg(self):
        """
        Gets the embeded_image_name_in_svg of this ImageSaveOptions.

        :return: The embeded_image_name_in_svg of this ImageSaveOptions.
        :rtype: str
        """
        return self.container['embeded_image_name_in_svg']

    @embeded_image_name_in_svg.setter
    def embeded_image_name_in_svg(self, embeded_image_name_in_svg):
        """
        Sets the embeded_image_name_in_svg of this ImageSaveOptions.

        :param embeded_image_name_in_svg: The embeded_image_name_in_svg of this ImageSaveOptions.
        :type: str
        """

        self.container['embeded_image_name_in_svg'] = embeded_image_name_in_svg

    @property
    def horizontal_resolution(self):
        """
        Gets the horizontal_resolution of this ImageSaveOptions.

        :return: The horizontal_resolution of this ImageSaveOptions.
        :rtype: int
        """
        return self.container['horizontal_resolution']

    @horizontal_resolution.setter
    def horizontal_resolution(self, horizontal_resolution):
        """
        Sets the horizontal_resolution of this ImageSaveOptions.

        :param horizontal_resolution: The horizontal_resolution of this ImageSaveOptions.
        :type: int
        """

        self.container['horizontal_resolution'] = horizontal_resolution

    @property
    def image_format(self):
        """
        Gets the image_format of this ImageSaveOptions.

        :return: The image_format of this ImageSaveOptions.
        :rtype: str
        """
        return self.container['image_format']

    @image_format.setter
    def image_format(self, image_format):
        """
        Sets the image_format of this ImageSaveOptions.

        :param image_format: The image_format of this ImageSaveOptions.
        :type: str
        """

        self.container['image_format'] = image_format

    @property
    def is_cell_auto_fit(self):
        """
        Gets the is_cell_auto_fit of this ImageSaveOptions.

        :return: The is_cell_auto_fit of this ImageSaveOptions.
        :rtype: bool
        """
        return self.container['is_cell_auto_fit']

    @is_cell_auto_fit.setter
    def is_cell_auto_fit(self, is_cell_auto_fit):
        """
        Sets the is_cell_auto_fit of this ImageSaveOptions.

        :param is_cell_auto_fit: The is_cell_auto_fit of this ImageSaveOptions.
        :type: bool
        """

        self.container['is_cell_auto_fit'] = is_cell_auto_fit

    @property
    def one_page_per_sheet(self):
        """
        Gets the one_page_per_sheet of this ImageSaveOptions.

        :return: The one_page_per_sheet of this ImageSaveOptions.
        :rtype: bool
        """
        return self.container['one_page_per_sheet']

    @one_page_per_sheet.setter
    def one_page_per_sheet(self, one_page_per_sheet):
        """
        Sets the one_page_per_sheet of this ImageSaveOptions.

        :param one_page_per_sheet: The one_page_per_sheet of this ImageSaveOptions.
        :type: bool
        """

        self.container['one_page_per_sheet'] = one_page_per_sheet

    @property
    def only_area(self):
        """
        Gets the only_area of this ImageSaveOptions.

        :return: The only_area of this ImageSaveOptions.
        :rtype: bool
        """
        return self.container['only_area']

    @only_area.setter
    def only_area(self, only_area):
        """
        Sets the only_area of this ImageSaveOptions.

        :param only_area: The only_area of this ImageSaveOptions.
        :type: bool
        """

        self.container['only_area'] = only_area

    @property
    def printing_page(self):
        """
        Gets the printing_page of this ImageSaveOptions.

        :return: The printing_page of this ImageSaveOptions.
        :rtype: str
        """
        return self.container['printing_page']

    @printing_page.setter
    def printing_page(self, printing_page):
        """
        Sets the printing_page of this ImageSaveOptions.

        :param printing_page: The printing_page of this ImageSaveOptions.
        :type: str
        """

        self.container['printing_page'] = printing_page

    @property
    def print_with_status_dialog(self):
        """
        Gets the print_with_status_dialog of this ImageSaveOptions.

        :return: The print_with_status_dialog of this ImageSaveOptions.
        :rtype: int
        """
        return self.container['print_with_status_dialog']

    @print_with_status_dialog.setter
    def print_with_status_dialog(self, print_with_status_dialog):
        """
        Sets the print_with_status_dialog of this ImageSaveOptions.

        :param print_with_status_dialog: The print_with_status_dialog of this ImageSaveOptions.
        :type: int
        """

        self.container['print_with_status_dialog'] = print_with_status_dialog

    @property
    def quality(self):
        """
        Gets the quality of this ImageSaveOptions.

        :return: The quality of this ImageSaveOptions.
        :rtype: int
        """
        return self.container['quality']

    @quality.setter
    def quality(self, quality):
        """
        Sets the quality of this ImageSaveOptions.

        :param quality: The quality of this ImageSaveOptions.
        :type: int
        """

        self.container['quality'] = quality

    @property
    def tiff_compression(self):
        """
        Gets the tiff_compression of this ImageSaveOptions.

        :return: The tiff_compression of this ImageSaveOptions.
        :rtype: str
        """
        return self.container['tiff_compression']

    @tiff_compression.setter
    def tiff_compression(self, tiff_compression):
        """
        Sets the tiff_compression of this ImageSaveOptions.

        :param tiff_compression: The tiff_compression of this ImageSaveOptions.
        :type: str
        """

        self.container['tiff_compression'] = tiff_compression

    @property
    def vertical_resolution(self):
        """
        Gets the vertical_resolution of this ImageSaveOptions.

        :return: The vertical_resolution of this ImageSaveOptions.
        :rtype: int
        """
        return self.container['vertical_resolution']

    @vertical_resolution.setter
    def vertical_resolution(self, vertical_resolution):
        """
        Sets the vertical_resolution of this ImageSaveOptions.

        :param vertical_resolution: The vertical_resolution of this ImageSaveOptions.
        :type: int
        """

        self.container['vertical_resolution'] = vertical_resolution

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
        if not isinstance(other, ImageSaveOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
