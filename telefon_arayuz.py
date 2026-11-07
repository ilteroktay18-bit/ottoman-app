from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

# Arka planı koyu yapıyoruz
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class OttomanRobotUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Üst Kısım: Robot Yüzü / Durum Alanı (Siyah Kutu)
        self.yuz_frame = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.65)
        )
        
        self.yuz_label = Label(
            text="( •_• )\n\n[ Bekleme Modu ]",
            font_size='26sp',
            bold=True,
            color=(0, 1, 0.8, 1), # #00ffcc turkuaz/yeşil tonu
            halign='center',
            valign='middle'
        )
        self.yuz_frame.add_widget(self.yuz_label)
        self.add_widget(self.yuz_frame)

        # Alt Kısım: Konuşma Kutusu
        self.konusma_frame = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.35),
            padding=10
        )
        
        self.konusma_baslik = Label(
            text="Konuşma Kutusu",
            font_size='14sp',
            bold=True,
            color=(0.6, 0.6, 0.6, 1),
            size_hint=(1, 0.2),
            halign='left'
        )
        
        self.konusma_kutusu = Label(
            text="Merhaba! Sistemi başlatman bekleniyor...",
            font_size='18sp',
            color=(1, 1, 1, 1),
            size_hint=(1, 0.8),
            halign='center',
            valign='middle'
        )
        self.konusma_kutusu.bind(size=self.konusma_kutusu.setter('text_size'))
        
        self.konusma_frame.add_widget(self.konusma_baslik)
        self.konusma_frame.add_widget(self.konusma_kutusu)
        self.add_widget(self.konusma_frame)

class OttomanApp(App):
    def build(self):
        return OttomanRobotUI()

if __name__ == '__main__':
    OttomanApp().run()