# Importing Libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image    # to import the image
import numpy as np

#image_path = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\wordcloud_images\wave.jpg'
#image_path = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\wordcloud_images\open-book-clipart.png' # not working
#image_path = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\wordcloud_images\book.jpg'
image_path = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\wordcloud_images\bottle-and-glass.jpg'

'''
# Create a list of word
text=("Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")

#text =('Hello Raja How Raja do you ramesh rameshdo hello how Python Python Python Matplotlib Matplotlib Seaborn Network')
#text =('Scatter Scatter Scatter Scatter your WordCloud')
# Create the wordcloud object
#wordcloud = WordCloud(width=480, height=480, margin=0).generate(text) # Normal code
#wordcloud = WordCloud(width=480, height=480, margin=0,background_color="white",colormap="Dark2").generate(text) # white background_color and colormap for color of words
#wordcloud = WordCloud(width=480, height=480, margin=0,background_color="white",colormap="Dark2", random_state=42, max_font_size=150 ).generate(text)
#Maximum and minimum font size
#wordcloud = WordCloud(width=480, height=480, max_font_size=70, min_font_size=20).generate(text)
#It is possible to set a maximum number of words to display on the tagcloud. Let’s assume I want to show only the 3 most frequent words:
#wordcloud = WordCloud(width=480, height=480, max_words=3).generate(text)
#remove some words that don’t interest you. Just list them as follow:
wordcloud = WordCloud(width=480, height=480, stopwords=["Python", "Matplotlib", "Chart"]).generate(text)

# Display the generated image:
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
'''
#----------------------------------------------------------------------------------------------------
# Below code is to display the wordcloud in particular shape or external image.
# You need to have the image in your current directory and give it to the wordcloud function.
# For this we need PIL library.
# Create a list of word (https://en.wikipedia.org/wiki/Data_visualization)
text=("Data visualization or data visualisation is viewed by many disciplines as a modern equivalent of visual communication. It involves the creation and study of the visual representation of data, meaning information that has been abstracted in some schematic form, including attributes or variables for the units of information A primary goal of data visualization is to communicate information clearly and efficiently via statistical graphics, plots and information graphics. Numerical data may be encoded using dots, lines, or bars, to visually communicate a quantitative message.[2] Effective visualization helps users analyze and reason about data and evidence. It makes complex data more accessible, understandable and usable. Users may have particular analytical tasks, such as making comparisons or understanding causality, and the design principle of the graphic (i.e., showing comparisons or showing causality) follows the task. Tables are generally used where users will look up a specific measurement, while charts of various types are used to show patterns or relationships in the data for one or more variables")

# Load the image
image_mask = np.array(Image.open(image_path))
#print(image_mask)
'''
def transform_format(val):
    if val == 0:
        return 255
    else:
        return val

transformed_wine_mask = np.ndarray((image_mask.shape[0], image_mask.shape[1]),np.int32)
for i in range(len(image_mask)):
    transformed_wine_mask[i]=list(map(transform_format,image_mask[i]))
'''
# Make the figure
#wordcloud = WordCloud(background_color = 'white',mask=image_mask, contour_width =3,contour_color='firebrick').generate(text)
wordcloud = WordCloud(background_color  = 'lightblue',mask=image_mask, contour_width=5,contour_color='firebrick').generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
#----------------------------------------------------------------------------------------------------

