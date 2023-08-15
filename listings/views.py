from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing
from listings.forms import BandForm, ListingForm, ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})  # nous passons l'id au modèle


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/band_update.html',
                {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})


def listing_list(request):
    titles = Listing.objects.all()
    return render(request, 'listings/listing_list.html',
                  {'titles': titles})


def listing_detail(request, id):
    title = Listing.objects.get(id=id)
    return render(request, 'listings/listing_detail.html',
                  {'title': title})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer un nouvel « objet listing » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail de lobjet que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()

    return render(request,
            'listings/listing_create.html',
            {'form': form})


def listing_update(request, id):
    objet = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=objet)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('listing-detail', objet.id)
    else:
        form = ListingForm(instance=objet)

    return render(request,
                'listings/listing_update.html',
                {'form': form})


def listing_delete(request, id):
    title = Listing.objects.get(id=id)

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        title.delete()
        # rediriger vers la liste des groupes
        return redirect('listing-list')
    return render(request,
                  'listings/listing_delete.html',
                  {'title': title})


def contact(request):
    # # ajoutez ces instructions d'impression afin que nous puissions jeter un coup d'oeil à « request.method » et à « request.POST »
    # print('La méthode de requête est : ', request.method)
    # print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
            # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

        return redirect('redirection-users')  # ajoutez cette instruction de retour
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    return render(request,
                  'listings/contact.html',
                  {'form': form})


def redirection(request):
    return render(request, 'listings/redirection.html', )


def about(request):
    return render(request, 'listings/about.html', )
