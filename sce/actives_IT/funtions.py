def form_valid(self,form):
    try:
        form.save()
        return render(self.request, 'actives_IT/home.html')
    except IntegrityError:
        return HttpResponse("Duplicado")
