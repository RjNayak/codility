from django.shortcuts import render

from .models import Document

from welcome.models import WelcomePage


# Create your views here.


def home(request):

    documents = Document.objects.all()

    grouped_document_list = group_by_topic(documents)

    welcomepagedata = WelcomePage.objects.first()

    return render(request, 'document/home.html', {'documents': grouped_document_list, 'welcomepagedata': welcomepagedata, 'nbar': 'document'})


def filtered_by_search(request):

    query = request.GET.get('search_box')

    documents = Document.objects.filter(title__icontains=query)

    grouped_document_list = group_by_topic(documents)

    welcomepagedata = WelcomePage.objects.first()

    return render(request, 'document/home.html', {'documents': grouped_document_list, 'welcomepagedata': welcomepagedata, 'nbar': 'document'})


def group_by_topic(documentlist):

    topic_list = []

    topic_dict_list = []

    for document in documentlist:

        topic_list.append(document.topic_type)

    for topic in topic_list:

        topic_dict = {}

        topic_dict[topic.name] = documentlist.filter(topic_type__name=topic)

        topic_dict_list.append(topic_dict)

    return topic_dict_list
