from django.shortcuts import render
from django.db import models
from .models import player


# Create your views here.
def home(request):
	return render(request,"home.html")

def playerpg(request):
	return render(request,"playerpg.html")

def remplr(request):
	return render(request,"remplayer.html")

def updplr(request):
	return render(request,"update.html")

def playeradd(request):
	response={}
	flag=0
	n=request.POST["nme"]
	mail=request.POST["eml"]
	cntry=request.POST["cnty"]
	gms=request.POST["no"]
	tot=request.POST["scr"]
	plr=player.objects.all()
	for i in plr:
		if(n==i.name and mail==i.email):
			flag=1
	if(flag==1):
		response["msg2"]="Player Already Exist"
		return render(request,'playerpg.html',response)	
	else:
		plyr_list=player(name=n,email=mail,country=cntry,no_of_games=gms,tot_score=tot)
		plyr_list.save()
		response["msg1"]="Player Registration Succesfull!!!!"
		return render(request,'playerpg.html',response)


def remplayer(request):
	response={}
	try:
		n=request.POST["nme"]
		lst3=player.objects.get(name=n)
		lst3.delete()
		response["msg1"]="Player Removed Succesfully!!"
		return render(request,'remplayer.html',response)
	except Exception as e:
		print(e)
		response["msg2"]="player not Found!!!"
		return render(request,'remplayer.html',response)

def display(request):
	pdtls=player.objects.all()
	return render(request,"players.html",{'det':pdtls})