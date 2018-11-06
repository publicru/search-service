# coding: utf-8

"""
    Public Search API

    Searches documens and editions  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: you@your-company.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EditionItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'int',
        'name': 'str',
        'prev_name': 'str',
        'alias': 'str',
        'url': 'str',
        'geo_id': 'int',
        'geo_name': 'str',
        'score': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'prev_name': 'prev_name',
        'alias': 'alias',
        'url': 'url',
        'geo_id': 'geo_id',
        'geo_name': 'geo_name',
        'score': 'score'
    }

    def __init__(self, id=None, name=None, prev_name=None, alias=None, url=None, geo_id=None, geo_name=None, score=None):  # noqa: E501
        """EditionItem - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._prev_name = None
        self._alias = None
        self._url = None
        self._geo_id = None
        self._geo_name = None
        self._score = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if prev_name is not None:
            self.prev_name = prev_name
        if alias is not None:
            self.alias = alias
        if url is not None:
            self.url = url
        if geo_id is not None:
            self.geo_id = geo_id
        if geo_name is not None:
            self.geo_name = geo_name
        self.score = score

    @property
    def id(self):
        """Gets the id of this EditionItem.  # noqa: E501


        :return: The id of this EditionItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EditionItem.


        :param id: The id of this EditionItem.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this EditionItem.  # noqa: E501

        edition name  # noqa: E501

        :return: The name of this EditionItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EditionItem.

        edition name  # noqa: E501

        :param name: The name of this EditionItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def prev_name(self):
        """Gets the prev_name of this EditionItem.  # noqa: E501

        previous edition name (could be null)  # noqa: E501

        :return: The prev_name of this EditionItem.  # noqa: E501
        :rtype: str
        """
        return self._prev_name

    @prev_name.setter
    def prev_name(self, prev_name):
        """Sets the prev_name of this EditionItem.

        previous edition name (could be null)  # noqa: E501

        :param prev_name: The prev_name of this EditionItem.  # noqa: E501
        :type: str
        """

        self._prev_name = prev_name

    @property
    def alias(self):
        """Gets the alias of this EditionItem.  # noqa: E501

        edition alias  # noqa: E501

        :return: The alias of this EditionItem.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this EditionItem.

        edition alias  # noqa: E501

        :param alias: The alias of this EditionItem.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def url(self):
        """Gets the url of this EditionItem.  # noqa: E501

        edition url (could be null)  # noqa: E501

        :return: The url of this EditionItem.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this EditionItem.

        edition url (could be null)  # noqa: E501

        :param url: The url of this EditionItem.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def geo_id(self):
        """Gets the geo_id of this EditionItem.  # noqa: E501


        :return: The geo_id of this EditionItem.  # noqa: E501
        :rtype: int
        """
        return self._geo_id

    @geo_id.setter
    def geo_id(self, geo_id):
        """Sets the geo_id of this EditionItem.


        :param geo_id: The geo_id of this EditionItem.  # noqa: E501
        :type: int
        """

        self._geo_id = geo_id

    @property
    def geo_name(self):
        """Gets the geo_name of this EditionItem.  # noqa: E501


        :return: The geo_name of this EditionItem.  # noqa: E501
        :rtype: str
        """
        return self._geo_name

    @geo_name.setter
    def geo_name(self, geo_name):
        """Sets the geo_name of this EditionItem.


        :param geo_name: The geo_name of this EditionItem.  # noqa: E501
        :type: str
        """

        self._geo_name = geo_name

    @property
    def score(self):
        """Gets the score of this EditionItem.  # noqa: E501


        :return: The score of this EditionItem.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this EditionItem.


        :param score: The score of this EditionItem.  # noqa: E501
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EditionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
