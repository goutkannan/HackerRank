class India:
    def __init__(self):
        self.capital = "New Delhi"
        self.type = "Demoratic"
        self.cities= ['Mumbai','Bangalore','Chennai']
    def get_country(self):
        return "India is "+self.type+" country, its capital city is "+self.capital


class USA:
    def __init__(self):
        self.capital = "Washington DC"
        self.type="Democratic "
        self.cities="LA,SFO,NY,Chicago,Boston,LV" 

    def get_country(self):
        return "U.S.A is "+ self.type +" its capital is "+ self.capital


def genFactory():
    countryList = {1:USA,2:India}
    for i,country in countryList.items():
        print(country().get_country())


genFactory()




