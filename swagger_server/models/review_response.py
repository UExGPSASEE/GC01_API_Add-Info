# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ReviewResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, content_id: int=None, rating: int=None, user_id: int=None, profile_id: int=None):  # noqa: E501
        """ReviewResponse - a model defined in Swagger

        :param content_id: The content_id of this ReviewResponse.  # noqa: E501
        :type content_id: int
        :param rating: The rating of this ReviewResponse.  # noqa: E501
        :type rating: int
        :param user_id: The user_id of this ReviewResponse.  # noqa: E501
        :type user_id: int
        :param profile_id: The profile_id of this ReviewResponse.  # noqa: E501
        :type profile_id: int
        """
        self.swagger_types = {
            'content_id': int,
            'rating': int,
            'user_id': int,
            'profile_id': int
        }

        self.attribute_map = {
            'content_id': 'content_id',
            'rating': 'rating',
            'user_id': 'user_id',
            'profile_id': 'profile_id'
        }
        self._content_id = content_id
        self._rating = rating
        self._user_id = user_id
        self._profile_id = profile_id

    @classmethod
    def from_dict(cls, dikt) -> 'ReviewResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReviewResponse of this ReviewResponse.  # noqa: E501
        :rtype: ReviewResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content_id(self) -> int:
        """Gets the content_id of this ReviewResponse.

        The ID of the content being reviewed  # noqa: E501

        :return: The content_id of this ReviewResponse.
        :rtype: int
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id: int):
        """Sets the content_id of this ReviewResponse.

        The ID of the content being reviewed  # noqa: E501

        :param content_id: The content_id of this ReviewResponse.
        :type content_id: int
        """
        if content_id is None:
            raise ValueError("Invalid value for `content_id`, must not be `None`")  # noqa: E501

        self._content_id = content_id

    @property
    def rating(self) -> int:
        """Gets the rating of this ReviewResponse.

        User's rating for the content (1 to 5 stars)  # noqa: E501

        :return: The rating of this ReviewResponse.
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating: int):
        """Sets the rating of this ReviewResponse.

        User's rating for the content (1 to 5 stars)  # noqa: E501

        :param rating: The rating of this ReviewResponse.
        :type rating: int
        """
        if rating is None:
            raise ValueError("Invalid value for `rating`, must not be `None`")  # noqa: E501

        self._rating = rating

    @property
    def user_id(self) -> int:
        """Gets the user_id of this ReviewResponse.

        The ID of the user who wrote the review  # noqa: E501

        :return: The user_id of this ReviewResponse.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this ReviewResponse.

        The ID of the user who wrote the review  # noqa: E501

        :param user_id: The user_id of this ReviewResponse.
        :type user_id: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def profile_id(self) -> int:
        """Gets the profile_id of this ReviewResponse.

        The ID of the profile associated with the review  # noqa: E501

        :return: The profile_id of this ReviewResponse.
        :rtype: int
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id: int):
        """Sets the profile_id of this ReviewResponse.

        The ID of the profile associated with the review  # noqa: E501

        :param profile_id: The profile_id of this ReviewResponse.
        :type profile_id: int
        """
        if profile_id is None:
            raise ValueError("Invalid value for `profile_id`, must not be `None`")  # noqa: E501

        self._profile_id = profile_id
