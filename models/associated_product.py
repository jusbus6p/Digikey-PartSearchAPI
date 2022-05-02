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


class AssociatedProduct(object):
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
        'product_url': 'str',
        'manufacturer_part_number': 'str',
        'minimum_order_quantity': 'int',
        'non_stock': 'bool',
        'packaging': 'PidVid',
        'quantity_available': 'int',
        'digi_key_part_number': 'str',
        'product_description': 'str',
        'unit_price': 'float',
        'manufacturer': 'PidVid',
        'manufacturer_public_quantity': 'int',
        'quantity_on_order': 'int',
        'max_quantity_for_distribution': 'int',
        'back_order_not_allowed': 'bool',
        'dk_plus_restriction': 'bool',
        'marketplace': 'bool',
        'supplier_direct_ship': 'bool',
        'pim_product_name': 'str',
        'supplier': 'str',
        'supplier_id': 'int',
        'is_ncnr': 'bool'
    }

    attribute_map = {
        'product_url': 'ProductUrl',
        'manufacturer_part_number': 'ManufacturerPartNumber',
        'minimum_order_quantity': 'MinimumOrderQuantity',
        'non_stock': 'NonStock',
        'packaging': 'Packaging',
        'quantity_available': 'QuantityAvailable',
        'digi_key_part_number': 'DigiKeyPartNumber',
        'product_description': 'ProductDescription',
        'unit_price': 'UnitPrice',
        'manufacturer': 'Manufacturer',
        'manufacturer_public_quantity': 'ManufacturerPublicQuantity',
        'quantity_on_order': 'QuantityOnOrder',
        'max_quantity_for_distribution': 'MaxQuantityForDistribution',
        'back_order_not_allowed': 'BackOrderNotAllowed',
        'dk_plus_restriction': 'DKPlusRestriction',
        'marketplace': 'Marketplace',
        'supplier_direct_ship': 'SupplierDirectShip',
        'pim_product_name': 'PimProductName',
        'supplier': 'Supplier',
        'supplier_id': 'SupplierId',
        'is_ncnr': 'IsNcnr'
    }

    def __init__(self, product_url=None, manufacturer_part_number=None, minimum_order_quantity=None, non_stock=None, packaging=None, quantity_available=None, digi_key_part_number=None, product_description=None, unit_price=None, manufacturer=None, manufacturer_public_quantity=None, quantity_on_order=None, max_quantity_for_distribution=None, back_order_not_allowed=None, dk_plus_restriction=None, marketplace=None, supplier_direct_ship=None, pim_product_name=None, supplier=None, supplier_id=None, is_ncnr=None, _configuration=None):  # noqa: E501
        """AssociatedProduct - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_url = None
        self._manufacturer_part_number = None
        self._minimum_order_quantity = None
        self._non_stock = None
        self._packaging = None
        self._quantity_available = None
        self._digi_key_part_number = None
        self._product_description = None
        self._unit_price = None
        self._manufacturer = None
        self._manufacturer_public_quantity = None
        self._quantity_on_order = None
        self._max_quantity_for_distribution = None
        self._back_order_not_allowed = None
        self._dk_plus_restriction = None
        self._marketplace = None
        self._supplier_direct_ship = None
        self._pim_product_name = None
        self._supplier = None
        self._supplier_id = None
        self._is_ncnr = None
        self.discriminator = None

        if product_url is not None:
            self.product_url = product_url
        if manufacturer_part_number is not None:
            self.manufacturer_part_number = manufacturer_part_number
        if minimum_order_quantity is not None:
            self.minimum_order_quantity = minimum_order_quantity
        if non_stock is not None:
            self.non_stock = non_stock
        if packaging is not None:
            self.packaging = packaging
        if quantity_available is not None:
            self.quantity_available = quantity_available
        if digi_key_part_number is not None:
            self.digi_key_part_number = digi_key_part_number
        if product_description is not None:
            self.product_description = product_description
        if unit_price is not None:
            self.unit_price = unit_price
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if manufacturer_public_quantity is not None:
            self.manufacturer_public_quantity = manufacturer_public_quantity
        if quantity_on_order is not None:
            self.quantity_on_order = quantity_on_order
        if max_quantity_for_distribution is not None:
            self.max_quantity_for_distribution = max_quantity_for_distribution
        if back_order_not_allowed is not None:
            self.back_order_not_allowed = back_order_not_allowed
        if dk_plus_restriction is not None:
            self.dk_plus_restriction = dk_plus_restriction
        if marketplace is not None:
            self.marketplace = marketplace
        if supplier_direct_ship is not None:
            self.supplier_direct_ship = supplier_direct_ship
        if pim_product_name is not None:
            self.pim_product_name = pim_product_name
        if supplier is not None:
            self.supplier = supplier
        if supplier_id is not None:
            self.supplier_id = supplier_id
        if is_ncnr is not None:
            self.is_ncnr = is_ncnr

    @property
    def product_url(self):
        """Gets the product_url of this AssociatedProduct.  # noqa: E501

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :return: The product_url of this AssociatedProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_url

    @product_url.setter
    def product_url(self, product_url):
        """Sets the product_url of this AssociatedProduct.

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :param product_url: The product_url of this AssociatedProduct.  # noqa: E501
        :type: str
        """

        self._product_url = product_url

    @property
    def manufacturer_part_number(self):
        """Gets the manufacturer_part_number of this AssociatedProduct.  # noqa: E501

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :return: The manufacturer_part_number of this AssociatedProduct.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_part_number

    @manufacturer_part_number.setter
    def manufacturer_part_number(self, manufacturer_part_number):
        """Sets the manufacturer_part_number of this AssociatedProduct.

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :param manufacturer_part_number: The manufacturer_part_number of this AssociatedProduct.  # noqa: E501
        :type: str
        """

        self._manufacturer_part_number = manufacturer_part_number

    @property
    def minimum_order_quantity(self):
        """Gets the minimum_order_quantity of this AssociatedProduct.  # noqa: E501

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :return: The minimum_order_quantity of this AssociatedProduct.  # noqa: E501
        :rtype: int
        """
        return self._minimum_order_quantity

    @minimum_order_quantity.setter
    def minimum_order_quantity(self, minimum_order_quantity):
        """Sets the minimum_order_quantity of this AssociatedProduct.

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :param minimum_order_quantity: The minimum_order_quantity of this AssociatedProduct.  # noqa: E501
        :type: int
        """

        self._minimum_order_quantity = minimum_order_quantity

    @property
    def non_stock(self):
        """Gets the non_stock of this AssociatedProduct.  # noqa: E501

        Indicates this product is a non stock product.  # noqa: E501

        :return: The non_stock of this AssociatedProduct.  # noqa: E501
        :rtype: bool
        """
        return self._non_stock

    @non_stock.setter
    def non_stock(self, non_stock):
        """Sets the non_stock of this AssociatedProduct.

        Indicates this product is a non stock product.  # noqa: E501

        :param non_stock: The non_stock of this AssociatedProduct.  # noqa: E501
        :type: bool
        """

        self._non_stock = non_stock

    @property
    def packaging(self):
        """Gets the packaging of this AssociatedProduct.  # noqa: E501


        :return: The packaging of this AssociatedProduct.  # noqa: E501
        :rtype: PidVid
        """
        return self._packaging

    @packaging.setter
    def packaging(self, packaging):
        """Sets the packaging of this AssociatedProduct.


        :param packaging: The packaging of this AssociatedProduct.  # noqa: E501
        :type: PidVid
        """

        self._packaging = packaging

    @property
    def quantity_available(self):
        """Gets the quantity_available of this AssociatedProduct.  # noqa: E501

        Quantity of the product available for immediate sale.  # noqa: E501

        :return: The quantity_available of this AssociatedProduct.  # noqa: E501
        :rtype: int
        """
        return self._quantity_available

    @quantity_available.setter
    def quantity_available(self, quantity_available):
        """Sets the quantity_available of this AssociatedProduct.

        Quantity of the product available for immediate sale.  # noqa: E501

        :param quantity_available: The quantity_available of this AssociatedProduct.  # noqa: E501
        :type: int
        """

        self._quantity_available = quantity_available

    @property
    def digi_key_part_number(self):
        """Gets the digi_key_part_number of this AssociatedProduct.  # noqa: E501

        The Digi-Key part number.  # noqa: E501

        :return: The digi_key_part_number of this AssociatedProduct.  # noqa: E501
        :rtype: str
        """
        return self._digi_key_part_number

    @digi_key_part_number.setter
    def digi_key_part_number(self, digi_key_part_number):
        """Sets the digi_key_part_number of this AssociatedProduct.

        The Digi-Key part number.  # noqa: E501

        :param digi_key_part_number: The digi_key_part_number of this AssociatedProduct.  # noqa: E501
        :type: str
        """

        self._digi_key_part_number = digi_key_part_number

    @property
    def product_description(self):
        """Gets the product_description of this AssociatedProduct.  # noqa: E501

        Catalog description of the product.  # noqa: E501

        :return: The product_description of this AssociatedProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this AssociatedProduct.

        Catalog description of the product.  # noqa: E501

        :param product_description: The product_description of this AssociatedProduct.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def unit_price(self):
        """Gets the unit_price of this AssociatedProduct.  # noqa: E501

        The price for a single unit of this product.  # noqa: E501

        :return: The unit_price of this AssociatedProduct.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this AssociatedProduct.

        The price for a single unit of this product.  # noqa: E501

        :param unit_price: The unit_price of this AssociatedProduct.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def manufacturer(self):
        """Gets the manufacturer of this AssociatedProduct.  # noqa: E501


        :return: The manufacturer of this AssociatedProduct.  # noqa: E501
        :rtype: PidVid
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this AssociatedProduct.


        :param manufacturer: The manufacturer of this AssociatedProduct.  # noqa: E501
        :type: PidVid
        """

        self._manufacturer = manufacturer

    @property
    def manufacturer_public_quantity(self):
        """Gets the manufacturer_public_quantity of this AssociatedProduct.  # noqa: E501

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :return: The manufacturer_public_quantity of this AssociatedProduct.  # noqa: E501
        :rtype: int
        """
        return self._manufacturer_public_quantity

    @manufacturer_public_quantity.setter
    def manufacturer_public_quantity(self, manufacturer_public_quantity):
        """Sets the manufacturer_public_quantity of this AssociatedProduct.

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :param manufacturer_public_quantity: The manufacturer_public_quantity of this AssociatedProduct.  # noqa: E501
        :type: int
        """

        self._manufacturer_public_quantity = manufacturer_public_quantity

    @property
    def quantity_on_order(self):
        """Gets the quantity_on_order of this AssociatedProduct.  # noqa: E501

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :return: The quantity_on_order of this AssociatedProduct.  # noqa: E501
        :rtype: int
        """
        return self._quantity_on_order

    @quantity_on_order.setter
    def quantity_on_order(self, quantity_on_order):
        """Sets the quantity_on_order of this AssociatedProduct.

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :param quantity_on_order: The quantity_on_order of this AssociatedProduct.  # noqa: E501
        :type: int
        """

        self._quantity_on_order = quantity_on_order

    @property
    def max_quantity_for_distribution(self):
        """Gets the max_quantity_for_distribution of this AssociatedProduct.  # noqa: E501

        Maximum order quantity for Distribution  # noqa: E501

        :return: The max_quantity_for_distribution of this AssociatedProduct.  # noqa: E501
        :rtype: int
        """
        return self._max_quantity_for_distribution

    @max_quantity_for_distribution.setter
    def max_quantity_for_distribution(self, max_quantity_for_distribution):
        """Sets the max_quantity_for_distribution of this AssociatedProduct.

        Maximum order quantity for Distribution  # noqa: E501

        :param max_quantity_for_distribution: The max_quantity_for_distribution of this AssociatedProduct.  # noqa: E501
        :type: int
        """

        self._max_quantity_for_distribution = max_quantity_for_distribution

    @property
    def back_order_not_allowed(self):
        """Gets the back_order_not_allowed of this AssociatedProduct.  # noqa: E501

        True if back order is not allowed for this product  # noqa: E501

        :return: The back_order_not_allowed of this AssociatedProduct.  # noqa: E501
        :rtype: bool
        """
        return self._back_order_not_allowed

    @back_order_not_allowed.setter
    def back_order_not_allowed(self, back_order_not_allowed):
        """Sets the back_order_not_allowed of this AssociatedProduct.

        True if back order is not allowed for this product  # noqa: E501

        :param back_order_not_allowed: The back_order_not_allowed of this AssociatedProduct.  # noqa: E501
        :type: bool
        """

        self._back_order_not_allowed = back_order_not_allowed

    @property
    def dk_plus_restriction(self):
        """Gets the dk_plus_restriction of this AssociatedProduct.  # noqa: E501

        If true- this product is not available for purchase through the Ordering API - it must be purchased through the  Digi-Key web site  # noqa: E501

        :return: The dk_plus_restriction of this AssociatedProduct.  # noqa: E501
        :rtype: bool
        """
        return self._dk_plus_restriction

    @dk_plus_restriction.setter
    def dk_plus_restriction(self, dk_plus_restriction):
        """Sets the dk_plus_restriction of this AssociatedProduct.

        If true- this product is not available for purchase through the Ordering API - it must be purchased through the  Digi-Key web site  # noqa: E501

        :param dk_plus_restriction: The dk_plus_restriction of this AssociatedProduct.  # noqa: E501
        :type: bool
        """

        self._dk_plus_restriction = dk_plus_restriction

    @property
    def marketplace(self):
        """Gets the marketplace of this AssociatedProduct.  # noqa: E501

        Product is a Marketplace product that ships direct from the supplier.  A separate shipping fee may apply  # noqa: E501

        :return: The marketplace of this AssociatedProduct.  # noqa: E501
        :rtype: bool
        """
        return self._marketplace

    @marketplace.setter
    def marketplace(self, marketplace):
        """Sets the marketplace of this AssociatedProduct.

        Product is a Marketplace product that ships direct from the supplier.  A separate shipping fee may apply  # noqa: E501

        :param marketplace: The marketplace of this AssociatedProduct.  # noqa: E501
        :type: bool
        """

        self._marketplace = marketplace

    @property
    def supplier_direct_ship(self):
        """Gets the supplier_direct_ship of this AssociatedProduct.  # noqa: E501

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :return: The supplier_direct_ship of this AssociatedProduct.  # noqa: E501
        :rtype: bool
        """
        return self._supplier_direct_ship

    @supplier_direct_ship.setter
    def supplier_direct_ship(self, supplier_direct_ship):
        """Sets the supplier_direct_ship of this AssociatedProduct.

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :param supplier_direct_ship: The supplier_direct_ship of this AssociatedProduct.  # noqa: E501
        :type: bool
        """

        self._supplier_direct_ship = supplier_direct_ship

    @property
    def pim_product_name(self):
        """Gets the pim_product_name of this AssociatedProduct.  # noqa: E501

        Pim name for the product  # noqa: E501

        :return: The pim_product_name of this AssociatedProduct.  # noqa: E501
        :rtype: str
        """
        return self._pim_product_name

    @pim_product_name.setter
    def pim_product_name(self, pim_product_name):
        """Sets the pim_product_name of this AssociatedProduct.

        Pim name for the product  # noqa: E501

        :param pim_product_name: The pim_product_name of this AssociatedProduct.  # noqa: E501
        :type: str
        """

        self._pim_product_name = pim_product_name

    @property
    def supplier(self):
        """Gets the supplier of this AssociatedProduct.  # noqa: E501

        The Supplier is the provider of the products to Digi-Key and some cases the customer directly.  # noqa: E501

        :return: The supplier of this AssociatedProduct.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this AssociatedProduct.

        The Supplier is the provider of the products to Digi-Key and some cases the customer directly.  # noqa: E501

        :param supplier: The supplier of this AssociatedProduct.  # noqa: E501
        :type: str
        """

        self._supplier = supplier

    @property
    def supplier_id(self):
        """Gets the supplier_id of this AssociatedProduct.  # noqa: E501

        Id for Supplier  # noqa: E501

        :return: The supplier_id of this AssociatedProduct.  # noqa: E501
        :rtype: int
        """
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, supplier_id):
        """Sets the supplier_id of this AssociatedProduct.

        Id for Supplier  # noqa: E501

        :param supplier_id: The supplier_id of this AssociatedProduct.  # noqa: E501
        :type: int
        """

        self._supplier_id = supplier_id

    @property
    def is_ncnr(self):
        """Gets the is_ncnr of this AssociatedProduct.  # noqa: E501

        Is product non-cancellable and non-returnable  # noqa: E501

        :return: The is_ncnr of this AssociatedProduct.  # noqa: E501
        :rtype: bool
        """
        return self._is_ncnr

    @is_ncnr.setter
    def is_ncnr(self, is_ncnr):
        """Sets the is_ncnr of this AssociatedProduct.

        Is product non-cancellable and non-returnable  # noqa: E501

        :param is_ncnr: The is_ncnr of this AssociatedProduct.  # noqa: E501
        :type: bool
        """

        self._is_ncnr = is_ncnr

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
        if issubclass(AssociatedProduct, dict):
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
        if not isinstance(other, AssociatedProduct):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssociatedProduct):
            return True

        return self.to_dict() != other.to_dict()
