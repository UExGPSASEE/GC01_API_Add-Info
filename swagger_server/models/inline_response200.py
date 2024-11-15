# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, last_watched_minute: int=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param last_watched_minute: The last_watched_minute of this InlineResponse200.  # noqa: E501
        :type last_watched_minute: int
        """
        self.swagger_types = {
            'last_watched_minute': int
        }

        self.attribute_map = {
            'last_watched_minute': 'last_watched_minute'
        }
        self._last_watched_minute = last_watched_minute

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def last_watched_minute(self) -> int:
        """Gets the last_watched_minute of this InlineResponse200.

        Last watched minute  # noqa: E501

        :return: The last_watched_minute of this InlineResponse200.
        :rtype: int
        """
        return self._last_watched_minute

    @last_watched_minute.setter
    def last_watched_minute(self, last_watched_minute: int):
        """Sets the last_watched_minute of this InlineResponse200.

        Last watched minute  # noqa: E501

        :param last_watched_minute: The last_watched_minute of this InlineResponse200.
        :type last_watched_minute: int
        """

        self._last_watched_minute = last_watched_minute
