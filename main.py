from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.text import LabelBase

import math
import arabic_reshaper
from bidi.algorithm import get_display


# ثبت فونت فارسی
LabelBase.register(
    name="Vazirmatn",
    fn_regular="Vazirmatn-Black.ttf"
)


def fa(text):
    return get_display(arabic_reshaper.reshape(text))


class FazeshApp(App):

    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        title = Label(
            text=fa("دستگاه فازش"),
            font_name="Vazirmatn",
            font_size=40,
            size_hint_y=None,
            height=80
        )

        self.angle_input = TextInput(
            hint_text=fa("زاویه (درجه)"),
            font_name="Vazirmatn",
            multiline=False,
            font_size=20
        )

        self.number_input = TextInput(
            hint_text=fa("عدد (برای ارتفاع‌سنج)"),
            font_name="Vazirmatn",
            multiline=False,
            font_size=20
        )

        height_btn = Button(
            text=fa("محاسبه ارتفاع"),
            font_name="Vazirmatn",
            font_size=20
        )
        height_btn.bind(on_press=self.calculate_height)

        slope_btn = Button(
            text=fa("محاسبه شیب"),
            font_name="Vazirmatn",
            font_size=20
        )
        slope_btn.bind(on_press=self.calculate_slope)

        self.result_label = Label(
            text=fa("نتیجه:"),
            font_name="Vazirmatn",
            font_size=22
        )

        main_layout.add_widget(title)
        main_layout.add_widget(self.angle_input)
        main_layout.add_widget(self.number_input)
        main_layout.add_widget(height_btn)
        main_layout.add_widget(slope_btn)
        main_layout.add_widget(self.result_label)

        return main_layout

    def calculate_height(self, instance):
        try:
            angle_deg = float(self.angle_input.text)
            number = float(self.number_input.text)

            angle_rad = math.radians(angle_deg)
            height = math.tan(angle_rad) * number

            self.result_label.text = fa(f"ارتفاع: {height:.3f}")
        except:
            self.result_label.text = fa("خطا: ورودی نامعتبر")

    def calculate_slope(self, instance):
        try:
            angle_deg = float(self.angle_input.text)

            angle_rad = math.radians(angle_deg)
            slope = math.tan(angle_rad)

            self.result_label.text = fa(f"شیب: {slope:.3f}")
        except:
            self.result_label.text = fa("خطا: ورودی نامعتبر")


FazeshApp().run()
