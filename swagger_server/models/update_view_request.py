# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UpdateViewRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, new_view_count: int=None):  # noqa: E501
        """UpdateViewRequest - a model defined in Swagger

        :param new_view_count: The new_view_count of this UpdateViewRequest.  # noqa: E501
        :type new_view_count: int
        """
        self.swagger_types = {
            'new_view_count': int
        }

        self.attribute_map = {
            'new_view_count': 'new_view_count'
        }
        self._new_view_count = new_view_count

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateViewRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateViewRequest of this UpdateViewRequest.  # noqa: E501
        :rtype: UpdateViewRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def new_view_count(self) -> int:
        """Gets the new_view_count of this UpdateViewRequest.

        The new view count value  # noqa: E501

        :return: The new_view_count of this UpdateViewRequest.
        :rtype: int
        """
        return self._new_view_count

    @new_view_count.setter
    def new_view_count(self, new_view_count: int):
        """Sets the new_view_count of this UpdateViewRequest.

        The new view count value  # noqa: E501

        :param new_view_count: The new_view_count of this UpdateViewRequest.
        :type new_view_count: int
        """
        if new_view_count is None:
            raise ValueError("Invalid value for `new_view_count`, must not be `None`")  # noqa: E501

        self._new_view_count = new_view_count
