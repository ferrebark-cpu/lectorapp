from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.utils import platform

from jnius import autoclass
from android.activity import bind as bind_activity

Window.clearcolor = (0.98, 0.98, 0.99, 1)


class LectorApp(App):

    def build(self):

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        self.input_codigo = TextInput(
            hint_text="Código EAN...",
            multiline=False,
            font_size=24,
            size_hint_y=None,
            height=60
        )

        btn_scan = Button(
            text="[ ESCANEAR EAN ]",
            size_hint_y=None,
            height=60
        )
        btn_scan.bind(on_release=self.escanear_codigo)

        self.lbl_resultado = Label(
            text="Esperando lectura...",
            font_size=22
        )

        root.add_widget(self.input_codigo)
        root.add_widget(btn_scan)
        root.add_widget(self.lbl_resultado)

        if platform == "android":
            bind_activity(on_activity_result=self.on_activity_result)

        return root

    # -------- ESCANEO --------

    def escanear_codigo(self, instance):

        if platform != "android":
            self.lbl_resultado.text = "Solo funciona en Android"
            return

        Intent = autoclass('android.content.Intent')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')

        intent = Intent("com.google.zxing.client.android.SCAN")
        intent.putExtra("SCAN_MODE", "PRODUCT_MODE")

        currentActivity = PythonActivity.mActivity
        currentActivity.startActivityForResult(intent, 0)

    def on_activity_result(self, requestCode, resultCode, intent):

        if resultCode == -1:  # RESULT_OK
            contents = intent.getStringExtra("SCAN_RESULT")
            self.input_codigo.text = contents
            self.lbl_resultado.text = f"EAN detectado: {contents}"


if __name__ == "__main__":
    LectorApp().run()