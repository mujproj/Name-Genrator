from django.shortcuts import render
from .forms import *
import random
import pandas as pd

# Create your views here.
def index1(request):
    form = main()
    return render(request, "index.html", {'form': form})

def index2(request):
    if request.method == "POST":
        form = main(request.POST)
        if form.is_valid():
            a = request.POST["string1"]
            print(a)
            str1 = list(a)
            b = request.POST["string2"]
            print(b)
            str2 = list(b)
            print("first", str1, str2)
            df = pd.read_csv('Indian-Female-Names.csv', usecols=['name'])
            indian_females = df['name'].values.tolist()
            # print(len(females))
            indian_female_names = list(dict.fromkeys(indian_females))

            df = pd.read_csv('Indian-Male-Names.csv', usecols=['name'])
            indian_males = df['name'].values.tolist()
            indian_male_names = list(dict.fromkeys(indian_males))
            print(len(indian_male_names))

            df = pd.read_csv('American-Names.csv')
            american_female = df.loc[df['Gender'] == "F"]
            american_female = american_female['Name'].values.tolist()
            american_female_names = list(dict.fromkeys(american_female))
            print(american_female_names[0])
            # print(american_female)
            american_male = df.loc[df['Gender'] == "M"]
            american_male = american_male['Name'].values.tolist()
            american_male_names = list(dict.fromkeys(american_male))
            print(len(american_male_names))
            f = [] # list to append the names mathced from concatenated strings
            while(len(f) != 30):
                
                random.shuffle(str1)
                random.shuffle(str2)
                # print("second", str1, str2)
                p1 = random.randint(0, (len(str1)))
                p2 = random.randint(0, (len(str2)))
                s1 = random.choices(str1, k=p1)
                s2 = random.choices(str2, k=p2)
                # print("third", s1, s2)
                random.shuffle(s1)
                random.shuffle(s2)
                # print("fourth", s1, s2)
                s1.extend(s2)
                # print("fifth", s1)
                random.shuffle(s1)
                # print("sixth", s1)
                l = ""
                o = l.join(s1)
                # print(o)
                # print(o)

                if request.POST["origin"] == "Indian":
                    if request.POST["gender"] == "Female":
                        if o in indian_female_names:
                            f.append(o)

                    if request.POST["gender"] == "Male":
                        if o in indian_male_names:
                            f.append(o)

                elif request.POST["origin"] == "American":
                    # print("inside this")
                    if request.POST["gender"] == "Female":
                        # print("inside")
                        if o in american_female_names:
                            print("inside")
                            f.append(o)
                        
                        else:
                            f.append("None")
                            break
                            # print(f)
                            # break

                    if request.POST["gender"] == "Male":
                        if o in american_male_names:
                            f.append(o)

                        else:
                            f.append("None")
                            break

            f = list(dict.fromkeys(f))
            print(f)
            name = ""
            for i in range(len(f)):
                a = f[i] + "\n"
                name += a
                # print(f[i])

            # print(len(female_names))
            # if o in female_names:
            #     print(o)

    return render(request, 'index.html', {'form': form, 'name': name})