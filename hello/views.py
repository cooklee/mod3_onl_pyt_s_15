from random import randint

from django.http import HttpResponse
from django.shortcuts import render, redirect
from hello.models import Author, Book


# Create your views here.
def hello(request):
    return render(request, 'hello.html')


def kosta(request, a=1, b=6):
    liczba = randint(a, b)
    dane = {
        'min': a,
        'max': b,
        'liczba': liczba,
    }
    return render(request, 'kostka.html', context=dane)


def przywitanie(request):
    if request.method == 'GET':
        return render(request, 'przywitanie.html')
    else:
        imie = request.POST['imie']
        imie2 = request.POST['imie2']
        imie3 = request.POST['imie3']
        imie4 = request.POST['imie4']
        imie5 = request.POST['imie5']
        dane = {

        }
        return render(request, 'imie.html', context={'imie': imie})


def list_autorow(request):
    imie = request.GET.get('first_name', '')
    nazwisko = request.GET.get('last_name', '')
    rok_urodzenia_od = request.GET.get('bigger', '')
    rok_urodzenia_do = request.GET.get('smaller', '')
    if rok_urodzenia_do == '':
        rok_urodzenia_do = 10000
    if rok_urodzenia_od == '':
        rok_urodzenia_od = -10

    # authors = Author.objects.all() # takie zapytanie jest rownoznaczne z SELECT * form hello_author; i zwraca queryset
    authors = Author.objects.filter(
        imie__icontains=imie,
        nazwisko__icontains=nazwisko,
        rok__gte=rok_urodzenia_od,
        rok__lte=rok_urodzenia_do
    )
    return render(request, 'list_autorow.html', {'authors': authors, 'imie': imie, 'nazwisko': nazwisko,
                                                 'od': rok_urodzenia_od, 'do': rok_urodzenia_do})

def dodaj_autora(request):
    if request.method == 'GET':
        return render(request, 'add_author.html')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    year = request.POST['year']
    a = Author(imie=first_name, nazwisko=last_name,rok=year)
    a.save()
    return redirect('/authors/')


def add_book(request):
    authors = Author.objects.all()
    if request.method == 'GET':
        return render(request, 'add_book.html', {'authors':authors})
    title = request.POST['title']
    year = request.POST['year']
    author_id = request.POST['author']
    autor = Author.objects.get(id=author_id)
    # get -> funkcja która pobiera jeden i tylko jeden objekt z bazy jesli jest wiecej niż
    # jeden to wywali bład jeśli jest 0 to tez bład poleci
    b = Book.objects.create(title=title, year=year, author=autor)
    return redirect('/books/')



def show_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books':books})


#dodaj_autor/ -> wyświetli formularz dodawania autora (imie, nazwisko, rok)