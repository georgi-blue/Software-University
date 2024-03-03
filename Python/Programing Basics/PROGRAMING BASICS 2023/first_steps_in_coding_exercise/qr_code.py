import pyqrcode
import png
from pyqrcode import QRCode

adress = 'https://moovitapp.com/index/bg/%D0%B3%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8_%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D1%80%D1%82-%D0%93%D1%80%D0%BE%D0%B7%D0%B4%D0%BE%D0%B2_%D0%9F%D0%B0%D0%B7%D0%B0%D1%80-Plovdiv-site_17617542-4897'
url = pyqrcode.create(adress)
url.png('example.png' , scale=8)