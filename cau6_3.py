class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Code by Quantrimang.com
aNam = Nam()
aNu = Nu()

print(aNam.getGender())   # Kết quả: Nam
print(aNu.getGender())    # Kết quả: Nữ
