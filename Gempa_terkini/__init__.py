import bs4
import requests


class Calamity:

    def __init__(self,description):
        self.description = description

    def ekstraksi_data(self):
        pass

    def tampilkan_data(self):
        pass

    def show_on_bot(self):
        pass

    def get_image(self):
        pass
        
    def run(self):
        self.ekstraksi_data()
        # self.tampilkan_data()
        self.get_image()


class GempaTerkini(Calamity):
    def __init__(self):
       self.result = None

       Calamity.__init__(self,'To get the latest earthquake information in indonesia form BMKG.go.id\n')

    def ekstraksi_data(self):
        try:
            content = requests.get("https://www.bmkg.go.id")
        except Exception:
            print(Exception)
            return None

        if content.status_code == 200:
            soup = bs4.BeautifulSoup(content.text,'html.parser')

            result= soup.find('span',{'class':'waktu'})
            result= result.text.split(',')
            tanggal= result[0]
            waktu= result[1]
        
            result = soup.find('img',{'class':'img-responsive'})
            result = result['src']
            srcImage=result

            result = soup.find('div',{'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            result =result.findChildren('li')


            i=0
            magnitudo=None
            kedalaman=None
            ls=None
            bt=None
            pusat=None
            dirasakan=None

            for rest in result:
                if i == 1:
                    magnitudo = rest.text
                elif i == 2:
                    kedalaman = rest.text
                elif i == 3:
                    koordinat = rest.text.split(' - ')
                    ls = koordinat[0]
                    bt = koordinat[1]
                elif i == 4:
                    pusat = rest.text
                elif i == 5:
                    dirasakan = rest.text
                i+=1


            hasil = dict ()
            hasil["tanggal"] = tanggal
            hasil["waktu"] = waktu
            hasil["magnitudo"] = magnitudo
            hasil["kedalaman"] = kedalaman
            hasil["lokasi"] = {"ls": ls,"bt" : bt }
            hasil["pusat"] = pusat
            hasil["dirasakan"] = dirasakan
            hasil["src"] = srcImage
            self.result = hasil
        else:
            return None
            

    def tampilkan_data(self):
        if self.result is None:
            print("Tidak menemukan data")
            return

        print("Gempa terakhir berdasarkan BMKG")
        print(f"Tanggal:  {self.result['tanggal']}")
        print(f"Waktu:  {self.result['waktu']}")
        print(f"magnitudo:  {self.result['magnitudo']}")
        print(f"kedalaman:  {self.result['kedalaman']}")
        print(f"lokasi:  ls= {self.result['lokasi']['ls']}  bt= {self.result['lokasi']['bt']}")
        print(f"pusat:  {self.result['pusat']}")
        print(f"dirasakan:  {self.result['dirasakan']}")
        print(f"srcImage: {self.result['src']}")

    def show_on_bot(self):
        if self.result is None:
            return ("Tidak menemukan data")

            
        return (
            "Gempa terakhir berdasarkan BMKG \n"
            f"Tanggal:  {self.result['tanggal']} \n"
            f"Waktu:  {self.result['waktu']} \n"
            f"magnitudo:  {self.result['magnitudo']} \n"
            f"kedalaman:  {self.result['kedalaman']} \n"
            f"lokasi:  ls= {self.result['lokasi']['ls']}  bt= {self.result['lokasi']['bt']} \n"
            f"pusat:  {self.result['pusat']} \n"
            f"dirasakan:  {self.result['dirasakan']} \n"
        )

    def get_image(self) -> str:
        src_img= str(self.result['src'])
        # print(src_img)
        return src_img

if __name__=="__main__":
    gempa_di_indonesia = GempaTerkini()
    print('Deskripsi class ', gempa_di_indonesia.description)
    gempa_di_indonesia.run()