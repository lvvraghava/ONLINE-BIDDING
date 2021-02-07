from django import forms


class MaterialCreationForm(forms.Form):
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
        (PAINT, 'Paint'),
        ]
    prod_type = forms.ChoiceField(
        choices=typ,
        label="Enter the Product Type"
   )

    quantity = forms.CharField(max_length=10)

    high_value = forms.DecimalField(max_digits=5, decimal_places=2)

    desc = forms.CharField(widget=forms.Textarea)
