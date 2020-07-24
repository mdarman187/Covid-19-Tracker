from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Get Covid-19 Details Country Wise - Md Arman")

def showData():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid
    covid = Covid()
    cases = []
    confirmed = []
    active = []
    death = []
    recovered = []
    try:
       root.update()
       countries = data.get()
       country_names = countries.strip()
       country_names = countries.replace(" "," ")
       country_names = country_names.strip(",")
       for x in country_names:
             cases.append(covid.get_status_by_country_name(x))
             root.update()
       for y in cases:
             confirmed.append(y["confirmed"])
             active.append(y["active"])
             deaths.append(y["deaths"])
             recovered.append(y["recovered"])
       confirmed_patch = mpatches.Patch(color = 'green', label = 'confirmed')
       recovered_patch = mpatches.Patch(color = 'red', label = 'recovered')
       active_patch = mpatches.Patch(color = 'blue', label = 'active')
       deaths_patch = mpatches.Patch(color = 'black', label = 'deaths')
       plt.legend(handles=[confirmed_patch,recovered_patch,active_patch,deaths_patch])
       
       
             
    
