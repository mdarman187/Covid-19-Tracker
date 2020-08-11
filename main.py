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
       for x in range(len(country_names)):
             plt.bar(country_name[x], confirmed[x], color = 'green')
             if recovered[x] > active[x]:
                plt.bar(country_name[x], recovered[x], color = 'red')
                plt.bar(country_name[x], active[x], color = 'blue')
             else:
                plt.bar(country_name[x], active[x], color = 'blue')
                plt.bar(country_name[x], recovered[x], color = 'red')
             plt.bar(country_name[x], deaths[x], color = 'black')
             plt.title('Current Covid Cases')
             plt.xlabel('Country name')
             plt.ylabel('Cases(in millions)')
             plt.show()
     except Exception as e:
        print("Enter correct name")
        
Label(root, text = "Enter countries names to\nto get COVID-19 details\n").pack()
Label(root, text = "Enter country name:").pack()
data = StringVar()
data.set("Separate country names using Space")
entry = Entry(root, textvariable = data, width = 50).pack()
Button(root, text = "Provide Data", command = showData).pack()
root.mainloop()
        
    
