import pandas
from ImageText import ImageText

IGSize = (1080, 1350)

with open("quotes.txt") as quotes:
    all_quotes = quotes.read()

s = pandas.read_csv("colors.txt", sep="\t")
items = s["9 45 2"].tolist()
colors = []

for item in items:
    current_nums = []
    for raw_str in item.split(" "):
        current_nums.append(int(raw_str))

    colors.append(tuple(current_nums))

print(colors)
quotes_array = all_quotes.split("\n\n")
font_name = "SFUIText-Bold.ttf"
medium_font = "SFUIText-Medium.ttf"
white_color = (255, 255, 255)
quote_coordinates = (40, IGSize[1]/2 - 150)
hest_name_coordinate = (40, IGSize[1] - 150)
sub_coordinate = (40, IGSize[1] - 120)


for (index, quote) in enumerate(quotes_array):
    img = ImageText(IGSize, background=colors[index])
    img.write_text_box(quote_coordinates, quote, font_filename=font_name, font_size=49, box_width=IGSize[0] * 0.8, color=white_color)
    img.write_text_box(hest_name_coordinate, "Hest", font_filename=font_name, font_size=30, box_width=500, color=white_color)
    img.write_text_box(sub_coordinate, "Available on the App Store", font_filename=medium_font, font_size=30, box_width=500,
                       color=white_color)
    img.save(f"../../IGContent/{index}.png")
    print(f"Image saved with filename: {index}.png")
