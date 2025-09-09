from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Football Store',
        'name': 'Josiah Naphta Simorangkir',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)