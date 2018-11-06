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


class Doc(object):
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
        'title': 'str',
        'pub_date': 'str',
        'load_date': 'str',
        'edition_id': 'int',
        'edition_shelf': 'int',
        'authors_name': 'str',
        'body': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'pub_date': 'pub_date',
        'load_date': 'load_date',
        'edition_id': 'edition_id',
        'edition_shelf': 'edition_shelf',
        'authors_name': 'authors_name',
        'body': 'body'
    }

    def __init__(self, id=None, title=None, pub_date=None, load_date=None, edition_id=None, edition_shelf=None, authors_name=None, body=None):  # noqa: E501
        """Doc - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._pub_date = None
        self._load_date = None
        self._edition_id = None
        self._edition_shelf = None
        self._authors_name = None
        self._body = None
        self.discriminator = None

        self.id = id
        if title is not None:
            self.title = title
        if pub_date is not None:
            self.pub_date = pub_date
        if load_date is not None:
            self.load_date = load_date
        if edition_id is not None:
            self.edition_id = edition_id
        if edition_shelf is not None:
            self.edition_shelf = edition_shelf
        if authors_name is not None:
            self.authors_name = authors_name
        if body is not None:
            self.body = body

    @property
    def id(self):
        """Gets the id of this Doc.  # noqa: E501


        :return: The id of this Doc.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Doc.


        :param id: The id of this Doc.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this Doc.  # noqa: E501


        :return: The title of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Doc.


        :param title: The title of this Doc.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def pub_date(self):
        """Gets the pub_date of this Doc.  # noqa: E501

        publication date  # noqa: E501

        :return: The pub_date of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._pub_date

    @pub_date.setter
    def pub_date(self, pub_date):
        """Sets the pub_date of this Doc.

        publication date  # noqa: E501

        :param pub_date: The pub_date of this Doc.  # noqa: E501
        :type: str
        """

        self._pub_date = pub_date

    @property
    def load_date(self):
        """Gets the load_date of this Doc.  # noqa: E501

        load date  # noqa: E501

        :return: The load_date of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._load_date

    @load_date.setter
    def load_date(self, load_date):
        """Sets the load_date of this Doc.

        load date  # noqa: E501

        :param load_date: The load_date of this Doc.  # noqa: E501
        :type: str
        """

        self._load_date = load_date

    @property
    def edition_id(self):
        """Gets the edition_id of this Doc.  # noqa: E501


        :return: The edition_id of this Doc.  # noqa: E501
        :rtype: int
        """
        return self._edition_id

    @edition_id.setter
    def edition_id(self, edition_id):
        """Sets the edition_id of this Doc.


        :param edition_id: The edition_id of this Doc.  # noqa: E501
        :type: int
        """

        self._edition_id = edition_id

    @property
    def edition_shelf(self):
        """Gets the edition_shelf of this Doc.  # noqa: E501

        todo  # noqa: E501

        :return: The edition_shelf of this Doc.  # noqa: E501
        :rtype: int
        """
        return self._edition_shelf

    @edition_shelf.setter
    def edition_shelf(self, edition_shelf):
        """Sets the edition_shelf of this Doc.

        todo  # noqa: E501

        :param edition_shelf: The edition_shelf of this Doc.  # noqa: E501
        :type: int
        """

        self._edition_shelf = edition_shelf

    @property
    def authors_name(self):
        """Gets the authors_name of this Doc.  # noqa: E501

        author name  # noqa: E501

        :return: The authors_name of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._authors_name

    @authors_name.setter
    def authors_name(self, authors_name):
        """Sets the authors_name of this Doc.

        author name  # noqa: E501

        :param authors_name: The authors_name of this Doc.  # noqa: E501
        :type: str
        """

        self._authors_name = authors_name

    @property
    def body(self):
        """Gets the body of this Doc.  # noqa: E501


        :return: The body of this Doc.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Doc.


        :param body: The body of this Doc.  # noqa: E501
        :type: str
        """

        self._body = body

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
        if not isinstance(other, Doc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
