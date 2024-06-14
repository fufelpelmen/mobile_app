from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout


class TicTacToeGame(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for row in range(3):
            for col in range(3):
                btn = Button(font_size=64)  # Увеличили размер шрифта до 64
                btn.bind(on_release=self.button_pressed)
                self.add_widget(btn)
                self.buttons[row][col] = btn

    def button_pressed(self, instance):
        if instance.text == '':
            instance.text = self.current_player
            if self.check_winner():
                self.show_popup(f'Player {self.current_player} wins!')
                self.reset_board()
            elif self.is_board_full():
                self.show_popup('It\'s a draw!')
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0].text == self.buttons[row][1].text == self.buttons[row][2].text != '':
                return True
        for col in range(3):
            if self.buttons[0][col].text == self.buttons[1][col].text == self.buttons[2][col].text != '':
                return True
        if self.buttons[0][0].text == self.buttons[1][1].text == self.buttons[2][2].text != '':
            return True
        if self.buttons[0][2].text == self.buttons[1][1].text == self.buttons[2][0].text != '':
            return True
        return False

    def is_board_full(self):
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col].text == '':
                    return False
        return True

    def show_popup(self, message):
        layout = BoxLayout(orientation='vertical', padding=10)
        popup_label = Label(text=message)
        close_button = Button(text='Close', size_hint=(1, 0.25))
        layout.add_widget(popup_label)
        layout.add_widget(close_button)
        popup = Popup(title='Game Over', content=layout, size_hint=(0.5, 0.5))
        close_button.bind(on_release=popup.dismiss)
        popup.open()

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].text = ''
        self.current_player = 'X'


class TicTacToeApp(App):
    def build(self):
        return TicTacToeGame()


if __name__ == '__main__':
    TicTacToeApp().run()
