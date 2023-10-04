from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("QuizPage.kv")


class QuizPageApp(App):
    def build(self):
        return QuizManager()


class QuizManager(ScreenManager):
    pass


class Question1Screen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "incorrect"


class Question2Screen(Screen):
    def answer_question(self,text):
        if (text.lower() == "beaver"):
            self.ids.test.text == "Correct"
            self.ids.test.text.font_size: 40
        else:
           self.ids.test.text == "Correct"
           self.ids.test.text.font_size: 70


class CorrectScreen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = "question2"


class IncorrectScreen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = "question1"


QuizPageApp().run()
