# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
urunler = {
            '100': {'ad': 'IPhone 8', 'fiyat': '5000'}, 
            '101': {'ad': 'IPhone X', 'fiyat': '6000'}, 
            '102': {'ad': 'IPhone XR', 'fiyat': '7000'}
        }
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.
id = input("id: ")
ad = input("ad: ")
fiyat = input("fiyat: ")
urunler[id] = {
     "ad": ad,
     "fiyat": fiyat
 }
print(urunler["100"]["fiyat"])
print(urunler)