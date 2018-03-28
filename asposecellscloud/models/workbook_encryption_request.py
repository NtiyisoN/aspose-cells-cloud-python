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


class WorkbookEncryptionRequest(object):
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
        'encryption_type': 'str',
        'key_length': 'int',
        'password': 'str'
    }

    attribute_map = {
        'encryption_type': 'EncryptionType',
        'key_length': 'KeyLength',
        'password': 'Password'
    }
    
    @staticmethod
    def get_swagger_types():
        return WorkbookEncryptionRequest.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return WorkbookEncryptionRequest.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, encryption_type=None, key_length=None, password=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        WorkbookEncryptionRequest - a model defined in Swagger
        """

        self.container['encryption_type'] = None
        self.container['key_length'] = None
        self.container['password'] = None

        if encryption_type is not None:
          self.encryption_type = encryption_type
        self.key_length = key_length
        if password is not None:
          self.password = password

    @property
    def encryption_type(self):
        """
        Gets the encryption_type of this WorkbookEncryptionRequest.
        Workbook encription type.

        :return: The encryption_type of this WorkbookEncryptionRequest.
        :rtype: str
        """
        return self.container['encryption_type']

    @encryption_type.setter
    def encryption_type(self, encryption_type):
        """
        Sets the encryption_type of this WorkbookEncryptionRequest.
        Workbook encription type.

        :param encryption_type: The encryption_type of this WorkbookEncryptionRequest.
        :type: str
        """

        self.container['encryption_type'] = encryption_type

    @property
    def key_length(self):
        """
        Gets the key_length of this WorkbookEncryptionRequest.
        Encription key length.

        :return: The key_length of this WorkbookEncryptionRequest.
        :rtype: int
        """
        return self.container['key_length']

    @key_length.setter
    def key_length(self, key_length):
        """
        Sets the key_length of this WorkbookEncryptionRequest.
        Encription key length.

        :param key_length: The key_length of this WorkbookEncryptionRequest.
        :type: int
        """
        if key_length is None:
            raise ValueError("Invalid value for `key_length`, must not be `None`")

        self.container['key_length'] = key_length

    @property
    def password(self):
        """
        Gets the password of this WorkbookEncryptionRequest.
        Encription password.

        :return: The password of this WorkbookEncryptionRequest.
        :rtype: str
        """
        return self.container['password']

    @password.setter
    def password(self, password):
        """
        Sets the password of this WorkbookEncryptionRequest.
        Encription password.

        :param password: The password of this WorkbookEncryptionRequest.
        :type: str
        """

        self.container['password'] = password

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
        if not isinstance(other, WorkbookEncryptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
