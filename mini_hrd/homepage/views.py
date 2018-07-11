from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import message

from karyawan.models import Akun, Karyawan

# Create your views here.

def login_view(request):
	if request.POST:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				try:
					akun = Akun.objects.get(akun=user.id)
					login(request, user)
