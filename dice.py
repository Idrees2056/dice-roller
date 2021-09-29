import random 
import plotly.figure_factory as ff

dice_result=[]

for i in range(1,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    j=dice1+dice2
    dice_result.append(j)

print(dice_result)
 
k=ff.create_distplot([dice_result]  ,["dice1+dice2plot"]  ,show_hist=True   )
k.show()