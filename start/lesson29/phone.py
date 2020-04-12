class Camera:
    def camera_method(self):
        print('this is main class Camera')

class Radio:
    def radio_method(self):
        print('this is main class Radio')

class CellPhone(Camera, Radio):
    def cellphone_method(self):
        print('this is second class CellPhone')


cphone1 = CellPhone()
cphone1.camera_method()
cphone1.radio_method()
cphone1.cellphone_method()