from django import forms


class ProductCreationForm(forms.Form):
    BRICKS = 'Bricks'
    SAND = 'Sand'
    NAILS = 'Nails'
    SCREWS = 'Screws'
    CEMENT = 'Cement'
    GLUE = 'Glue'
    STEEL = 'Steel'
    PAINT = 'Paint'
    typ = [
        (BRICKS, 'Bricks'),
        (SAND, 'Sand'),
        (NAILS, 'Nails'),
        (SCREWS, 'Screws'),
        (CEMENT, 'Cement'),
        (GLUE, 'Glue'),
        (STEEL, 'Steel'),
        (PAINT, 'Paint')
        ]
    prod_type = forms.ChoiceField(
        choices=typ,
        label="Enter the Product Type"
   )

    quantity = forms.CharField(max_length=10)

    base_price = forms.DecimalField(max_digits=5, decimal_places=2)

    desc = forms.CharField(widget=forms.Textarea)


class give_review_form(forms.Form):
    e_mail = forms.EmailField(max_length=50, label="E-Mail Address")
    review = forms.CharField(widget=forms.Textarea, label="Review")