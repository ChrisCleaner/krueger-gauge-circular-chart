# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:49:29 2021

@author: chris
"""

import math
import cairo
from PIL import Image
#import argparse

class krueger_circular_gauge_chart():
    
    def __init__(self, data_dict, height = 2000, width = 2000, background_color = (0.3, 0.3, 0.3), max_width = 80, max_length = 1.5 * math.pi, spacing = 20):
        #set settings
        self.height = height
        self.width = width
        self.center = (self.width/2, self.height/2)
        self.dict = data_dict
        self.rings = len(self.dict)
        self.background_color = background_color
        self.max_width = max_width
        self.spacing = spacing
        self.max_length = max_length
        self.font_size = self.max_width / 2
        
        #get a color scheme
        self.list_of_colors = [(145, 185, 141), (229, 192, 121), (210, 191, 88), (140, 190, 178), (255, 183, 10), (189, 190, 220),
                              (221, 79, 91), (16, 182, 98), (227, 146, 80), (241, 133, 123), (110, 197, 233), (235, 205, 188), (197, 239, 247), (190, 144, 212),
                              (41, 241, 195), (101, 198, 187), (255, 246, 143), (243, 156, 18), (189, 195, 199), (243, 241, 239)]
        #adjust for values between zero and one
        new_list = []
        for item in self.list_of_colors:
            r, g, b = item
            new_list.append((r/255, g/255, b/255))
        self.list_of_colors = new_list
            
        
        
        #seperate dict tuples data for easier access later
        self.length_array = []
        self.width_array = []
        self.name_list = []
        for num, (name, tuple_val) in enumerate(self.dict.items()):
            self.length_array.append(tuple_val[0])
            self.width_array.append(tuple_val[1])
            self.name_list.append(name)
        
        
        #set image
        
        #create class instances
        self.image_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height) #image surface
        self.cr = cairo.Context(self.image_surface)
        
        #draw background
        r, g, b = self.background_color
        self.cr.set_source_rgb(r,g,b)
        self.cr.rectangle(0, 0, self.width, self.height)
        self.cr.fill()
        
        
        
    def __str__(self):
        return f"This is a Krüger-Gauge-Chart with {self.rings} elements"
    
    
    
    def save_image_as_png(self, name = "krueger_gauge_chart.png"):
        self.image_surface.write_to_png(name)  # Output to PNG
        
        
        
    def save_and_display_image(self, name = "krueger_gauge_chart.png"):
        self.image_surface.write_to_png(name)  # Output to PNG
        
        with Image.open(name) as img:
            img.show()
            
            
            

    def calculate_bars(self, starting_pos = (1000, 1000), spacing = 20, radius = 200):
    
        #calculate radii
        return_radiuses = [radius]
        x, y = starting_pos
        prev_bar_width = 0
        for num, bar_width in enumerate(self.data_width_array):

           
            
            bar_width = self.max_width * bar_width #adjust relative width to max width
            return_radiuses.append(return_radiuses[-1] + bar_width/2 + prev_bar_width/2 + spacing) #bar width is drawn on both sides of radius, hence half of old and new bar width are needed for equal spacing
            prev_bar_width = bar_width
            
        return_radiuses.pop(0) #pop first element, as it is only gives the inside radius
        
        
        
        #calculate length of line
        return_angles = []
        for  length in self.data_len_array:
            return_angles.append(length*self.max_length)
            
        
            
        return return_radiuses, return_angles
        
    def add_labels(self):
        
        #write labels
        self.cr.set_font_size(self.font_size)
        for num, text_pos in enumerate(self.radiuses):
            self.cr.move_to(self.center[0] - (len(self.name_list[num]) * self.font_size), self.center[1] - text_pos + self.spacing)
            r, g, b = self.list_of_colors[num]
            self.cr.set_source_rgb(r, g, b)
            self.cr.show_text(self.name_list[num])
    
    def draw(self):
        
        #first calculate width and angle (assuming three quarters of a cirlce as full length)
        self.data_display_dict = {}
        self.data_width_array = []
        self.data_len_array = []
        
        for name, tuple_val in self.dict.items():
            self.data_display_dict[name] = (math.pi * 0.5 * tuple_val[0] / max(self.length_array), tuple_val[1] / max(self.width_array))
            self.data_width_array.append(tuple_val[1] / max(self.width_array))
            self.data_len_array.append(tuple_val[0] / max(self.length_array))
        
        
        self.radiuses, self.angles = self.calculate_bars(spacing = 20)
        
       
        for num, (radius, angle) in enumerate(zip(self.radiuses, self.angles)):
            self.draw_circle(angle = angle, radius = radius, line_width = self.data_width_array[num] * self.max_width, rgb_colors = self.list_of_colors[num])
            
        
        
    
    
    
    def draw_circle(self, radius = 200, angle = math.pi, rgb_colors = (.1, .1, .4), line_width = 50):
        x, y = self.center
        r, g, b = rgb_colors
        self.cr.arc(x, y, radius, -math.pi*.5, angle -math.pi*.5) #center posi, radius, starting and ending angle (have to add starting and ending angle together to adjust for start pos)
        self.cr.set_line_width(line_width)
        self.cr.set_source_rgb(r, g, b)
        self.cr.stroke()



    
data = {"Pigs":(2,50), "Cows":(3,350), "Dogs":(5,125), "Chickens":(0.7, 20)}
k_c_g_chart = krueger_circular_gauge_chart(data)
k_c_g_chart.draw()
k_c_g_chart.add_labels()
k_c_g_chart.save_and_display_image()
print(k_c_g_chart)

        
        
        
    