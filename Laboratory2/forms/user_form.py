from flask_wtf import Form
from wtforms import StringField,SubmitField,  PasswordField, DateField, HiddenField,IntegerField
from wtforms import validators


class HolidayForm(Form):
    holiday_name = StringField("holiday name: ",[
                                    validators.DataRequired("Please enter holiday name."),
                                    validators.Length(5, 20, "Name should be from 5 to 20 symbols")
                                 ])

    season_year = StringField("season year: ",[
                                    validators.DataRequired("Please enter season year."),
                                    validators.Length(5, 20, "Name should be from 5 to 20 symbols")
                                 ])

    submit = SubmitField("Save")


class HolidayForm1(Form):

    season_year = StringField("season year: ",[
                                    validators.DataRequired("Please enter season year."),
                                    validators.Length(5, 20, "Name should be from 5 to 20 symbols")
                                 ])

    submit = SubmitField("Save")


class ClientForm(Form):
    passport_num = IntegerField("passport num: ",[
                                    validators.DataRequired("Please enter passport num.")
                                 ])

    holiday_name = StringField("holiday name: ",[
                                    validators.DataRequired("Please enter holiday name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

    present_name = StringField("present name: ",[
                                 validators.DataRequired("Please enter present name."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")])

    name = StringField("name: ",[
                                             validators.DataRequired("Please enter name."),
        validators.Length(5, 40, "Name should be from 5 to 40 symbols")
                                          ])

    family_state = StringField("Study Book: ",[
                                             validators.DataRequired("Please enter your study book."),
        validators.Length(10, 30, "Name should be from 10 to 30 symbols")
                                          ])

    age = IntegerField("age: ",[
                                    validators.DataRequired("Please enter age.")
                                 ])
    gender =  StringField("gender: ",[
                                             validators.DataRequired("Please enter gender."),
        validators.Length(10, 40, "Name should be from 10 to 40 symbols")
                                          ])

    submit = SubmitField("Save")


class ClientForm1(Form):

    holiday_name = StringField("holiday name: ",[
                                    validators.DataRequired("Please enter holiday name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

    present_name = StringField("present name: ",[
                                 validators.DataRequired("Please enter present name."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")])

    name = StringField("name: ",[
                                             validators.DataRequired("Please enter name."),
        validators.Length(5, 40, "Name should be from 5 to 40 symbols")
                                          ])

    family_state = StringField("Study Book: ",[
                                             validators.DataRequired("Please enter your study book."),
        validators.Length(10, 30, "Name should be from 10 to 30 symbols")
                                          ])

    age = IntegerField("age: ",[
                                    validators.DataRequired("Please enter age.")
                                 ])
    gender =  StringField("gender: ",[
                                             validators.DataRequired("Please enter gender."),
        validators.Length(10, 40, "Name should be from 10 to 40 symbols")
                                          ])

    submit = SubmitField("Save")

class PresentsForm(Form):
    present_name = StringField("present name: ",[
                                    validators.DataRequired("Please enter present name."),
                                    validators.Length(5, 20, "Name should be from 3 to 20 symbols")
                                 ])


    count_items = IntegerField("count items: ",[
                                    validators.DataRequired("Please enter count items.")
                                 ])

    store_name = StringField("store name: ",[
                                 validators.DataRequired("Please enter store name."),
        validators.Length(3, 30, "Name should be from 3 to 30 symbols")
                                 ])

    submit = SubmitField("Save")

class PresentsForm1(Form):

    count_items = IntegerField("count items: ",[
                                    validators.DataRequired("Please enter count items.")
                                 ])

    store_name = StringField("store name: ",[
                                 validators.DataRequired("Please enter store name."),
        validators.Length(3, 30, "Name should be from 3 to 30 symbols")
                                 ])

    submit = SubmitField("Save")