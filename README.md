# `krüger-gauge-circular-chart`

`krüger-gauge-circular-chart` is an addition to the `gauge-circular-chart`. The added feature is another data dimension the chart, by adjusting the bar width of each bar seperately. 

## Example

The data passed is from the Netherlands with the first element the age at which the animals are slaughtered, the second element the amount of animals slaughtered the main difference between a `krüger-gauge-circular-chart` and a bar chart with variable bar width is the functionality of display. a bar chart displays the whole amount as an area (A = length * width), which makes sense when the two variables are compatible to multiply (e.g. per Capita CO2 emissions and number of people). However, as seen in the hypothetical data above, this chart type is not compatible, as the interesting fact is not the whole amount of years lived by the animals, but the comparison of amount of animals slaughtered and their age.

```python
from kgc_chart import krueger_gauge_circular_chart as kgc_chart

data_cows = {"Dairy Cow": (5.5, 966545+1571393), "Calves": (0.8, 1046503+167391), "Bulls":(1.5, 859264+12907)}

full_life_cow = 20

cow_chart = krueger_gauge_circular_chart(data_cows, max_value = full_life_cow, transparent_background = False, max_width = 150)

cow_chart.draw()

cow_chart.add_labels(True, specific_labels = ["Bulls 872,171x/year", "Calves 1,213,894x/year", "Dairy Cows 2,537,938x/year"][::-1])

cow_chart.add_ending_labels(specific_labels = ["5.5 years", "0.8 years", "1.5 years", "20 years"], full_circle_label = True)

cow_chart.add_description_box("Bar Width: Amount of Animals Killed\n Bar Length: Age Of Killing\n Full Bar Length: Natural Life Expectancy", size = (660, 166), position = (50, 1650), rectangle_line_width = 10, text_spacing = 40, background_color = (0.4, 0.4, 0.4), rectangle_color = (227/255, 146/255, 80/255), font_size = 33)

cow_chart.save_and_display_image("Cow.png")
```

![image](https://user-images.githubusercontent.com/29770094/151188728-c0ec5951-6d54-4103-bbdd-761909494552.png)

--- 
est. December 2021
Christoph Krüger
