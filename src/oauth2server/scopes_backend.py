from typing import Optional, Dict, Iterable

from django.contrib.auth.models import Permission
from oauth2_provider.models import AbstractApplication
from oauth2_provider.scopes import BaseScopes


class SettingsScopes(BaseScopes):
    def get_all_scopes(self) -> Dict[str, str]:
        return {
            codename: name
            for codename, name in Permission.objects.all().values_list(
                "codename", "name"
            )
        }

    def get_available_scopes(
        self,
        application: Optional[AbstractApplication] = None,
        request=None,
        *args,
        **kwargs
    ) -> Iterable[str]:
        return self.get_all_scopes().keys()

    def get_default_scopes(
        self,
        application: Optional[AbstractApplication] = None,
        request=None,
        *args,
        **kwargs
    ) -> Iterable[str]:
        return ["view_user"]
