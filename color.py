import colorgram
# extract color from picture and add to a list
color_list = colorgram.extract('dot2.jpg', 2**32)
color_palette = []
for item in range(len(color_list)):
    color_palette.append(color_list[item].rgb)

print(color_palette)