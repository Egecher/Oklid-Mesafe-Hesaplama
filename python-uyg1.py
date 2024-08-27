import math

points = [(1,2),(3,4),(5,6)]

# Verilen iki nokta arasındaki Öklid mesafesini hesaplayan bir fonksiyon tanımlanıyor.
def euclideanDistance(point1, point2):
    # Öklid mesafesi, iki nokta arasındaki düz bir hattın uzunluğudur.
    # Bu mesafe, iki noktanın x ve y koordinatları arasındaki farkların karelerinin toplamının karekökü alınarak hesaplanır.
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
  
# Mesafeleri saklamak için boş bir liste oluşturuluyor.
distances = []

# Tüm noktalar arasında mesafeleri hesaplamak için çift döngü kullanılıyor.
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        # Her iki nokta çifti arasındaki mesafe hesaplanıyor.
        distance = euclideanDistance(points[i], points[j])
        # Hesaplanan mesafe, distances listesine ekleniyor.
        distances.append(distance)
   
# Mesafeler listesindeki en küçük mesafe bulunuyor.     
min_distance = min(distances)

# Tüm mesafeler ve en küçük mesafe ekrana yazdırılıyor.
print('Tüm mesafeler: ', distances)
print('En küçük mesafe: ', min_distance)
