from flask_wtf import FlaskForm
from wtforms import widgets, StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SearchForm(FlaskForm):

    search = StringField("Search", validators=[DataRequired()])
    types = MultiCheckboxField(
        "Type",
        choices=[(1, "story"), (2, "job"), (3, "poll"), (4, "others")],
        coerce=int,
    )
    submit = SubmitField("Submit")
