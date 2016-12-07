# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cmsplugin_filer_image.cms_plugins import FilerImagePlugin

from djangocms_rest_api.serializers.filerimageplugin_serializer import FilerImagePluginSerializer

from positive.serializers import PromoSerializer, TextPluginSerializer
from positive.cms_plugins import PromoPlugin
from djangocms_text_ckeditor.cms_plugins import TextPlugin

serializer_class_mapping = {
    FilerImagePlugin: FilerImagePluginSerializer,
    PromoPlugin: PromoSerializer,
    # TextPlugin: TextPluginSerializer,
}
