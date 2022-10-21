# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:54:10 2021

@author: stanb
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:59:21 2021

@author: stanb
"""
# In[1]:
## IMPORTING LIBARIES 
import matplotlib.pyplot as plt  # Used for plotting
import numpy as np  # Used for loading in data.
def lighten_color(color, amount=0.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
import pint 
u=pint.UnitRegistry()
Q=u.Quantity
# In[INPUT]:  
#1 Open up the csv-file in Excel to determine which columns to import
#2 Click "Start" twice in order to obtain thefirst figure
#3 Fill in "Best Value", and click start again to obtain difference spectrum

###NAME###
Name = "(26th of April: HOPC CYP3A4 ND)"

###SOURCE###
Source = "20220426 CO-assay HOPC_CYP3A4_MSP1D1(-his) NDs 14.csv"

##COLUMS### 
wavelength = 0
baseline = 1
buffer = 3
cyp_co = 5
cyp_co_D1 = 7
cyp_co_D2 = 9
cyp_co_D3 = 11
cyp_co_D4 = 13
cyp_co_D5 = 15
cyp_co_D6 = 17
cyp_co_D7 = 19
cyp_co_D8 = 21
cyp_co_D9 = 23
cyp_co_D10 = 25
cyp_co_D11 = 27
cyp_co_D12 = 29
cyp_co_D13 = 31
cyp_co_D14 = 33



# In[2]: 
Wavelength_All, Baseline_All, Buffer_All, CYP_CO_All, CYP_CO_D1_All, CYP_CO_D2_All, CYP_CO_D3_All, CYP_CO_D4_All,CYP_CO_D5_All, CYP_CO_D6_All, CYP_CO_D7_All, CYP_CO_D8_All, CYP_CO_D9_All, CYP_CO_D10_All, CYP_CO_D11_All, CYP_CO_D12_All, CYP_CO_D13_All, CYP_CO_D14_All, = np.genfromtxt(Source , invalid_raise=False, delimiter=',',  usecols = (wavelength, baseline, buffer, cyp_co, cyp_co_D1, cyp_co_D2, cyp_co_D3, cyp_co_D4, cyp_co_D5, cyp_co_D6, cyp_co_D7, cyp_co_D8, cyp_co_D9, cyp_co_D10, cyp_co_D11, cyp_co_D12, cyp_co_D13, cyp_co_D14),  autostrip=True,  unpack = True)
import warnings 
warnings.simplefilter("ignore",UserWarning)
# In[3]:
Wavelength = Wavelength_All[2:602]
Absorbance_Baseline = Baseline_All[2:602]
Absorbance_Buffer = Buffer_All[2:602]
Absorbance_CYP_CO =CYP_CO_All[2:602]
Absorbance_CYP_Dithioniet_min1 = CYP_CO_D1_All[2:602]
Absorbance_CYP_Dithioniet_min2 = CYP_CO_D2_All[2:602]
Absorbance_CYP_Dithioniet_min3 = CYP_CO_D3_All[2:602]
Absorbance_CYP_Dithioniet_min4 = CYP_CO_D4_All[2:602]
Absorbance_CYP_Dithioniet_min5 = CYP_CO_D5_All[2:602]
Absorbance_CYP_Dithioniet_min6 = CYP_CO_D6_All[2:602]
Absorbance_CYP_Dithioniet_min7 = CYP_CO_D7_All[2:602]
Absorbance_CYP_Dithioniet_min8 = CYP_CO_D8_All[2:602]
Absorbance_CYP_Dithioniet_min9 = CYP_CO_D9_All[2:602]
Absorbance_CYP_Dithioniet_min10 = CYP_CO_D10_All[2:602]
Absorbance_CYP_Dithioniet_min11 = CYP_CO_D11_All[2:602]
Absorbance_CYP_Dithioniet_min12 = CYP_CO_D12_All[2:602]
Absorbance_CYP_Dithioniet_min13 = CYP_CO_D13_All[2:602]
Absorbance_CYP_Dithioniet_min14 = CYP_CO_D14_All[2:602]
# In[4]:
###CREATING  PLOT
plt.plot(Wavelength, Absorbance_Baseline, color="red", ls= "--", lw=10, label = "Baseline")
plt.plot(Wavelength, Absorbance_Buffer, color="pink", ls= "--", lw=10, label = "Buffer")
plt.plot(Wavelength, Absorbance_CYP_CO, color="green", ls= "solid", lw=10, label = "CYP + CO")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min1, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min1")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min2, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min2")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min3, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min3")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min4, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min4")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min5, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min5")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min6, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min6")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min7, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min7")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min8, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min8")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min9, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min9")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min10, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min10")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min11, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min11")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min12, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min12")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min13, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min13")
plt.plot(Wavelength, Absorbance_CYP_Dithioniet_min14, color="lightblue", ls= "--", lw=10, label = "CYP + CO +Dithioniet min14")
# In[5]:
###FINDING OPTIMAL VALUE
y1450=Absorbance_CYP_Dithioniet_min1[200:410]
y2450=Absorbance_CYP_Dithioniet_min2[200:410]
y3450=Absorbance_CYP_Dithioniet_min3[200:410]
y4450=Absorbance_CYP_Dithioniet_min4[200:410]
y5450=Absorbance_CYP_Dithioniet_min5[200:410]
y6450=Absorbance_CYP_Dithioniet_min6[200:410]
y7450=Absorbance_CYP_Dithioniet_min7[200:410]
y8450=Absorbance_CYP_Dithioniet_min8[200:410]
y9450=Absorbance_CYP_Dithioniet_min9[200:410]
y10450=Absorbance_CYP_Dithioniet_min10[200:410]
y11450=Absorbance_CYP_Dithioniet_min11[200:410]
y12450=Absorbance_CYP_Dithioniet_min12[200:410]
y13450=Absorbance_CYP_Dithioniet_min13[200:410]
y14450=Absorbance_CYP_Dithioniet_min14[200:410]
y1max450 = y1450.max()
y2max450 = y2450.max()
y3max450 = y3450.max()
y4max450 = y4450.max()
y5max450 = y5450.max()
y6max450 = y6450.max()
y7max450 = y7450.max()
y8max450 = y8450.max()
y9max450 = y9450.max()
y10max450 = y10450.max()
y11max450 = y11450.max()
y12max450 = y12450.max()
y13max450 = y13450.max()
y14max450 = y14450.max()
list = [y1max450, y2max450, y3max450, y4max450, y5max450, y6max450, y7max450, y8max450, y9max450, y10max450, y11max450, y12max450, y13max450, y14max450]
Best_value = max(list) 
# In[6]:
###FORM MATRIX, AND FIND RIGHT INDEX
exists1 = Best_value in Absorbance_CYP_Dithioniet_min1
exists2 = Best_value in Absorbance_CYP_Dithioniet_min2
exists3 = Best_value in Absorbance_CYP_Dithioniet_min3
exists4 = Best_value in Absorbance_CYP_Dithioniet_min4
exists5 = Best_value in Absorbance_CYP_Dithioniet_min5
exists6 = Best_value in Absorbance_CYP_Dithioniet_min6
exists7 = Best_value in Absorbance_CYP_Dithioniet_min7
exists8 = Best_value in Absorbance_CYP_Dithioniet_min8
exists9 = Best_value in Absorbance_CYP_Dithioniet_min9
exists10 = Best_value in Absorbance_CYP_Dithioniet_min10
exists11 = Best_value in Absorbance_CYP_Dithioniet_min11
exists12 = Best_value in Absorbance_CYP_Dithioniet_min12
exists13 = Best_value in Absorbance_CYP_Dithioniet_min13
exists14 = Best_value in Absorbance_CYP_Dithioniet_min14
List_Arrays = np.append(Absorbance_CYP_Dithioniet_min1, [Absorbance_CYP_Dithioniet_min2, Absorbance_CYP_Dithioniet_min3, Absorbance_CYP_Dithioniet_min4, Absorbance_CYP_Dithioniet_min5, Absorbance_CYP_Dithioniet_min6, Absorbance_CYP_Dithioniet_min7, Absorbance_CYP_Dithioniet_min8, Absorbance_CYP_Dithioniet_min9, Absorbance_CYP_Dithioniet_min10, Absorbance_CYP_Dithioniet_min11, Absorbance_CYP_Dithioniet_min12, Absorbance_CYP_Dithioniet_min13, Absorbance_CYP_Dithioniet_min14])
Matrix_All_arrays=List_Arrays.reshape((600, 14), order='F')
List_Existence = [exists1, exists2, exists3, exists4, exists5, exists6, exists7, exists8, exists9, exists10, exists11, exists12, exists13, exists14]
List_All = np.append(List_Arrays, List_Existence)
Matrix_All = List_All.reshape(601, 14)
# In[7]:
###FINDING OPTIMAL COLUMN, AND PLOTTING RIGHT MINUTE
Best_index=np.where(Matrix_All  == True)
Best_index_column=Best_index[1]
Best_Array=Matrix_All_arrays[:,Best_index_column]
Best_column = np.resize(Best_Array, (600,))
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min1):
    Best_column_name ="CYP + CO + Dithioniet min1"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min2):
    Best_column_name ="CYP + CO + Dithioniet min2"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min3):
    Best_column_name ="CYP + CO + Dithioniet min3"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min4):
    Best_column_name ="CYP + CO + Dithioniet min4"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min5):
    Best_column_name ="CYP + CO + Dithioniet min5"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min6):
    Best_column_name ="CYP + CO + Dithioniet min6"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min7):
    Best_column_name ="CYP + CO + Dithioniet min7"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min8):
    Best_column_name ="CYP + CO + Dithioniet min8"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min9):
    Best_column_name ="CYP + CO + Dithioniet min9"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min10):
    Best_column_name ="CYP + CO + Dithioniet min10"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min11):
    Best_column_name ="CYP + CO + Dithioniet min11"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min12):
    Best_column_name ="CYP + CO + Dithioniet min12"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min13):
    Best_column_name ="CYP + CO + Dithioniet min13"
if np.array_equal(Best_column,Absorbance_CYP_Dithioniet_min14):
    Best_column_name ="CYP + CO + Dithioniet min14"
plt.plot(Wavelength, Best_column, color="navy", ls= "solid", lw=10, label = str(Best_column_name))
# In[8]: 
###START MAKING DIFFERENCE SPECTRUM
x=Wavelength
y=Best_column
z=Absorbance_CYP_CO
# In[9]:
#Opmaak 
fig = plt.gcf()
fig.set_size_inches(30,30)
plt.legend(loc='upper right', fontsize=38)
plt.grid(True, lw=3)    
plt.xlim([350, 550])
plt.ylim([-0.05, 0.25])
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.ylabel("Absorbance (A.U.)", fontsize=50)
plt.xlabel("Wavelength (nm)", fontsize=50)
plt.title("CO-assay "+ str(Name), fontsize=50)
plt.rcParams.update({'font.size': 30})
plt.savefig("CYP3A4 CO-assay " + str(Name)+".png")
plt.show()
# In[10]:
###CALCULATING MICROMOLAR CONCENTRATIONS FOR P450 AND P420
Delta_Array=np.subtract(y,z)
plt.plot(Wavelength, Delta_Array, color="blue", ls= "solid", lw=10, label = "Difference spectrum "+ str(Best_column_name))
Zero_Array=np.zeros(600)
x490=Delta_Array[310]
y490=Delta_Array[310]
x450=Wavelength[350]
y450=Delta_Array[350]
ymax450=y450 
Decimals_C_P450 = y450/0.091 
C_P450=round(Decimals_C_P450, 3)
xa420=Wavelength[370:400]
ya420=Delta_Array[370:400]
x420 = xa420[10]       
y420 = ya420[10]
Theoretical_P420 = Decimals_C_P450*-0.041
Observed_P420 = y420
Decimals_C_P420 = -(Observed_P420 - Theoretical_P420)/0.110 
C_P420=round(Decimals_C_P420, 3)
Ratio_P450 = round(100/(C_P450+C_P420)*C_P450,1)
Ratio_P420 = round(100/(C_P450+C_P420)*C_P420,1)

print(C_P450)
print(Ratio_P450)
print(C_P420)
print(Ratio_P420)
# In[11]:
def annot_max(x450,y450, ax=None):
    xmax = x450
    ymax = y450
    text= ("Wavelength={:.1f} nm, Absorbance={:.3f} A.U.").format(xmax, ymax), str(C_P450) + " µM", str(Ratio_P450) + "%"
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", color="red", fc="w", ec="k", lw=0.72)
    kw = dict(xycoords='data',textcoords="axes fraction",
              bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw, color="red", fontsize=40)
annot_max(x450,y450)

def annot_min(x420,y420, ax=None):
    xmin = x420
    ymin = y420
    text= ("Wavelength={:.1f} nm, Absorbance={:.3f} A.U.").format(xmin, ymin), str(C_P420) + " µM", str(Ratio_P420) + "%"
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", color="darkgreen", fc="w", ec="k", lw=0.72)
    kw = dict(xycoords='data',textcoords="axes fraction",
              bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmin, ymin), xytext=(0.94,0.90), **kw, color="darkgreen", fontsize=40)
annot_min(x420,y420)

#Opmaak 
fig = plt.gcf()
fig.set_size_inches(30,30)
plt.legend(loc='lower left', fontsize=40)
plt.grid(True, lw=3)  
plt.xlim([380, 500])
plt.ylim([-0.30, 0.30])
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.ylabel("Absorbance (A.U.)", fontsize=50)
plt.xlabel("Wavelength (nm)", fontsize=50)
plt.title('Difference Spectrum ' + str(Name), fontsize=50)
plt.rcParams.update({'font.size': 35})
plt.savefig('Difference Spectrum CO-Assay ' + str(Name) + '.png')
plt.show()