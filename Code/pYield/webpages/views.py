from django.views.generic import TemplateView, CreateView, View
from . import models
from django.shortcuts import render, redirect
from .forms import FarmerRegistrationForm, FarmerDetailsForm
from django.http import HttpResponse
from .utils import render_to_pdf
from django.template.loader import get_template
from django.contrib import messages
from difflib import SequenceMatcher
from webpages.scripts import callAPI
from dateutil.relativedelta import relativedelta
from dateutil import parser
from datetime import datetime


def generate_pdf(request):
    aadhar_Num = request.POST.get('aadhar', None)

    farmer_List, curr_Date, crop_List, crop_Profit, curr_Season, grow_Time, date_Diff = callAPI.run(
        aadhar_Num)

    farmer_Name = farmer_List[0]
    farmer_Phone_No = farmer_List[1]
    farmer_Area = farmer_List[2]
    farmer_Aadhar = farmer_List[3]
    farmer_Dist = farmer_List[4]
    farmer_Village = farmer_List[5]

    crop1 = crop_List[0]
    crop2 = crop_List[1]
    crop3 = crop_List[2]

    crop1_Profit = crop_Profit[0] * float(farmer_Area)  # Multiply
    crop2_Profit = crop_Profit[1] * float(farmer_Area)
    crop3_Profit = crop_Profit[2] * float(farmer_Area)

    crop1_Gtime = curr_Date + \
        relativedelta(months=+grow_Time[0]) + \
        relativedelta(days=+date_Diff)
    crop2_Gtime = curr_Date + \
        relativedelta(months=+grow_Time[1]) + \
        relativedelta(days=+date_Diff)
    crop3_Gtime = curr_Date + \
        relativedelta(months=+grow_Time[2]) + \
        relativedelta(days=+date_Diff)

    #farmers = models.farmerRegistration.objects.get(aadhar_Number=a)
    context = {
        'farmer_Name': farmer_Name,
        'farmer_Phone': farmer_Phone_No,
        'farmer_Aadhar': farmer_Aadhar,
        'farmer_Area': farmer_Area,
        'farmer_Dist': farmer_Dist,
        'farmer_Village': farmer_Village,
        'date': curr_Date,
        'crop1': crop1,
        'crop2': crop2,
        'crop3': crop3,
        'crop1_Profit': crop1_Profit,
        'crop2_Profit': crop2_Profit,
        'crop3_Profit': crop3_Profit,
        'season': curr_Season,
        'crop1_Gtime': crop1_Gtime,
        'crop2_Gtime': crop2_Gtime,
        'crop3_Gtime': crop3_Gtime,
    }
    template = get_template('report.html')
    html = template.render(context)
    pdf = render_to_pdf('report.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "RecommendationReport_%s.pdf" % ("168001210718    ")
        content = "inline; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        return response
    else:
        return HttpResponse("Data Not Found")


class AdminLoginPageView(TemplateView):
    template_name = 'admin.html'


def FarmerRegisterPage(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            reg_farmer = models.farmerRegistration(
                farmer_Name=request.POST['farmer_Name'], phone_Number=request.POST[
                    'phone_Number'], areaInHectare=request.POST['areaInHectare'],
                aadhar_Number=request.POST['aadhar_Number'],
                district=request.POST['district'],
                village=request.POST['village'])
            village = form.cleaned_data.get("village")
            district = form.cleaned_data.get("district")
            if district == 'Akola':
                village_Ret = models.Akola.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")

            elif district == 'Amravati':
                village_Ret = models.Amravati.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Aurangabad':
                village_Ret = models.Aurangabad.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Beed':
                village_Ret = models.Beed.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Bhandara':
                village_Ret = models.Bhandara.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Buldhana':
                village_Ret = models.Buldhana.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Chandrapur':
                village_Ret = models.Chandrapur.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Dhule':
                village_Ret = models.Dhule.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Gadchiroli':
                village_Ret = models.Gadchiroli.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Gondia':
                village_Ret = models.Gondia.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Hingoli':
                village_Ret = models.Hingoli.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Jalgaon':
                village_Ret = models.Jalgaon.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Jalna':
                village_Ret = models.Jalna.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Kolhapur':
                village_Ret = models.Kolhapur.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Latur':
                village_Ret = models.Latur.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Nagpur':
                village_Ret = models.Nagpur.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Nanded':
                village_Ret = models.Nanded.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Nandurbar':
                village_Ret = models.Nandurbar.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Nashik':
                village_Ret = models.Nashik.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Osmanabad':
                village_Ret = models.Osmanabad.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Parbhani':
                village_Ret = models.Parbhani.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Pune':
                village_Ret = models.Pune.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Raigad':
                village_Ret = models.Raigad.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Ratnagiri':
                village_Ret = models.Ratnagiri.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Sangli':
                village_Ret = models.Sangli.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Satara':
                village_Ret = models.Satara.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Sindhudurg':
                village_Ret = models.Sindhudurg.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Solapur':
                village_Ret = models.Solapur.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Thane':
                village_Ret = models.Thane.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Wardha':
                village_Ret = models.Wardha.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Washim':
                village_Ret = models.Washim.objects.values_list('village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            elif district == 'Yavatmal':
                village_Ret = models.Yavatmal.objects.values_list(
                    'village_Name')
                village_List = [village_Ret[i][0]
                                for i in range(0, len(village_Ret))]

                if village.upper() in village_List:
                    reg_farmer.save()

                else:
                    list1 = [i for i in village_List if SequenceMatcher(
                        None, village.upper(), i).ratio() >= 0.75]

                    messages.error(
                        request, f"This Village does not exist.\n Did you mean {list1}")
            else:
                form = FarmerRegistrationForm()

            return redirect('farmerRegister')
    else:
        form = FarmerRegistrationForm()

    context = {'form': form}
    return render(request, 'farmerReg_form.html', context)


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ConnectPageView(TemplateView):
    template_name = 'connect.html'


def FarmerDetailPageView(request):
    if request.method == 'POST':
        form = FarmerDetailsForm(request.POST)
        if form.is_valid():
            farmer = models.farmerSearch(
                farmer_Name=request.POST['farmer_Name'],
                aadhar_Number=request.POST['aadhar_Number'],
            )
            aadhar_Number = form.cleaned_data.get("aadhar_Number")
            registered_farmers = models.farmerRegistration.objects.get(
                aadhar_Number=aadhar_Number)
            context = {'registered_farmers': registered_farmers}
            farmers_data = models.farmerRegistration.objects.all()
            return render(request, 'farmerdetail.html', context)
