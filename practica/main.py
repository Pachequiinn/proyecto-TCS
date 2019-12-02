import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.slider import Slider
from kivy.uix.label import Label


class FramePrincipal(BoxLayout):
	def __init__(self):
		super(FramePrincipal,self).__init__()
		self.add_widget(ContainerAction())
		self.add_widget(ContainerEntradas())
		self.add_widget(ContainerButtons())

class ContainerAction(BoxLayout):
	def __init__(self):
		super(ContainerAction,self).__init__()

class ContainerEntradas(BoxLayout):
	def __init__(self):
		super(ContainerEntradas,self).__init__()
		lbl ='[color=ff3333]Ingresa h(x) y g(x) y presiona el botón de la convolución a realizar.[/color]'
		label = Label(text=lbl, size_hint_y=20, height=10, pos_hint={'top': 1})
		self.add_widget(label)
		self.add_widget(ContainerInputs())


class ContainerInputs(BoxLayout):
	def __init__(self):
		super(ContainerInputs,self).__init__()
		s = Scatter(size_hint=(None, None), pos=(100, 30))
		s.add_widget(TextInput(size_hint=(None, None), size=(100, 25)))
		self.add_widget(s)

		s = Scatter(size_hint=(None, None), pos=(300, 30))
		s.add_widget(TextInput(size_hint=(None, None), size=(100, 25)))
		self.add_widget(s)

class ContainerButtons(BoxLayout):
	def __init__(self):
		super(ContainerButtons,self).__init__()
		self.add_widget(ConvolucionFinita())
		self.add_widget(ConvolucionPeriodica())
		self.add_widget(ConvolucionCircular())

class ConvolucionFinita(BoxLayout):
	def __init__(self):
		super(ConvolucionFinita,self).__init__()
		self.BtnAction = Button(text="Convolución finita")
		self.add_widget(self.BtnAction)
		self.BtnAction.bind(on_press = self.iniciar_convolucion)
	def iniciar_convolucion(self,*arg):
		pass

class ConvolucionPeriodica(BoxLayout):
	def __init__(self):
		super(ConvolucionPeriodica,self).__init__()
		self.BtnAction = Button(text="Convoluión periódica")
		self.add_widget(self.BtnAction)
		self.BtnAction.bind(on_press = self.iniciar_convolucion)
	def iniciar_convolucion(self,*arg):
		pass

class ConvolucionCircular(BoxLayout):
	def __init__(self):
		super(ConvolucionCircular,self).__init__()
		self.BtnAction = Button(text="Convolución circular")
		self.add_widget(self.BtnAction)
		self.BtnAction.bind(on_press = self.iniciar_convolucion)
	def iniciar_convolucion(self,*arg):
		pass

class MainApp(App):
	title = "Práctica convolución discreta"
	def build(self):
		return FramePrincipal()

if __name__ == '__main__':
	MainApp().run()
