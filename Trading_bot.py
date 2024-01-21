import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window  # Import Window for getting window dimensions
import yfinance as yf

kivy.require('1.11.1')  # Specify Kivy version

class StockTradingApp(App):
    def build(self):
        # Create layout with top and bottom sections
        layout = BoxLayout(orientation='vertical')
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=0.1, padding=10)

        # Create a container within ScrollView to hold multiple widgets
        bottom_content_container = BoxLayout(orientation='vertical')
        bottom_content = ScrollView()
        bottom_content.add_widget(bottom_content_container)

        layout.add_widget(top_bar)
        layout.add_widget(bottom_content)

        # Add search bar for ticker symbol input
        search_bar = TextInput(hint_text="Enter stock ticker symbol")
        top_bar.add_widget(search_bar)

        # Add search button to top_bar
        search_button = Button(text="Search")
        search_button.bind(on_press=lambda x: self.search_stock(search_bar.text, bottom_content_container))
        top_bar.add_widget(search_button)

        return layout

    def search_stock(self, stock_symbol, bottom_content_container):
        try:
            current_price = yf.Ticker(stock_symbol).info['regularMarketPrice']
            if current_price:
                # Display the current price
                display_label = Label(text=f"Current price of {stock_symbol}: {current_price}")
                bottom_content_container.add_widget(display_label)  # Add to the container
            else:
                display_label = Label(text="Error: Could not fetch price")
                bottom_content_container.add_widget(display_label)
        except:
            display_label = Label(text="Error: Could not fetch price")
            bottom_content_container.add_widget(display_label)

if __name__ == '__main__':
    StockTradingApp().run()
