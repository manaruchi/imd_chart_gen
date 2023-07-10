from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta
import requests

def make_page(links, text_to_print):

    #For 925, 850, 700 and 600 hPa
    new = Image.new("RGB", (3220,2480), "blue")
    button_img = Image.new('RGBA', (300,120), "yellow")

    #Image 1
    img1 = Image.open(requests.get(links[0], stream = True).raw).convert("RGB")
    img1 = img1.resize((1600, 1200))
    img1 = img1.crop((400,200,1400,900))
    img1 = img1.resize((1500, 1100))

    #Image 2
    img2 = Image.open(requests.get(links[1], stream = True).raw).convert("RGB")
    img2 = img2.resize((1600, 1200))
    img2 = img2.crop((400,200,1400,900))
    img2 = img2.resize((1500, 1100))

    #Image3
    img3 = Image.open(requests.get(links[2], stream = True).raw).convert("RGB")
    img3 = img3.resize((1600, 1200))
    img3 = img3.crop((400,200,1400,900))
    img3 = img3.resize((1500, 1100))

    #Image 4
    img4 = Image.open(requests.get(links[3], stream = True).raw).convert("RGB")
    img4 = img4.resize((1600, 1200))
    img4 = img4.crop((400,200,1400,900))
    img4 = img4.resize((1500, 1100))

    new.paste(img1, (100,200))
    new.paste(img2, (1630,200))
    new.paste(img3, (100,1330))
    new.paste(img4, (1630,1330))
    new.paste(button_img, (1300,200))
    new.paste(button_img, (2828,200))
    new.paste(button_img, (1300,1330))
    new.paste(button_img, (2828,1330))

    new_2 = ImageDraw.Draw(new)
    new_2.text((225, 50), text_to_print, font=ImageFont.truetype("arial.ttf", size=90), fill ="yellow")
    new_2.text((1320, 220), "925hPa", font=ImageFont.truetype("arial.ttf", size=75), fill =(255, 0, 0))
    new_2.text((2848, 220), "850hPa", font=ImageFont.truetype("arial.ttf", size=75), fill =(255, 0, 0))
    new_2.text((1320, 1350), "700hPa", font=ImageFont.truetype("arial.ttf", size=75), fill =(255, 0, 0))
    new_2.text((2848, 1350), "600hPa", font=ImageFont.truetype("arial.ttf", size=75), fill =(255, 0, 0))

    return new

def generate_list_z(z, days, start_date):
    if(z == "00UTC"): start_z = 0
    elif(z == "06UTC"): start_z = 6
    elif(z == "12UTC"): start_z = 12
    elif(z == "18UTC"): start_z = 18

    z_list = []
    cap_list = []
    dates_list = []

    for d in range(days):
        z_list.append(format_text(start_z))
        z_list.append(format_text(start_z + 6))
        z_list.append(format_text(start_z + 12))
        z_list.append(format_text(start_z + 18))
        cap_list.append("00")
        cap_list.append("06")
        cap_list.append("12")
        cap_list.append("18")
        dateval = start_date + timedelta(days = d)
        datetext = "{} {} {}".format(format_text(dateval.day), mv(dateval.month), str(dateval.year)[2:])
        dates_list.append(datetext)
        dates_list.append(datetext)
        dates_list.append(datetext)
        dates_list.append(datetext)

        start_z = start_z + 24

    return z_list, cap_list, dates_list


def format_text(z):
    if(z < 10): return "0{}".format(z)
    else: return "{}".format(z)

def mv(month_val):
    if month_val == 1: return "JAN"
    elif month_val == 2: return "FEB"
    elif month_val == 3: return "MAR"
    elif month_val == 4: return "APR"
    elif month_val == 5: return "MAY"
    elif month_val == 6: return "JUN"
    elif month_val == 7: return "JUL"
    elif month_val == 8: return "AUG"
    elif month_val == 9: return "SEP"
    elif month_val == 10: return "OCT"
    elif month_val == 11: return "NOV"
    elif month_val == 12: return "DEC"

def mg(d):
    return "{} {} {}".format(format_text(d.day), mv(d.month), str(d.year)[2:])

def mgu(d):
    return "{}_{}_{}".format(format_text(d.day), mv(d.month), str(d.year)[2:])
