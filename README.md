krueger-gauge-circular-chart is an addition to the gauge-circular-chart. 
the added feature is the possibility to include another variable in the chart, by adjusting the bar width of each bar seperately.

below there is a code example. 

    
data = {"Pigs":(2,50), "Cows":(3,350), "Dogs":(5,125), "Chickens":(0.7, 20)}
k_c_g_chart = krueger_circular_gauge_chart(data)
k_c_g_chart.draw()
k_c_g_chart.add_labels()
k_c_g_chart.save_and_display_image()
print(k_c_g_chart)

        
the data passed is hypothetical data of a farm, with the first element the age at which the animals are slaugthered, the second element the amount of animals slaughtered
