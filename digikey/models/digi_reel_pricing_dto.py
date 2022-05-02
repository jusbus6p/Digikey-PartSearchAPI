# coding: utf-8

"""
    PartSearch Api

    Search for products and retrieve details and pricing.  # noqa: E501

    OpenAPI spec version: Ps2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from digikey.configuration import Configuration


class DigiReelPricingDto(object):
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
        'reeling_fee': 'float',
        'unit_price': 'float',
        'extended_price': 'float',
        'requested_quantity': 'int',
        'search_locale_used': 'IsoSearchLocale'
    }

    attribute_map = {
        'reeling_fee': 'ReelingFee',
        'unit_price': 'UnitPrice',
        'extended_price': 'ExtendedPrice',
        'requested_quantity': 'RequestedQuantity',
        'search_locale_used': 'SearchLocaleUsed'
    }

    def __init__(self, reeling_fee=None, unit_price=None, extended_price=None, requested_quantity=None, search_locale_used=None, _configuration=None):  # noqa: E501
        """DigiReelPricingDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._reeling_fee = None
        self._unit_price = None
        self._extended_price = None
        self._requested_quantity = None
        self._search_locale_used = None
        self.discriminator = None

        if reeling_fee is not None:
            self.reeling_fee = reeling_fee
        if unit_price is not None:
            self.unit_price = unit_price
        if extended_price is not None:
            self.extended_price = extended_price
        if requested_quantity is not None:
            self.requested_quantity = requested_quantity
        if search_locale_used is not None:
            self.search_locale_used = search_locale_used

    @property
    def reeling_fee(self):
        """Gets the reeling_fee of this DigiReelPricingDto.  # noqa: E501

        Fee per reel ordered.  # noqa: E501

        :return: The reeling_fee of this DigiReelPricingDto.  # noqa: E501
        :rtype: float
        """
        return self._reeling_fee

    @reeling_fee.setter
    def reeling_fee(self, reeling_fee):
        """Sets the reeling_fee of this DigiReelPricingDto.

        Fee per reel ordered.  # noqa: E501

        :param reeling_fee: The reeling_fee of this DigiReelPricingDto.  # noqa: E501
        :type: float
        """

        self._reeling_fee = reeling_fee

    @property
    def unit_price(self):
        """Gets the unit_price of this DigiReelPricingDto.  # noqa: E501

        Price of a single unit of the product.  # noqa: E501

        :return: The unit_price of this DigiReelPricingDto.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this DigiReelPricingDto.

        Price of a single unit of the product.  # noqa: E501

        :param unit_price: The unit_price of this DigiReelPricingDto.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def extended_price(self):
        """Gets the extended_price of this DigiReelPricingDto.  # noqa: E501

        The total price of the requested reels and the reeling fee.  # noqa: E501

        :return: The extended_price of this DigiReelPricingDto.  # noqa: E501
        :rtype: float
        """
        return self._extended_price

    @extended_price.setter
    def extended_price(self, extended_price):
        """Sets the extended_price of this DigiReelPricingDto.

        The total price of the requested reels and the reeling fee.  # noqa: E501

        :param extended_price: The extended_price of this DigiReelPricingDto.  # noqa: E501
        :type: float
        """

        self._extended_price = extended_price

    @property
    def requested_quantity(self):
        """Gets the requested_quantity of this DigiReelPricingDto.  # noqa: E501

        The passed in quantity of the product you are looking to create a Digi-Reel with.  # noqa: E501

        :return: The requested_quantity of this DigiReelPricingDto.  # noqa: E501
        :rtype: int
        """
        return self._requested_quantity

    @requested_quantity.setter
    def requested_quantity(self, requested_quantity):
        """Sets the requested_quantity of this DigiReelPricingDto.

        The passed in quantity of the product you are looking to create a Digi-Reel with.  # noqa: E501

        :param requested_quantity: The requested_quantity of this DigiReelPricingDto.  # noqa: E501
        :type: int
        """

        self._requested_quantity = requested_quantity

    @property
    def search_locale_used(self):
        """Gets the search_locale_used of this DigiReelPricingDto.  # noqa: E501


        :return: The search_locale_used of this DigiReelPricingDto.  # noqa: E501
        :rtype: IsoSearchLocale
        """
        return self._search_locale_used

    @search_locale_used.setter
    def search_locale_used(self, search_locale_used):
        """Sets the search_locale_used of this DigiReelPricingDto.


        :param search_locale_used: The search_locale_used of this DigiReelPricingDto.  # noqa: E501
        :type: IsoSearchLocale
        """

        self._search_locale_used = search_locale_used

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
        if issubclass(DigiReelPricingDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DigiReelPricingDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DigiReelPricingDto):
            return True

        return self.to_dict() != other.to_dict()
