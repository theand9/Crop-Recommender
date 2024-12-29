from django.db import models
from django.utils import timezone


class farmerRegistration(models.Model):
    farmer_Name = models.CharField(max_length=30)
    phone_Number = models.CharField(max_length=10, unique=True)
    areaInHectare = models.CharField(max_length=3)
    aadhar_Number = models.CharField(max_length=12, primary_key=True)
    district = models.CharField(max_length=20)
    village = models.CharField(max_length=30, default="")
    date_register = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'FarmerName: {} - District: {} - DateOfRegister: {}'.format(self.farmer_Name, self.district, self.date_register)


class farmerSearch(models.Model):
    farmer_Name = models.CharField(max_length=30)
    aadhar_Number = models.CharField(max_length=12, primary_key=True)
    # village = models.CharField(max_length=30, default="")


class districtCoords(models.Model):
    District = models.CharField(max_length=50, primary_key=True)
    Latitude = models.FloatField()
    Longitude = models.FloatField()

    def __str__(self):
        return 'DistrictName: {} - Latitude: {} - Longitude: {}'.format(self.District, self.Latitude, self.Longitude)

    # ****************************** Models To Store Soil Data In The Database


class Akola(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Amravati(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Aurangabad(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Beed(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Bhandara(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Buldhana(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Chandrapur(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Dhule(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Gadchiroli(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Gondia(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Hingoli(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Jalgaon(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Jalna(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Kolhapur(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Latur(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Nagpur(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Nanded(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Nandurbar(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Nashik(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Osmanabad(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Parbhani(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Pune(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Raigad(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Ratnagiri(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Sangli(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Satara(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Sindhudurg(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Solapur(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Thane(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Wardha(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Washim(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class Yavatmal(models.Model):
    village_Name = models.CharField(max_length=50, primary_key=True)
    ph_Value = models.FloatField()
    N_Value = models.FloatField()
    P_Value = models.FloatField()
    K_Value = models.FloatField()
    OC_Value = models.FloatField()
    Fe_Value = models.FloatField()

    def __str__(self):
        return 'VillageName: {} - pH: {} - N: {} - P: {} - K: {} - OC: {}- Fe: {}'.format(self.village_Name, self.ph_Value, self.N_Value, self.P_Value, self.K_Value, self.OC_Value, self.Fe_Value)


class seasonEncode(models.Model):
    seasonName = models.CharField(max_length=20, primary_key=True)
    kharif = models.IntegerField()
    rabi = models.IntegerField()
    wholeYear = models.IntegerField()

    def __str__(self):
        return self.seasonName


class rainfall2k19(models.Model):
    district = models.CharField(max_length=30, primary_key=True)
    rainfall = models.FloatField()

    def __str__(self):
        return self.district


class Crop_List(models.Model):
    crop = models.CharField(max_length=30, primary_key=True)
    crop_Arhar = models.IntegerField()
    crop_Bajra = models.IntegerField()
    crop_Cotton = models.IntegerField()
    crop_Gram = models.IntegerField()
    crop_Groundnut = models.IntegerField()
    crop_Jowar = models.IntegerField()
    crop_Maize = models.IntegerField()
    crop_Moong = models.IntegerField()
    crop_Mustard = models.IntegerField()
    crop_Nigerseed = models.IntegerField()
    crop_Ragi = models.IntegerField()
    crop_Rice = models.IntegerField()
    crop_Safflower = models.IntegerField()
    crop_Sesamum = models.IntegerField()
    crop_Soyabean = models.IntegerField()
    crop_Sugarcane = models.IntegerField()
    crop_Sunflower = models.IntegerField()
    crop_Urad = models.IntegerField()
    crop_Wheat = models.IntegerField()
    time_to_Grow = models.IntegerField()
    season = models.CharField(max_length=20)

    def __str__(self):
        return self.crop
        # return 'CropName: {} - Arhar: {} - Bajra: {} - Cotton: {} - Gram: {} - Groundnut: {}- Jowar: {}- Maize: {}- Moong: {}- Mustard: {}- Nigerseed: {}- Ragi: {}- Rice: {}- Safflower: {}- Sesamum: {}- Soyabean: {}- Sugarcane: {}- Sunflower: {}- Urad: {}- Wheat: {}- TimeToGrow: {}- Season: {}'.format(self.crop, self.crop_Arhar, self.crop_Bajra, self.crop_Cotton, self.crop_Gram, self.crop_Groundnut, self.crop_Jowar, self.crop_Maize, self.crop_Moong, self.crop_Mustard, self.crop_Nigerseed, self.crop_Ragi, self.crop_Rice, self.crop_Safflower, self.crop_Sesamum, self.crop_Soyabean, self.crop_Sugarcane, self.crop_Urad, self.crop_Wheat, self.time_to_Grow, self.season)
