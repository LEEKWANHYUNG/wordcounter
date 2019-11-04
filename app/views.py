from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def Result(request):
    text = request.GET["text"]
    context = {
        "name": "단어의 갯수는?",
        "list": list([10, 20, 30, 40]),
        "text": text.split(" ")
    }
    return render(request,"home.html",context)
