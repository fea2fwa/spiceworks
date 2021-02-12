import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS

def wordcloudcreation(file="dellhw-spiceworks.txt"):
    with open(file, encoding='utf-8') as f:
        text = f.read()
        print(text)
        stopwords = set(STOPWORDS)
        stopwords.add("Dell")
        stopwords.add("will")
        stopwords.add("use")

        wc = WordCloud(max_words=1000, stopwords=stopwords, margin=10,
                    random_state=1).generate(text)
        
        default_colors = wc.to_array()
        plt.title("Default colors")
        plt.imshow(default_colors, interpolation="bilinear")
        plt.axis("off")
        plt.show()
