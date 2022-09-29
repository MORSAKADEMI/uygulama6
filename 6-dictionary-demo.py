# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.


urunler = {
            '100': {'ad': 'IPhone 8', 'fiyat': '5000'}, 
            '101': {'ad': 'IPhone X', 'fiyat': '6000'}, 
            '102': {'ad': 'IPhone XR', 'fiyat': '7000'}
        }


# id = input("id: ")
# ad = input("ad: ")
# fiyat = input("fiyat: ")

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat
# }


print(urunler["100"]["fiyat"])