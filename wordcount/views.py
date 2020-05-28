from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist=fulltext.split()
    count=len(wordlist)
    dict={}
    for word in wordlist:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    sort = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':count,'dict':sort})
