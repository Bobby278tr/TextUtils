from django.http import HttpResponse # important to import http 
from django.shortcuts import render

def index(request):
    #return render(request, template name, dict variable name)
    return render(request, 'index.html') # with the help of render 3rd argument we can use variable in our template

def analyze(request):
    #get the text
    djtext=request.POST.get('text', 'default')# it return the text that you pass or give default
    
    #Check box values
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    charactercount=request.POST.get('charactercount', 'off')
    
    #check which checkbox is on
    
    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char
        params={'purpose':'Remove Punctuation', 'analyzed_text': analyzed}
        djtext=analyzed

    
    if(fullcaps == 'on'):
        analyzed=''
        for char in djtext:
            analyzed= analyzed + char.upper()
        params={'purpose':'Changed To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

            
    if(newlineremover=="on"):
        analyzed=''
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed= analyzed + char
        params={'purpose':'Remove new Line', 'analyzed_text': analyzed}
        djtext=analyzed

        
    if(extraspaceremover=="on"):
        analyzed=''
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed= analyzed + char
        params={'purpose':'Remove Extra Space', 'analyzed_text': analyzed}
        djtext=analyzed

    
    if(charactercount=="on"):
        analyzed=0
        analyze=djtext
        for char in djtext:
            analyzed= analyzed + 1
        params={'purpose': 'Counting Character ', 'analyzed_text': f"{analyze} \n No. of Characters present in the text are: {analyzed}"}
     
    if(charactercount !="on" and extraspaceremover!="on" and newlineremover!="on" and fullcaps != 'on' and removepunc != "on" ):
        return HttpResponse("<h1><em><strong>Please Select Any of the Operations</strong></em></h1>")
    
    return render(request, 'analyze.html', params)

                  
