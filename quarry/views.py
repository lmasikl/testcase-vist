from django.db.models import F, ExpressionWrapper, IntegerField
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView
from quarry.forms import TruckModelFilter
from quarry.models import Truck, TruckModel


class Trucks(ListView):
    model = Truck
    template_name = 'trucks.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Trucks, self).get_context_data(*args, **kwargs)
        model_filter = TruckModelFilter(data=self.request.GET)
        if model_filter.is_valid():
            trucks = model_filter.execute(context['truck_list'])
        else:
            trucks = context['truck_list']

        trucks = trucks.values(
            'id', 'number', 'model__title', 'model__capacity', 'current_load'
        ).annotate(overload=ExpressionWrapper(
            100.0 * F('current_load') / F('model__capacity') - 100,
            output_field=IntegerField()
        ))

        context.update({
            'trucks': trucks,
            'model_filter': model_filter
        })

        return context


class UpdateTruck(UpdateView):
    model = Truck
    template_name = 'create_truck.html'
    fields = ('model', 'number', 'current_load', )

    def get_success_url(self):
        return reverse('trucks')


class CreateTruck(CreateView):
    model = Truck
    template_name = 'create_truck.html'
    fields = ('model', 'number', )

    def get_success_url(self):
        return reverse('trucks')


class CreateTruckModel(CreateView):
    model = TruckModel
    template_name = 'create_truck_model.html'
    fields = ('title', 'capacity')

    def get_success_url(self):
        return reverse('create-truck')
