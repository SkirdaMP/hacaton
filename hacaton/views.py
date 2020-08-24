from random import choice

from django.shortcuts import render, redirect

from .forms import PostForm


def ar_form(request):
    result = 0
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(request.POST.get('field_count'))
            result = choice([1, 2])
            # return redirect('ar_form')
    else:
        form = PostForm()

    return render(request, 'index.html', {'form': form, 'result': result})

