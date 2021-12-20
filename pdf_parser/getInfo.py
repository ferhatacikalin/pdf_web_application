import re
import datetime as dt


class Author():
    def __init__(self):
        self.id = []
        self.student_name = []
        self.e_type = []
        self.data = ReadTxt().open_txt()
        self.get_student_id()
        self.get_education_type()
        self.get_student_name()

    def get_student_id(self):
        self.id = re.findall("Öğrenci No:.*", self.data)
        for i in range(len(self.id)):
            self.id[i] = self.id[i][12:21]
        # print(self.id)

    def get_student_name(self):
        self.student_name = re.findall("Adı Soy.*", self.data)
        for i in range(len(self.student_name)):
            self.student_name[i] = self.student_name[i][12:]
        # print(self.student_name)

    def get_education_type(self):
        self.e_type = self.id.copy()
        for i in range(len(self.e_type)):
            self.e_type[i] = self.e_type[i][5:6]
            if self.e_type[i] == '1':
                self.e_type[i] = "Birinci Öğretim"
            elif self.e_type[i] == '2':
                self.e_type[i] = "İkinci Öğretim"
            else:
                print("Öğrenci Numarası Yanlış Girildi Kontrol Edin")
        # print(e_type)


class Advisor():
    def __init__(self):
        self.advisor_name = []
        self.advisor_degree = []
        self.data = ReadTxt().open_txt()
        self.get_advisor()

    def get_advisor(self):
        advisors = re.findall("(.*Danışman)", self.data)
        for i in range(len(advisors)):
            advisors[i] = advisors[i].strip()
            advisors[i] = advisors[i][:-8]
        for i in range(len(advisors)):
            y = re.search("(.*Dr.)(.+)", advisors[i])
            if y:
                # print(y.group(1))
                self.advisor_degree.append(y.group(1).strip())
                self.advisor_name.append(y.group(2).strip())
        # print(self.advisor_name)
        # print(self.advisor_degree)


class Jury():
    def __init__(self):
        self.jury_name = []
        self.jury_degree = []
        self.data = ReadTxt().open_txt()
        self.get_jury()

    def get_jury(self):
        jury = re.findall("(.*Jüri)", self.data)

        for i in range(len(jury)):
            jury[i] = jury[i].strip()
            jury[i] = jury[i][:-4]

        for i in jury:
            y = re.search("(.*r.)(.*Ü)", i)
            if y == None:
                x = re.search("(.*Dr.)(.+)", i)
                # print(x.group(1))
                if x:
                    self.jury_degree.append(x.group(1).strip())
                    self.jury_name.append(x.group(2).strip())
            else:
                z = re.search("(.*si)(.+)", i)
                self.jury_degree.append(z.group(1).strip())
                self.jury_name.append(z.group(2).strip())

        # print(self.jury_degree)
        # print(self.jury_name)


class Project():
    def __init__(self):
        self.deliveryTime = []
        self.keyword = []
        self.project_name = []
        self.lesson_type = []
        self.summary = []
        self.data = ReadTxt().open_txt()
        self.get_delivery()
        self.get_keywords()
        self.get_title_and_lesson_type()
        self.get_summary()

    def get_delivery(self):
        d = re.search("(\d{2}.\d{2}.\d{4})", self.data)
        d_time = dt.datetime.strptime(d.group(1), "%d.%m.%Y")
        if 6 >= d_time.month > 2:
            self.deliveryTime.append(
                str(d_time.year)+"-"+str(d_time.year+1)+" BAHAR")
        else:
            self.deliveryTime.append(
                str(d_time.year)+"-"+str(d_time.year+1)+" GÜZ")
        # print(self.deliveryTime)

    def get_keywords(self):
        k = re.search('(Anahtar kelimeler:.*\n*.+)', self.data)
        x = k.group(1).replace("\n", "")[19:].strip()
        self.keyword.append(x)
        # print(self.keyword)

    def get_title_and_lesson_type(self):
        t = re.search(
            "(BÖLÜMÜ\n*)(.*\n*)(.*\n*)(.*\n*)(.*)(.*\n*)(.*\n*)(.*\n*)(.*\n*)(.*)", self.data)
        self.lesson_type.append(t.group(2).strip())
        self.project_name.append(t.group(3).strip())
        # print(t.group(10))
        # print(self.project_name)
        # print(self.lesson_type)

    def get_summary(self):
        a = re.search("(ÖZET\s*.*[A-Z].*)((?<=)[\S\s]*(?=Anahtar))", self.data)
        self.summary.append(a.group().replace(
            "ÖZET", "").replace("\n", "").strip())
        # print(self.summary)


class ReadTxt():

    def open_txt(self):
        f = open("Tez-4.txt", 'r')
        data = f.read()
        f.close()
        return data


if __name__ == '__main__':
    a = Author()
    advisor = Advisor()
    j = Jury()
    p = Project()


    print(f"Öğrenci No:{a.id}")
    print(f"Öğrenci Adı:{a.student_name}")
    print(f"Öğrenim Türü:{a.e_type}")
    print(f"Danışaman Adı :{advisor.advisor_name}")
    print(f"Danışaman Ünvanı :{advisor.advisor_degree}")
    print(f"Juri Adı:{j.jury_name}")
    print(f"Jüri Ünvanı:{j.jury_degree}")
    print(f"Proje Adı:{p.project_name}")
    print(f"Proje Teslim EDildiği Dönem:{p.deliveryTime}")
    print(f"Anahtar Kelimeler:{p.keyword}")
    print(f"Ders Türü:{p.lesson_type}")
    print(f"Proje Özeti : {p.summary}")


