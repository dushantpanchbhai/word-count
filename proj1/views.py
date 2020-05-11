from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{'thisis':'dushant'})
    
def count(request):
    r=request.GET['box']
    wordcount=r.split()
    dic={}
    for i in wordcount:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    ans=sorted(dic.items(),key=lambda x:x[1],reverse=True)


    return render(request,'count.html',{'fulltext':r,'words':ans})