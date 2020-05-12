from django.views.generic import View
from django.utils import timezone
from testapp.models import *
from testapp.render import *
import requests
from threading import Thread, activeCount
from testapp.render_to_file import Render


def send_email(file: list):
    r = requests.post(
        "https://api.mailgun.net/v3/######/messages",
        auth=("api", "key-########################################"),
        files=[("attachment", (file[0], open(file[1], "rb").read()))],
        data={"from": "No Reply <no-reply@##########>",
              "to": "me@########",
              "subject": "User Report",
              "text": "Requested user Report",
              "html": "<html>Requested user Report</html>"})


class Pdf(View):

    def get(self, request):
        data = student.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'data': data,
            'request': request
        }
        file = Render.render_to_file('pdf.html', params)
        thread = Thread(target=send_email, args=(file,))
        thread.start()
        return HttpResponse("Processed")