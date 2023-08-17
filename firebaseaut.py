import pyrebase
from firebase import firebase
import json
from kivy.app import App

config = {
    "apiKey": "AIzaSyBQoLAxEA4BpGoK_bwsuKr9vvB1GWL78aY",
    "authDomain": "kivy-auth-test-bc4f6.firebaseapp.com",
    "databaseURL":"https://kivy-auth-test.firebaseio.com",
    "projectId": "kivy-auth-test-bc4f6",
    "storageBucket": "kivy-auth-test-bc4f6.appspot.com",
    "messagingSenderId": "1037097064331",
    "appId": "1:1037097064331:web:abce574b82b9898edb418e",
    "measurementId": "G-NLR772SRQ1"
}

firebase_auth = pyrebase.initialize_app(config)

#Enter Your firebase RealTime database url here
firebase_data = firebase.FirebaseApplication("https://kivy-auth-test-bc4f6-default-rtdb.firebaseio.com/" , None)

class MyFirebase() :
    def sign_up(self , fullname , email , password):

        try :
            # RealTime Database
            data = {
                "Name": fullname,
                "Email": email,
                "Password": password
            }
            result = firebase_data.post("/kivy-auth-test/Pegawai", data) #Enter your database table name here

            # Creating User
            signup_auth = firebase_auth.auth()
            user_signup = signup_auth.create_user_with_email_and_password(email, password)
            print("SignUp Successfully")
            App.get_running_app().root.ids["signup_screen"].ids["signup_screen"].text = "[b][color=#FF0000]Signup Succesfully.[/color][/b]"
        except:
            App.get_running_app().root.ids["signup_screen"].ids["signup_screen"].text = "[b][color=#0000FF]Please enter correct details.[/color][/b]"




    def sign_in(self , email , password):
        signin_auth = firebase_auth.auth()

        try :
            user_login = signin_auth.sign_in_with_email_and_password(email,password)
            print("Login Successfully !!!")
            print(user_login["registered"])
            path_to_home = user_login["registered"]

            if path_to_home == True :
                print("hello")
                App.get_running_app().root.ids["login_screen"].ids["login_message"].text = ""
                App.get_running_app().change_screen("home_screen")
                App.get_running_app().root.ids["home_screen"].ids["passing_email"].text = "[b]%s[/b]" %email

        except :
            App.get_running_app().root.ids["login_screen"].ids["login_message"].text = "[b]Invalid Email or Password[/b]"

    def forgot_password(self , email) :
        try:
            auth = firebase_auth.auth()
            auth.send_password_reset_email(email)
            App.get_running_app().root.ids["forgot_password_screen"].ids["forgot_message"].text = "[b]Thanks! Please check your email .[/b]"
        except:
            App.get_running_app().root.ids["forgot_password_screen"].ids["forgot_message"].text = "[b][color=#FF0000]Please Enter Correct Email !.[/color][/b]"
