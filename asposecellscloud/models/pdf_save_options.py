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

class PdfSaveOptions(SaveOptions):
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
        'calculate_formula': 'bool',
        'check_font_compatibility': 'bool',
        'one_page_per_sheet': 'bool',
        'compliance': 'str',
        'default_font': 'str',
        'printing_page_type': 'str',
        'image_type': 'str',
        'desired_ppi': 'int',
        'jpeg_quality': 'int',
        'security_options': 'PdfSecurityOptions'
    }

    attribute_map = {
        'calculate_formula': 'CalculateFormula',
        'check_font_compatibility': 'CheckFontCompatibility',
        'one_page_per_sheet': 'OnePagePerSheet',
        'compliance': 'Compliance',
        'default_font': 'DefaultFont',
        'printing_page_type': 'PrintingPageType',
        'image_type': 'ImageType',
        'desired_ppi': 'desiredPPI',
        'jpeg_quality': 'jpegQuality',
        'security_options': 'SecurityOptions'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(PdfSaveOptions.swagger_types, **SaveOptions.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(PdfSaveOptions.attribute_map, **SaveOptions.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, calculate_formula=None, check_font_compatibility=None, one_page_per_sheet=None, compliance=None, default_font=None, printing_page_type=None, image_type=None, desired_ppi=None, jpeg_quality=None, security_options=None, **kw):
        super(PdfSaveOptions, self).__init__(**kw)
		    
        """
        PdfSaveOptions - a model defined in Swagger
        """

        self.container['calculate_formula'] = None
        self.container['check_font_compatibility'] = None
        self.container['one_page_per_sheet'] = None
        self.container['compliance'] = None
        self.container['default_font'] = None
        self.container['printing_page_type'] = None
        self.container['image_type'] = None
        self.container['desired_ppi'] = None
        self.container['jpeg_quality'] = None
        self.container['security_options'] = None

        if calculate_formula is not None:
          self.calculate_formula = calculate_formula
        if check_font_compatibility is not None:
          self.check_font_compatibility = check_font_compatibility
        if one_page_per_sheet is not None:
          self.one_page_per_sheet = one_page_per_sheet
        if compliance is not None:
          self.compliance = compliance
        if default_font is not None:
          self.default_font = default_font
        if printing_page_type is not None:
          self.printing_page_type = printing_page_type
        if image_type is not None:
          self.image_type = image_type
        if desired_ppi is not None:
          self.desired_ppi = desired_ppi
        if jpeg_quality is not None:
          self.jpeg_quality = jpeg_quality
        if security_options is not None:
          self.security_options = security_options

    @property
    def calculate_formula(self):
        """
        Gets the calculate_formula of this PdfSaveOptions.

        :return: The calculate_formula of this PdfSaveOptions.
        :rtype: bool
        """
        return self.container['calculate_formula']

    @calculate_formula.setter
    def calculate_formula(self, calculate_formula):
        """
        Sets the calculate_formula of this PdfSaveOptions.

        :param calculate_formula: The calculate_formula of this PdfSaveOptions.
        :type: bool
        """

        self.container['calculate_formula'] = calculate_formula

    @property
    def check_font_compatibility(self):
        """
        Gets the check_font_compatibility of this PdfSaveOptions.

        :return: The check_font_compatibility of this PdfSaveOptions.
        :rtype: bool
        """
        return self.container['check_font_compatibility']

    @check_font_compatibility.setter
    def check_font_compatibility(self, check_font_compatibility):
        """
        Sets the check_font_compatibility of this PdfSaveOptions.

        :param check_font_compatibility: The check_font_compatibility of this PdfSaveOptions.
        :type: bool
        """

        self.container['check_font_compatibility'] = check_font_compatibility

    @property
    def one_page_per_sheet(self):
        """
        Gets the one_page_per_sheet of this PdfSaveOptions.

        :return: The one_page_per_sheet of this PdfSaveOptions.
        :rtype: bool
        """
        return self.container['one_page_per_sheet']

    @one_page_per_sheet.setter
    def one_page_per_sheet(self, one_page_per_sheet):
        """
        Sets the one_page_per_sheet of this PdfSaveOptions.

        :param one_page_per_sheet: The one_page_per_sheet of this PdfSaveOptions.
        :type: bool
        """

        self.container['one_page_per_sheet'] = one_page_per_sheet

    @property
    def compliance(self):
        """
        Gets the compliance of this PdfSaveOptions.

        :return: The compliance of this PdfSaveOptions.
        :rtype: str
        """
        return self.container['compliance']

    @compliance.setter
    def compliance(self, compliance):
        """
        Sets the compliance of this PdfSaveOptions.

        :param compliance: The compliance of this PdfSaveOptions.
        :type: str
        """

        self.container['compliance'] = compliance

    @property
    def default_font(self):
        """
        Gets the default_font of this PdfSaveOptions.

        :return: The default_font of this PdfSaveOptions.
        :rtype: str
        """
        return self.container['default_font']

    @default_font.setter
    def default_font(self, default_font):
        """
        Sets the default_font of this PdfSaveOptions.

        :param default_font: The default_font of this PdfSaveOptions.
        :type: str
        """

        self.container['default_font'] = default_font

    @property
    def printing_page_type(self):
        """
        Gets the printing_page_type of this PdfSaveOptions.

        :return: The printing_page_type of this PdfSaveOptions.
        :rtype: str
        """
        return self.container['printing_page_type']

    @printing_page_type.setter
    def printing_page_type(self, printing_page_type):
        """
        Sets the printing_page_type of this PdfSaveOptions.

        :param printing_page_type: The printing_page_type of this PdfSaveOptions.
        :type: str
        """

        self.container['printing_page_type'] = printing_page_type

    @property
    def image_type(self):
        """
        Gets the image_type of this PdfSaveOptions.

        :return: The image_type of this PdfSaveOptions.
        :rtype: str
        """
        return self.container['image_type']

    @image_type.setter
    def image_type(self, image_type):
        """
        Sets the image_type of this PdfSaveOptions.

        :param image_type: The image_type of this PdfSaveOptions.
        :type: str
        """

        self.container['image_type'] = image_type

    @property
    def desired_ppi(self):
        """
        Gets the desired_ppi of this PdfSaveOptions.

        :return: The desired_ppi of this PdfSaveOptions.
        :rtype: int
        """
        return self.container['desired_ppi']

    @desired_ppi.setter
    def desired_ppi(self, desired_ppi):
        """
        Sets the desired_ppi of this PdfSaveOptions.

        :param desired_ppi: The desired_ppi of this PdfSaveOptions.
        :type: int
        """

        self.container['desired_ppi'] = desired_ppi

    @property
    def jpeg_quality(self):
        """
        Gets the jpeg_quality of this PdfSaveOptions.

        :return: The jpeg_quality of this PdfSaveOptions.
        :rtype: int
        """
        return self.container['jpeg_quality']

    @jpeg_quality.setter
    def jpeg_quality(self, jpeg_quality):
        """
        Sets the jpeg_quality of this PdfSaveOptions.

        :param jpeg_quality: The jpeg_quality of this PdfSaveOptions.
        :type: int
        """

        self.container['jpeg_quality'] = jpeg_quality

    @property
    def security_options(self):
        """
        Gets the security_options of this PdfSaveOptions.

        :return: The security_options of this PdfSaveOptions.
        :rtype: PdfSecurityOptions
        """
        return self.container['security_options']

    @security_options.setter
    def security_options(self, security_options):
        """
        Sets the security_options of this PdfSaveOptions.

        :param security_options: The security_options of this PdfSaveOptions.
        :type: PdfSecurityOptions
        """

        self.container['security_options'] = security_options

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
        if not isinstance(other, PdfSaveOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
