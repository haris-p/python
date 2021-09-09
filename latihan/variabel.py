# variabel adalah untuk menyimpan sebuah nilai data

"""
x = 5
y = 2
print(x+y)

# varibel casting
x = "y"     - ini variabel string
y = 1       - ini variabel int
a = 1,3     - ini variabel float
untuk melihat typenya
print(type(x,y,a))

# variabel case sensitive adalah peka terhadap huruf besar dan kecil
x = 20
X = "ya"

# variabel tidak boleh asal harus menggunkan string dan tidak boleh diawali dgn spaci

# multi word variabel name
- camel case
myVariabel = "haris"

- pascal case
MyVariabel = "haris"

- snack case
my_variabel = "haris"

# assign multiple values
- many values(variabel satu line)
x = "haris","dika","rehan"
print("haris")
print("dika")
print("rehan")

- unpack collaction
x = ["mangga","jeruk"]
buah = x
print(x)

# global variabel (variabel yang diluar fungsi, seperti contoh diatas disebut variabel global)
-variabel diluar fungsi
x = "pohon"

def myfunct():
    print(x,"saya")

myfunct()

- variabel didalam fungsi dan bisa dipakai diluar fungsi
def myfunct():
    global x
    x = "mangga"
    print(x,"manis")
myfunct()

print(x,"pahit")

"""