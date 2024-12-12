from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import socket

class ZenithApp(App):
    def build(self):
        # Основной макет
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Поле ввода текста
        self.text_input = TextInput(hint_text="Введите сообщение")
        
        # Кнопка для отправки
        self.send_button = Button(text="Отправить")
        self.send_button.bind(on_press=self.send_message)
        
        # Поле для отображения ответа
        self.response_label = TextInput(readonly=True, hint_text="Ответ от ПК")
        
        # Добавляем виджеты
        layout.add_widget(self.text_input)
        layout.add_widget(self.send_button)
        layout.add_widget(self.response_label)
        
        return layout

    def send_message(self, instance):
        # Получаем текст из текстового поля
        message = self.text_input.text
        if not message.strip():
            self.response_label.text = "Введите сообщение!"
            return

        try:
            # Устанавливаем соединение с сервером на ПК
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(("192.168.1.100", 9090))  # Замените IP на IP вашего ПК
            
            # Отправляем сообщение
            client_socket.sendall(message.encode("utf-8"))
            
            # Получаем ответ
            response = client_socket.recv(1024).decode("utf-8")
            self.response_label.text = f"Ответ: {response}"
            
            # Закрываем соединение
            client_socket.close()
        except Exception as e:
            self.response_label.text = f"Ошибка: {e}"

# Запуск приложения
if __name__ == "__main__":
    ZenithApp().run()
