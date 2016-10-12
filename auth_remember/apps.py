# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AuthRememberConfig(AppConfig):
    name = 'auth_remember'
    verbose_name = _("Remember Me")

    def ready(self):
        pass
