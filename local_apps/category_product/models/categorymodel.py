# -*- coding: utf-8 -*-
"""
This overrides the ProductCategory  with the class loaded from the
CATEGORYPRODUCT_CATEGORY_MODEL setting if it exists.
"""
from django.conf import settings
from shop.util.loader import load_class

#==============================================================================
# Extensibility
#==============================================================================
CATEGORY_MODEL = getattr(settings, 'CATEGORYPRODUCT_CATEGORY_MODEL',
    'category_product.models.defaults.productcategory.ProductCategory')
ProductCategory = load_class(CATEGORY_MODEL, 'CATEGORYPRODUCT_CATEGORY_MODEL')