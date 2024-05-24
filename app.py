from tkinter import *
import tkinter
from mydb import Database
import time


class NLPApp:
    def __init__(self):
        self.__name_input = ''
        self.__email_input = ''
        self.__password_input = ''
        self.db0 = Database()
        self.root = Tk()
        self.root.title("My NLP App")
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#4599A7')

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP App", bg='#4599A7', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label_1 = Label(self.root, text="Enter Email", bg='#4599A7', fg='white')
        label_1.pack(pady=(10, 10))

        self.__email_input = Entry(self.root, width=50)
        self.__email_input.pack(pady=(5, 10), ipady=4)

        label_2 = Label(self.root, text="Enter Password", bg='#4599A7', fg='white')
        label_2.pack(pady=(10, 10))

        self.__password_input = Entry(self.root, width=50, show="*")
        self.__password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Login', command=self.check_user_exist, bg='black', fg='white', width=30,
                           height=2)
        login_btn.pack(pady=(10, 10))

        label_3 = Label(self.root, text="Not a Member ?l", bg='#4599A7', fg='white')
        label_3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register', command=self.register_gui, bg='grey', fg='white', width=20,
                              height=2)
        redirect_btn.pack(pady=(10, 10))

    def analyze_sentiment(self):
        prompt = self.prompt_input

    def analyze_NER(self):
        prompt = self.prompt_input

    def analyze_emotion(self):
        prompt = self.prompt_input

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP App", bg='#4599A7', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Sentiment Analysis", bg='#4599A7', fg='white')
        heading2.pack(pady=(30, 30))

        prompt = Label(self.root, text="Enter Prompt", bg='#4599A7', fg='white')
        prompt.pack(pady=(10, 10))
        #
        # self.result = Label(self.root, text="Chatbot reply ", bg='#4599A7', fg='white')
        # self.result.pack(pady=(10, 10))

        self.prompt_input = Entry(self.root, width=50)
        self.prompt_input.pack(pady=(5, 10), ipady=4)

        analyze_btn = Button(self.root, text='Analyze Sentiment', command=self.analyze_sentiment, bg='black', fg='white',
                              width=30, height=2)
        analyze_btn.pack(pady=(10, 10))
        go_back_btn = Button(self.root, text='Main Menu', command=self.home_gui, bg='black', fg='white',
                              width=30, height=2)
        go_back_btn.pack(pady=(10, 10))


    def ner_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP App", bg='#4599A7', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Named Entity Recognition", bg='#4599A7', fg='white')
        heading2.pack(pady=(30, 30))

        prompt = Label(self.root, text="Enter Prompt", bg='#4599A7', fg='white')
        prompt.pack(pady=(10, 10))

        # self.result = Label(self.root, text="Chatbot reply ", bg='#4599A7', fg='white')
        # self.result.pack(pady=(10, 10))

        self.prompt_input = Entry(self.root, width=50)
        self.prompt_input.pack(pady=(5, 10), ipady=4)
        analyze_btn = Button(self.root, text='Analyze NER', command=self.analyze_NER, bg='black', fg='white',
                              width=30, height=2)
        analyze_btn.pack(pady=(10, 10))
        go_back_btn = Button(self.root, text='Main Menu', command=self.home_gui, bg='black', fg='white',
                              width=30, height=2)
        go_back_btn.pack(pady=(10, 10))
    def emotion_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP App", bg='#4599A7', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Emotion Analysis", bg='#4599A7', fg='white')
        heading2.pack(pady=(30, 30))
        # heading.configure(font=('verdana', 24, 'bold'))

        prompt = Label(self.root, text="Enter Prompt", bg='#4599A7', fg='white')
        prompt.pack(pady=(10, 10))

        # self.result = Label(self.root, text="Chatbot reply ", bg='#4599A7', fg='white')
        # self.result.pack(pady=(10, 10))

        self.prompt_input = Entry(self.root, width=50)
        self.prompt_input.pack(pady=(5, 10), ipady=4)
        analyze_btn = Button(self.root, text='Analyze Emotion', command=self.analyze_emotion, bg='black', fg='white',
                              width=30, height=2)
        analyze_btn.pack(pady=(10, 10))
        go_back_btn = Button(self.root, text='Main Menu', command=self.home_gui, bg='black', fg='white',
                              width=30, height=2)
        go_back_btn.pack(pady=(10, 10))

    def home_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP App", bg='#4599A7', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', command=self.sentiment_gui, bg='grey', fg='white', width=20,
                               height=2)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition ', command=self.ner_gui, bg='grey', fg='white', width=20,
                         height=2)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Analysis', command=self.emotion_gui, bg='grey', fg='white', width=20,
                             height=2)
        emotion_btn.pack(pady=(10, 10))

        log_out_btn = Button(self.root, text='Log out', command=self.login_gui, bg='grey', fg='white', width=20,
                             height=2)
        log_out_btn.pack(pady=(50, 10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP App", bg='#4599A7', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label_1 = Label(self.root, text="Enter Name", bg='#4599A7', fg='white')
        label_1.pack(pady=(10, 10))

        self.__name_input = Entry(self.root, width=50)
        self.__name_input.pack(pady=(5, 10), ipady=4)

        label_1 = Label(self.root, text="Enter Email", bg='#4599A7', fg='white')
        label_1.pack(pady=(10, 10))

        self.__email_input = Entry(self.root, width=50)
        self.__email_input.pack(pady=(5, 10), ipady=4)

        label_2 = Label(self.root, text="Enter Password", bg='#4599A7', fg='white')
        label_2.pack(pady=(10, 10))

        self.__password_input = Entry(self.root, width=50, show="*")
        self.__password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', command=self.perform_registration, bg='black', fg='white',
                              width=30, height=2)
        register_btn.pack(pady=(10, 10))

        label_3 = Label(self.root, text="Already a Member ?l", bg='#4599A7', fg='white')
        label_3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui, bg='grey', fg='white', width=20,
                              height=2)
        redirect_btn.pack(pady=(10, 10))

    def perform_registration(self):
        name = self.__name_input.get()
        email = self.__email_input.get()
        password = self.__password_input.get()
        already_member = self.db0.add_data(name, email, password)

        self.clear()
        if already_member:
            label_3 = Label(self.root, text="Email already registered !", bg='#4599A7', fg='white')
            label_3.pack(pady=(50, 10))
            label_4 = Label(self.root, text="Redirecting to login page !", bg='#4599A7', fg='white')
            label_4.pack(pady=(30, 10))
        else:
            label_3 = Label(self.root, text="Registration Successful !", bg='#4599A7', fg='white')
            label_3.pack(pady=(50, 10))
            label_4 = Label(self.root, text="Redirecting to login page !", bg='#4599A7', fg='white')
            label_4.pack(pady=(30, 10))

        # Schedule the login_gui function to be called after 2000 milliseconds (2 seconds)
        self.root.after(3000, self.login_gui)

    def check_user_exist(self):
        email = self.__email_input.get()
        password = self.__password_input.get()
        valid_member = self.db0.check_data(email, password)
        self.clear()
        if valid_member:
            label_3 = Label(self.root, text="Login Succesfull !", bg='#4599A7', fg='white')
            label_3.pack(pady=(50, 10))
            label_4 = Label(self.root, text="Redirecting to Main menu !", bg='#4599A7', fg='white')
            label_4.pack(pady=(30, 10))
            self.root.after(1000, self.home_gui)
        else:
            label_3 = Label(self.root, text="login failed !", bg='#4599A7', fg='white')
            label_3.pack(pady=(50, 10))
            label_4 = Label(self.root, text="Please try again !", bg='#4599A7', fg='white')
            label_4.pack(pady=(30, 10))
            self.root.after(2000, self.login_gui)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


nlp = NLPApp()