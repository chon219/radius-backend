# -*- coding: utf-8 -*-

import json

from restless.views import Endpoint
from restless.auth import BasicHttpAuthMixin, login_required

from radius.models import Radcheck


def message(status, content):
    return {"status": status, "content": content}


class RadiusAPI(Endpoint, BasicHttpAuthMixin):
    @login_required
    def post(self, request):
        try:
            data = json.loads(request.body)
        except ValueError, e:
            return message(False, unicode(e))
        username = data.get('username')
        password = data.get('password')
        if not username:
            return message(False, "Username not provided.")
        if not password:
            return message(False, "Password not provided.")
        accounts = Radcheck.objects.filter(username=username) \
            .filter(attribute="Cleartext-Password")
        if accounts:
            return message(False, "Account existed.")
        else:
            Radcheck.objects.create(
                username=username,
                attribute="Cleartext-Password",
                op=":=",
                value=password)
            return message(True, "Acount created.")

    @login_required
    def put(self, request):
        try:
            data = json.loads(request.body)
        except ValueError, e:
            return message(False, unicode(e))
        username = data.get('username')
        password = data.get('password')
        if not username:
            return message(False, "Username not provided.")
        if not password:
            return message(False, "Password not provided.")
        accounts = Radcheck.objects.filter(username=username) \
            .filter(attribute="Cleartext-Password")
        if accounts:
            account = accounts[0]
            account.value = password
            account.save()
            return message(True, "Account updated.")
        else:
            Radcheck.objects.create(
                username=username,
                attribute="Cleartext-Password",
                op=":=",
                value=password)
            return message(True, "Account created.")

    @login_required
    def delete(self, request):
        username = request.params.get('username')
        if not username:
            return message(False, "Username not provided.")
        accounts = Radcheck.objects.filter(username=username) \
            .filter(attribute="Cleartext-Password")
        if accounts:
            for account in accounts:
                account.delete()
            return message(True, "Account deleted.")
        else:
            return message(False, "Account not found.")
