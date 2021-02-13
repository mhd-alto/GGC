from django.shortcuts import render, redirect
from .models import Trade
from .forms import TradeForm
from django.utils.text import slugify


def trade_page(request):
    trades = Trade.objects.all()
    count = trades.count()
    context = {
        'trades': trades,
        'count': count, }
    return render(request, 'trade_page.html', context)


def add_in_trade(request):
    # Is it a post request ?
    if request.method == 'POST':
        # Instantiate a CreateTrade with the submitted data
        trade_form = TradeForm(request.POST, files=request.FILES)
        # The data are valid ?
        if trade_form.is_valid():
            # Create a new trade object but don't save it to the database just yet
            new_trade_form = trade_form.save(commit=False)
            # request user name to put it in trade
            new_trade_form.author = request.user
            # create friendly links
            new_trade_form.slug = slugify(new_trade_form.title)
            # is image included
            if request.FILES:
                # add the image to trade
                new_trade_form.image = request.FILES["image"]
            # save trade
            new_trade_form.save()
            # save tags
            trade_form.save_m2m()
            # to go to trade page
            return redirect('trade_page')
    else:
        # create empty trade
        trade_form = TradeForm()
        # a dictionary that hold form of trade
    context = {'form': trade_form}
    # to represent add trade page
    return render(request, 'add_in_trade.html', context)
