#BMI Calculator

#Using the BMI calculator used from the NHS website found at:
#https://www.nhs.uk/health-assessment-tools/calculate-your-body-mass-index/calculate-bmi-for-adults

import matplotlib.pyplot as plt
import numpy as np

#Allows users to input their name, weight and height to calculate their bmi
#name = str(input('What is your name?\n'))

#weight = float(input('Please enter your weight in kilograms:\n'))

#height = float(input('Enter your height in meters:\n'))
name = "b"
height = 1.5
weight = 216

BMI = weight/(height * height)
#Converts the BMI result to a string type.
txtBMI = str(round(BMI, 1))

#If statement to categorise BMI into the 4 catergories - Underweight, Healthy Weight, Overweigh and Obese
#Saves the concatenated strings into the variable 'result' 
if BMI <= 18.4: result = name + ", your BMI is " + txtBMI + ". A BMI of 18.4 and below is classed as underweight."
elif 18.5 <= BMI <= 22.9: result = name + ", your BMI is " + txtBMI + ". A BMI of 18.5 to 22.9 is classed as a healthy weight."
elif 23 <= BMI <= 27.4: result = name + ", your BMI is "+ txtBMI + ". A BMI of 23 to 27.4 is classed as overweight."
else: result = name + ", your BMI is "+ txtBMI + ". A BMI of 27.5 and above is classed as obese."

#A list of the colors: darkred, darkorange, darkgreen, and blueviolet found at:
#https://www.w3schools.com/colors/color_tryit.asp?color=Purple
colors = ["#880000", "#ff8c00","#006400",'#8a2be2'   ]

#A list of the BMI category boundaries
# =<18.5 is underweight
# 18.5-23 is a healthy weight
# 23-27.6 is overweiight
# >27.5 is obese
values = [50,27.5,23,18.5,0]

#X axis values for the gauge chart
x_axis_vals = [0, 0.73, 1.46, 2.19]


fig = plt.figure(figsize=(10,10))

ax = fig.add_subplot(projection="polar");

ax.bar(x_axis_vals, width=1, height=0.5, bottom=2,
       color=colors, align="edge");

plt.annotate("Underweight", xy=(2.8,2.28), rotation=60, color="white", fontweight="bold");
plt.annotate("Healthy Weight", xy=(2.02,2.25), rotation=15, color="white", fontweight="bold");
plt.annotate("Overweight", xy=(1.18,1.98), rotation=-25, color="white", fontweight="bold");
plt.annotate("Obese", xy=(0.32,2.08), rotation=-70, color="white", fontweight="bold");

for loc, val in zip([0, 0.73, 1.46, 2.19], values):
    plt.annotate(val, xy=(loc, 2.5), ha="right" if val<=18.5 else "left");


if BMI<=50: y_value = (BMI/50)*x_axis_vals[2] 
else: y_value = 0


#add a arrow pointing to the BMI alue on thechart
plt.annotate(round(BMI,1), xytext=(0,0), xy=(y_value, 2.0),
             arrowprops=dict(arrowstyle="wedge, tail_width=0.5", color="black", shrinkA=0),
             bbox=dict(boxstyle="circle", facecolor="black", linewidth=1.0 ),
             fontsize=18, color="white", ha="center"
            )

plt.suptitle("BMI", fontsize = 20, fontweight = "bold")
plt.title(result, loc="center", pad = 5, fontsize=14, fontweight="bold")

#hide the axis
ax.set_axis_off()

plt.show()






