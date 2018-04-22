from django.shortcuts import render
from django.http import HttpResponse
from . import calculadora
# Create your views here.

def barra(request):
    return HttpResponse("Calculadora Online")

def suma(request,op1,op2):
    print(request)
    num1 = int(op1)
    num2 = int(op2)
    resultado = calculadora.suma(num1,num2)
    return HttpResponse("Resultado: " + str(resultado))

def resta(request,op1,op2):
    num1 = int(op1)
    num2 = int(op2)
    resultado = calculadora.resta(num1,num2)
    return HttpResponse("Resultado: " + str(resultado))

def multiplicacion(request,op1,op2):
    num1 = int(op1)
    num2 = int(op2)
    resultado = calculadora.multiplicacion(num1,num2)
    return HttpResponse("Resultado: " + str(resultado))

def division(request,op1,op2):
    num1 = int(op1)
    num2 = int(op2)
    resultado = calculadora.division(num1,num2)
    return HttpResponse("Resultado: " + str(resultado))

def error(request):
    return HttpResponse("404 Not Found")
