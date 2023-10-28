# I have created this file - Aditya
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

    # return HttpResponse('<h1>Hello</h1> <a href="about"> about</a>')


def analyze(request):
    djtext = request.POST.get('text')
    remove = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcaps', 'off')
    charcount = request.POST.get('charcount', 'off')

    if remove == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)
    if fullcap == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Change to Upper case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if charcount == "on":
        analyze = []
        for char in djtext:
            analyze.append(char)
        params = {'purpose': 'Total Characters', 'analyzed_text': f'{analyzed}\nLength:{len(analyze)}'}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if remove == "off" and fullcap == "off" and charcount == "off":
        return HttpResponse("Please select any operation and try again.")

    return render(request, 'analyze.html', params)
    # return HttpResponse('About Aditya  <a href="/"> home</a>')
