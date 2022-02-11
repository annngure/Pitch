class UpdateProfile(FlaskForm):
    bio = TeaxtAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    