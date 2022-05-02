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


class KitPart(object):
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
        'associated_product': 'AssociatedProduct',
        'kit_part_quantity': 'int'
    }

    attribute_map = {
        'associated_product': 'AssociatedProduct',
        'kit_part_quantity': 'KitPartQuantity'
    }

    def __init__(self, associated_product=None, kit_part_quantity=None, _configuration=None):  # noqa: E501
        """KitPart - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._associated_product = None
        self._kit_part_quantity = None
        self.discriminator = None

        if associated_product is not None:
            self.associated_product = associated_product
        if kit_part_quantity is not None:
            self.kit_part_quantity = kit_part_quantity

    @property
    def associated_product(self):
        """Gets the associated_product of this KitPart.  # noqa: E501


        :return: The associated_product of this KitPart.  # noqa: E501
        :rtype: AssociatedProduct
        """
        return self._associated_product

    @associated_product.setter
    def associated_product(self, associated_product):
        """Sets the associated_product of this KitPart.


        :param associated_product: The associated_product of this KitPart.  # noqa: E501
        :type: AssociatedProduct
        """

        self._associated_product = associated_product

    @property
    def kit_part_quantity(self):
        """Gets the kit_part_quantity of this KitPart.  # noqa: E501

        Number of the product in the Kit.  # noqa: E501

        :return: The kit_part_quantity of this KitPart.  # noqa: E501
        :rtype: int
        """
        return self._kit_part_quantity

    @kit_part_quantity.setter
    def kit_part_quantity(self, kit_part_quantity):
        """Sets the kit_part_quantity of this KitPart.

        Number of the product in the Kit.  # noqa: E501

        :param kit_part_quantity: The kit_part_quantity of this KitPart.  # noqa: E501
        :type: int
        """

        self._kit_part_quantity = kit_part_quantity

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
        if issubclass(KitPart, dict):
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
        if not isinstance(other, KitPart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KitPart):
            return True

        return self.to_dict() != other.to_dict()
