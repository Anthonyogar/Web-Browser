from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MyWebBrowser(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MyWebBrowser, self).__init__(*args, **kwargs)


		self.window = QWidget()
		self.window.setWindowTitle("Normadic Codes")

		self.layout = QVBoxLayout()
		self.Horizontal = QHBoxLayout()

		self.url_bar = QTextEdit()
		self.url_bar.setMaximumHeight(30)

		self.go_btn =QPushButton("Go")
		self.go_btn.setMinimumHeight(30)

		self.back_btn =QPushButton("<")
		self.back_btn.setMinimumHeight(30)

		self.forward_btn =QPushButton(">")
		self.forward_btn.setMinimumHeight(30)

		self.Horizontal.addWidget(self.url_bar)
		self.Horizontal.addWidget(self.go_btn)
		self.Horizontal.addWidget(self.back_btn)
		self.Horizontal.addWidget(self.forward_btn)

		self.browser = QWebEngineView()

		self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
		self.back_btn.clicked.connect(self.browser.back)
		self.forward_btn.clicked.connect(self.browser.forward)



		self.layout.addLayout(self.Horizontal)
		self.layout.addWidget(self.browser)

		self.browser.setUrl(QUrl("https://google.com"))

		self.window.setLayout(self.layout)
		self.window.show()

	def navigate(self, url):
		if not url.startswith("http"):
			url = "http://" + url
			self.url_bar.setText(url)
		self.browser.setUrl(QUrl(url))

app = QApplication([])
Window = MyWebBrowser()
app.exec_()