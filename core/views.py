from django.shortcuts import render
from django.contrib import messages
from core.forms import SendMsgForm
from core.api_data import *

# Create your views here.
def index(request):
    success = False
    if request.method == "POST":
        username = request.POST["username"]
        number = request.POST["number"]
        body = request.POST["body"]
        try:
            success = post_message(username, number, body)
        except:
            success = False

    return render(request, "core/index.html", {
        "success": success,
        "messages": fetch_response(),
        "form": SendMsgForm()
    })