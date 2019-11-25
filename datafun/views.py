from django.shortcuts import render
from .models import Contact


from django.db.models import Q


def marz_index(request):
    projects = Contact.objects.all().order_by('-created_on')
    lookup = request.GET.get('q')
    print (lookup)
    # paginator=Paginator(projects,6)
    # try:
    #     page = int(request.GET.get('page','1'))
    # except:
    #     page = 1
    # try:
    #     projects = paginator.page(page)
    # except(EmptyPage, InvalidPage):
    #     projects=paginator.page(paginator.num_pages)

    if lookup:
            projects = Contact.objects.filter(Q(name__icontains = lookup) | Q(Contact__icontains = lookup) |Q(address__icontains = lookup)|Q(country__icontains = lookup) ).order_by('-created_on')
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)
