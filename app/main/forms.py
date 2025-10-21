from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, SubmitField, DateField, DecimalField, SelectField
from wtforms.validators import ValidationError, DataRequired, InputRequired, NumberRange, Length, Optional
from flask import current_app
import filetype

class InviteForm(FlaskForm):
    weeks = IntegerField("Weeks", default=0, validators=[NumberRange(min=0)])
    days = IntegerField("Days", default=0, validators=[NumberRange(min=0)])
    hours = IntegerField("Hours", default=0, validators=[NumberRange(min=0)])
    minutes = IntegerField("Minutes", default=0, validators=[NumberRange(min=0)])
    seconds = IntegerField("Seconds", default=0, validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField("Generate Link")


class IDForm(FlaskForm):
    image = FileField("Upload ")

    def __init__(self, allowed, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image.validators = [
            FileRequired('File was empty!'),
            FileAllowed(allowed, "Only images are allowed!")
        ]
    first_name = StringField("First Name", validators=[DataRequired(), Length(max=50)])
    middle_name = StringField("Middle Name", validators=[Optional(), Length(max=50)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(max=50)])
    eye_color = SelectField(
        "Eye Color",
        choices=[
            ("", "Select eye color"),
            ("brown", "Brown"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("hazel", "Hazel"),
            ("gray", "Gray"),
            ("black", "Black")
        ],
        validators=[DataRequired()]
    )
    hair_color = SelectField(
        "Hair Color",
        choices=[
            ("", "Select hair color"),
            ("black", "Black"),
            ("brown", "Brown"),
            ("blonde", "Blonde"),
            ("red", "Red"),
            ("gray", "Gray"),
            ("white", "White")
        ],
        validators=[DataRequired()]
    )
    address = StringField("Address", validators=[DataRequired(), Length(max=200)])
    date_of_birth = DateField("Date of Birth", format='%Y-%m-%d', validators=[DataRequired()])
    height = DecimalField("Height (in cm)", validators=[DataRequired(), NumberRange(min=0)])
    weight = DecimalField("Weight (in kg)", validators=[DataRequired(), NumberRange(min=0)])
    gender = SelectField(
        "Gender",
        choices=[("", "Select gender"), ("male", "Male"), ("female", "Female"), ("other", "Other")],
        validators=[DataRequired()]
    )
    submit = SubmitField("Submit Application")


    def validate_image(self, image):
        data = image.data.read()
        kind = filetype.guess(data)
        image.data.seek(0)  # Reset file pointer after reading
        if kind is None or kind.extension not in current_app.config['UPLOAD_EXTENSIONS']:
            raise ValidationError("Invalid image format.")