from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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
    'december': 'dec eat no meat for the entire month'
}


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for mon in months:
        capitalized_month = mon.capitalize()
        mon_path = reverse('month-challenge', args=[mon])
        list_items += f'<li><a href="{mon_path}">{capitalized_month}</a></li>'

    response_data = """
    <ul>
        <li><a href='/challenges/january'>january</a></li>
    </ul>
    
    """
    return HttpResponse()


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
        response_html = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_html)

    except:
        return HttpResponseNotFound('<h1>this month is not supported</h1>')
