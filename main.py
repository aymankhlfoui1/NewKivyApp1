from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
import socket
import threading
import ssl
import dns.resolver

# تصميم الواجهة مع إضافة الحقول الجديدة
KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: "main"
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        canvas.before:
            Color:
                rgba: 0.1, 0.1, 0.1, 1
            Rectangle:
                size: self.size
                pos: self.pos

        Label:
            text: "[b]HTTP/UDP Custom Client[/b]"
            font_size: "24sp"
            size_hint: (1, 0.1)
            markup: True
            color: 1, 1, 1, 1

        GridLayout:
            cols: 2
            size_hint: (1, 0.25)
            spacing: 5

            Label:
                text: "Server IP:"
                color: 1, 1, 1, 1
            TextInput:
                id: ip_input
                hint_text: "e.g. 127.0.0.1"
                multiline: False

            Label:
                text: "Port:"
                color: 1, 1, 1, 1
            TextInput:
                id: port_input
                hint_text: "e.g. 8080"
                multiline: False

            Label:
                text: "Username:"
                color: 1, 1, 1, 1
            TextInput:
                id: username_input
                hint_text: "Enter username"
                multiline: False

            Label:
                text: "Password:"
                color: 1, 1, 1, 1
            TextInput:
                id: password_input
                hint_text: "Enter password"
                multiline: False
                password: True  # إخفاء النص

        GridLayout:
            cols: 2
            size_hint: (1, 0.3)
            spacing: 5

            BoxLayout:
                orientation: 'horizontal'
                Label:
                    text: "Use Payload"
                    color: 1, 1, 1, 1
                CheckBox:
                    id: payload_check

            BoxLayout:
                orientation: 'horizontal'
                Label:
                    text: "Enable SSL"
                    color: 1, 1, 1, 1
                CheckBox:
                    id: ssl_check

            BoxLayout:
                orientation: 'horizontal'
                Label:
                    text: "Enable DNS"
                    color: 1, 1, 1, 1
                CheckBox:
                    id: dns_check

            BoxLayout:
                orientation: 'horizontal'
                Label:
                    text: "UDP Custom"
                    color: 1, 1, 1, 1
                CheckBox:
                    id: udp_check
                    active: True

        Button:
            text: "[b]CONNECT[/b]"
            markup: True
            background_color: 0, 0.5, 0, 1
            size_hint: (1, 0.1)
            on_press: root.start_connection()

        TextInput:
            id: message_input
            hint_text: "Enter custom payload/message"
            size_hint: (1, 0.1)
            multiline: False
            background_color: 0.2, 0.2, 0.2, 1
            foreground_color: 1, 1, 1, 1

        ScrollView:
            size_hint: (1, 0.3)
            Label:
                id: log_label
                text: "[b]Connection Logs:[/b]"
                markup: True
                size_hint_y: None
                height: self.texture_size[1]
                color: 1, 1, 1, 1
'''

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client_socket = None
        self.is_connected = False
        self.thread = None
        self.context = ssl.create_default_context()

    def log_message(self, message, level="INFO"):
        """تسجيل الرسائل مع تلوين"""
        colors = {
            "INFO": "[color=00FF00]",
            "ERROR": "[color=FF0000]",
            "WARN": "[color=FFFF00]"
        }
        log_label = self.ids.log_label
        log_label.text += f"\n{colors.get(level, '')}[{level}] {message}[/color]"

    def resolve_dns(self, hostname):
        """تحليل DNS"""
        try:
            result = dns.resolver.resolve(hostname, 'A')
            return str(result[0])
        except Exception as e:
            self.log_message(f"DNS Error: {e}", "ERROR")
            return None

    def start_connection(self):
        """بدء الاتصال مع استخدام username و password"""
        ip = self.ids.ip_input.text
        port = self.ids.port_input.text
        username = self.ids.username_input.text  # قراءة اسم المستخدم
        password = self.ids.password_input.text  # قراءة كلمة المرور
        use_ssl = self.ids.ssl_check.active
        use_dns = self.ids.dns_check.active

        # إضافة تحقق من الحقول الإجبارية
        if not username or not password:
            self.log_message("Username and password are required!", "ERROR")
            return

        if use_dns:
            resolved_ip = self.resolve_dns(ip)
            if not resolved_ip:
                return
            ip = resolved_ip

        try:
            port = int(port)
        except ValueError:
            self.log_message("Port must be a number!", "ERROR")
            return

        try:
            # إنشاء السوكت
            if self.ids.udp_check.active:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            else:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # تشفير SSL
            if use_ssl:
                self.client_socket = self.context.wrap_socket(
                    self.client_socket,
                    server_hostname=ip
                )

            # الاتصال
            self.client_socket.connect((ip, port))
            self.is_connected = True
            self.log_message(f"Connected to {ip}:{port}")

            # إرسال بيانات الاعتماد (مثال)
            credentials = f"USER:{username}|PASS:{password}"
            self.client_socket.send(credentials.encode())

            # بدء استقبال الرسائل
            self.thread = threading.Thread(
                target=self.receive_messages,
                daemon=True
            )
            self.thread.start()

        except Exception as e:
            self.log_message(f"Connection failed: {str(e)}", "ERROR")

    # باقي الدوال (send_message, receive_messages, on_stop) تبقى كما هي

class CustomClientApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    CustomClientApp().run()
