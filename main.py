
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

KV = r"""
#:import dp kivy.metrics.dp
#:import sp kivy.metrics.sp

<GreenButton@Button>:
    background_normal: ''
    background_color: 0.08, 0.48, 0.25, 1
    color: 1, 1, 1, 1
    font_size: sp(15)
    bold: True
    size_hint_y: None
    height: dp(48)

<WhiteButton@Button>:
    background_normal: ''
    background_color: 0.96, 0.97, 0.96, 1
    color: 0.08, 0.25, 0.14, 1
    font_size: sp(14)
    size_hint_y: None
    height: dp(44)

<Header@BoxLayout>:
    size_hint_y: None
    height: dp(70)
    padding: dp(10), dp(7)
    spacing: dp(8)
    canvas.before:
        Color:
            rgba: 0.08, 0.48, 0.25, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Image:
        source: 'logo.png'
        size_hint_x: None
        width: dp(55)
    Label:
        text: 'رزك'
        color: 1,1,1,1
        bold: True
        font_size: sp(25)
        halign: 'right'
    Label:
        text: 'عمّان، الأردن  📍'
        color: 1,1,1,1
        font_size: sp(12)
        halign: 'right'

<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        Header:
        BoxLayout:
            orientation: 'vertical'
            padding: dp(14)
            spacing: dp(10)
            ScrollView:
                do_scroll_x: False
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: dp(10)

                    Label:
                        text: 'أفضل أنواع الرز\\nبأفضل الأسعار'
                        color: 0.08,0.25,0.14,1
                        font_size: sp(24)
                        bold: True
                        halign: 'right'
                        text_size: self.width, None
                        size_hint_y: None
                        height: dp(70)

                    TextInput:
                        hint_text: 'شو نوع الرز اللي بتدور عليه؟ 🔍'
                        multiline: False
                        halign: 'right'
                        size_hint_y: None
                        height: dp(48)

                    Label:
                        text: '🔥 عروض اليوم'
                        color: 0.08,0.48,0.25,1
                        bold: True
                        font_size: sp(19)
                        halign: 'right'
                        text_size: self.width, None
                        size_hint_y: None
                        height: dp(32)

                    BoxLayout:
                        orientation: 'vertical'
                        padding: dp(14)
                        spacing: dp(6)
                        size_hint_y: None
                        height: dp(145)
                        canvas.before:
                            Color:
                                rgba: 0.05,0.34,0.15,1
                            RoundedRectangle:
                                pos: self.pos
                                size: self.size
                                radius: [18,18,18,18]
                        Label:
                            text: 'رز بسمتي هندي أصلي - 5 كغم'
                            color: 1,1,1,1
                            font_size: sp(20)
                            bold: True
                            halign: 'right'
                        Label:
                            text: 'ابتداءً من 4.99 د.أ'
                            color: 1,0.85,0.35,1
                            font_size: sp(18)
                            halign: 'right'
                        GreenButton:
                            text: 'اطلب الآن'
                            on_release: app.go_products()

                    Label:
                        text: 'تسوّق حسب النوع'
                        color: 0.08,0.25,0.14,1
                        bold: True
                        font_size: sp(18)
                        halign: 'right'
                        text_size: self.width, None
                        size_hint_y: None
                        height: dp(30)

                    GridLayout:
                        cols: 4
                        spacing: dp(6)
                        size_hint_y: None
                        height: dp(55)
                        Button:
                            text: 'بسمتي'
                            on_release: app.filter_products('بسمتي')
                        Button:
                            text: 'كالووز'
                            on_release: app.filter_products('كالووز')
                        Button:
                            text: 'مصري'
                            on_release: app.filter_products('مصري')
                        Button:
                            text: 'مندي'
                            on_release: app.filter_products('مندي')

                    Label:
                        text: 'الأكثر مبيعاً'
                        color: 0.08,0.25,0.14,1
                        bold: True
                        font_size: sp(19)
                        halign: 'right'
                        text_size: self.width, None
                        size_hint_y: None
                        height: dp(32)

                    GridLayout:
                        cols: 2
                        spacing: dp(8)
                        size_hint_y: None
                        height: dp(190)
                        BoxLayout:
                            orientation: 'vertical'
                            padding: dp(8)
                            spacing: dp(5)
                            Label:
                                text: 'رز بسمتي هندي\\n5 كغم\\n⭐ 4.8\\n5.50 د.أ'
                                color: 0.08,0.25,0.14,1
                                font_size: sp(15)
                                bold: True
                            GreenButton:
                                text: '+ أضف للسلة'
                                on_release: app.add_to_cart('رز بسمتي هندي', 5.50)
                        BoxLayout:
                            orientation: 'vertical'
                            padding: dp(8)
                            spacing: dp(5)
                            Label:
                                text: 'رز مصري متوسط الحبة\\n5 كغم\\n⭐ 4.6\\n3.25 د.أ'
                                color: 0.08,0.25,0.14,1
                                font_size: sp(15)
                                bold: True
                            GreenButton:
                                text: '+ أضف للسلة'
                                on_release: app.add_to_cart('رز مصري متوسط الحبة', 3.25)

            BoxLayout:
                size_hint_y: None
                height: dp(55)
                spacing: dp(5)
                GreenButton:
                    text: 'الرئيسية'
                WhiteButton:
                    text: 'المنتجات'
                    on_release: app.go_products()
                WhiteButton:
                    text: 'السلة'
                    on_release: app.go_cart()
                WhiteButton:
                    text: 'حسابي'

<ProductsScreen>:
    BoxLayout:
        orientation: 'vertical'
        Header:
        BoxLayout:
            orientation: 'vertical'
            padding: dp(14)
            spacing: dp(8)
            Label:
                text: 'قائمة المنتجات'
                color: 0.08,0.25,0.14,1
                font_size: sp(23)
                bold: True
                halign: 'right'
                text_size: self.width, None
                size_hint_y: None
                height: dp(38)
            Label:
                text: root.category
                color: 0.08,0.48,0.25,1
                halign: 'right'
                text_size: self.width, None
                size_hint_y: None
                height: dp(28)
            ScrollView:
                GridLayout:
                    id: product_list
                    cols: 1
                    spacing: dp(8)
                    size_hint_y: None
                    height: self.minimum_height
            BoxLayout:
                size_hint_y: None
                height: dp(55)
                spacing: dp(5)
                WhiteButton:
                    text: 'الرئيسية'
                    on_release: app.go_home()
                GreenButton:
                    text: 'السلة'
                    on_release: app.go_cart()

<CartScreen>:
    BoxLayout:
        orientation: 'vertical'
        Header:
        BoxLayout:
            orientation: 'vertical'
            padding: dp(14)
            spacing: dp(8)
            Label:
                text: 'سلة المشتريات'
                color: 0.08,0.25,0.14,1
                font_size: sp(23)
                bold: True
                halign: 'right'
                text_size: self.width, None
                size_hint_y: None
                height: dp(40)
            ScrollView:
                GridLayout:
                    id: cart_list
                    cols: 1
                    spacing: dp(6)
                    size_hint_y: None
                    height: self.minimum_height
            Label:
                id: total_label
                text: 'الإجمالي: 0.00 د.أ'
                color: 0.08,0.48,0.25,1
                bold: True
                font_size: sp(20)
                halign: 'right'
                text_size: self.width, None
                size_hint_y: None
                height: dp(38)
            GreenButton:
                text: 'إتمام الطلب'
                on_release: app.checkout()
            WhiteButton:
                text: 'متابعة التسوق'
                on_release: app.go_products()

class HomeScreen(Screen):
    pass

class ProductsScreen(Screen):
    category = StringProperty('كل الأنواع')

class CartScreen(Screen):
    pass

class RezakApp(App):
    cart = []

    def build(self):
        self.title = 'رزك'
        Builder.load_string(KV)
        sm = ScreenManager(transition=FadeTransition(duration=0.15))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ProductsScreen(name='products'))
        sm.add_widget(CartScreen(name='cart'))
        return sm

    def on_start(self):
        self.show_products()

    def go_home(self):
        self.root.current = 'home'

    def go_products(self):
        self.root.current = 'products'
        self.show_products()

    def filter_products(self, category):
        self.root.current = 'products'
        self.root.get_screen('products').category = category
        self.show_products(category)

    def show_products(self, category='كل الأنواع'):
        screen = self.root.get_screen('products')
        box = screen.ids.product_list
        box.clear_widgets()

        products = [
            ('رز بسمتي تاج محل', 4.60, 'بسمتي'),
            ('رز بسمتي هندي', 5.50, 'بسمتي'),
            ('رز مصري متوسط الحبة', 3.25, 'مصري'),
            ('رز كالووز أمريكي', 4.10, 'كالووز'),
            ('رز مندي بسمتي', 5.75, 'مندي'),
            ('رز قصير الحبة', 2.90, 'قصير'),
        ]

        for name, price, kind in products:
            if category != 'كل الأنواع' and kind != category:
                continue

            row = BoxLayout(size_hint_y=None, height=dp(76), padding=dp(8), spacing=dp(8))
            row.add_widget(Label(
                text=f'{name}\\n⭐ 4.7    {price:.2f} د.أ',
                color=(.08,.20,.12,1),
                font_size=sp(15),
                halign='right',
                valign='middle'
            ))
            btn = Button(
                text='+ أضف',
                size_hint_x=None,
                width=dp(88),
                background_normal='',
                background_color=(.08,.48,.25,1),
                color=(1,1,1,1),
                bold=True
            )
            btn.bind(on_release=lambda _btn, n=name, p=price: self.add_to_cart(n, p))
            row.add_widget(btn)
            box.add_widget(row)

    def add_to_cart(self, name, price):
        self.cart.append((name, price))
        self.update_cart()
        self.show_message('تمت الإضافة', f'تمت إضافة {name} إلى السلة.')

    def go_cart(self):
        self.root.current = 'cart'
        self.update_cart()

    def update_cart(self):
        screen = self.root.get_screen('cart')
        box = screen.ids.cart_list
        box.clear_widgets()
        total = sum(price for _, price in self.cart)

        if not self.cart:
            box.add_widget(Label(
                text='السلة فارغة حالياً 🛒',
                color=(.3,.3,.3,1),
                font_size=sp(18),
                size_hint_y=None,
                height=dp(60)
            ))
        else:
            for name, price in self.cart:
                box.add_widget(Label(
                    text=f'{name}    —    {price:.2f} د.أ',
                    color=(.08,.20,.12,1),
                    font_size=sp(15),
                    halign='right',
                    size_hint_y=None,
                    height=dp(44)
                ))

        screen.ids.total_label.text = f'الإجمالي: {total:.2f} د.أ'

    def checkout(self):
        if not self.cart:
            self.show_message('السلة فارغة', 'أضف منتجات أولاً ثم أتمم الطلب.')
            return

        total = sum(price for _, price in self.cart)
        self.show_message(
            'تم تأكيد الطلب ✅',
            f'شكراً لك!\\nإجمالي الطلب: {total:.2f} د.أ\\nسيتم التواصل معك لتأكيد عنوان التوصيل.'
        )
        self.cart.clear()
        self.update_cart()

    def show_message(self, title, message):
        Popup(
            title=title,
            content=Label(text=message, halign='center', valign='middle'),
            size_hint=(.82, .30)
        ).open()

if __name__ == '__main__':
    RezakApp().run()
