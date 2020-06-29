from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView



# Create your views here.
# from django.http import HttpResponse

# def recommender(request):
#     return render(request, 'recommender.html', {})

# def showresults(request):
#     searchterm = request.GET.get("searchterm", "")
#     return render(request, 'showresults.html', {'searchterm': searchterm})
from .models import ContractOpportunities
from .forms import SearchForm, SimilarsForm
from .doc2vec import search_by_query, most_similar, latest_opportunities

# class HomePageView(TemplateView):
#     template_name = 'recommender.html'

# class LandingPageView(ListView):
#     model = ContractOpportunities
#     template_name = 'landingpage.html'


# class SearchSimilarsView(ListView):
#     template_name = 'searchsimilars.html'
def landingpage(request):
    request.method = 'GET'
    form = SearchForm()
    matches = latest_opportunities()
    return render(request, 'landingpage.html', {'form': form,
                                                'matches': matches})

def search_results(request):
    form = SearchForm(request.GET)
    search_term = form['search_term'].value()
    matches =  search_by_query(search_term)

    return render(request, 'search_results.html', {'form': form,
                                                    'matches': matches
                                                    })


# source: https://stackoverflow.com/questions/4706255/how-to-get-value-from-form-field-in-django-framework

def similar_results(request):
    form = SimilarsForm(request.GET)
    base_document_idx = int(form['base_document_idx'].value())
    matches = most_similar(base_document_idx, 20)
    return render(request, 'search_results.html', {'matches': matches})
