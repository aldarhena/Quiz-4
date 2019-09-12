listGPA = (2.1, 2.5, 4, 3)
def Hadiah (GPA):
    Bonus = 500000
    Hadiah = GPA * Bonus
    return Hadiah

for GPA in listGPA:
    if GPA > 2.5:
        print("\nSelamat, Anda Mendapatkan Bonus Rp", Hadiah(GPA))
    else:
        print("\nMaaf, Anda Belum Beruntung. Silahkan Coba Lagi.")