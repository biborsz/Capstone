from django.urls import path

from .views import landingpage, search_results, similar_results

urlpatterns = [

        path('', landingpage, name="landingpage"),
        # path('search/', SearchResultsView.as_view(), name="showresults"),
        # path('search_opportunities/', search_opportunities, name="search_opportunities"),
        path('search_results/', search_results, name="search_results"),
        path('similar_results/', similar_results, name="similar_results"),
]
