from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.


monthly_challenges = {
    'january': 'eat no meat for the entire month',
    'february': 'walk for atleast 20 mins everyday',
    'march': 'learn django for at least 20 mins everyday',
    'april': 'april eat no meat for the entire month',
    'may': ' may eat no meat for the entire month',
    'june': 'june eat no meat for the entire month',
    'july': ' july eat no meat for the entire month',
    'august': 'aug eat no meat for the entire month',
    'september': 'sep eat no meat for the entire month',
    'october': 'oct eat no meat for the entire month',
    'november': 'nov eat no meat for the entire month',
    'december': None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {"months": months,  })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('<h1>invalid month</h1>')
    redirect_month = months[month-1]
    print(redirect_month)
    redirect_path = reverse(
        'month-challenge', args=[redirect_month])  # challenge/january
    print(redirect_path)

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    # response_data = render_to_string("challenges/challenge.html")
    # return HttpResponse(response_data)

    except:
        raise Http404()
