from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    # Esto es un metodo de mi clase
    def get_perms(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tiene permiso para ingresar a este módulo u opción')
        messages.error(request, 'Contacte al administrador, Gracias')
        return HttpResponseRedirect(self.get_url_redirect())
