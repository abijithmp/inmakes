from django import forms
from .models import Person,District,Branch


class DateInput(forms.DateInput):
    input_type = 'date'

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

        widgets={
            'dob':DateInput()

        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['branch'].queryset = District.objects.none()

        # if 'district' in self.data:
        #     try:
        #         district_id = int(self.data.get('country'))
        #         self.fields['city'].queryset = District.objects.filter(country_id=country_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['city'].queryset = self.instance.country.city_set.order_by('name')