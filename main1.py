from flask import Flask, render_template
import pandas as pd
import urllib.request
import bs4 as bs

app = Flask(__name__)

@app.route("/")
def new_csv():
    sauce = urllib.request.urlopen('https://www.alibaba.com/trade/search?spm=a27aq.cp_44.4746171840.1.374d3ccfjdtOJd&CatId=7&SearchText=Computer+Hardware+%26+Software&language=en&indexArea=product_en')
    soup = bs.BeautifulSoup(sauce, 'html.parser')

    long_list = list()

    for names, prices in zip(
                   soup.find_all('p', attrs={'class': 'elements-title-normal__content large'}),
                   soup.find_all('span', attrs={'class': 'elements-offer-price-normal__price'})
    ):
        long_list.append({'name': names.text, 'price': prices.text})

    # print(long_list)

    df = pd.DataFrame(long_list)
    #df.to_csv('output_file.csv', index=False)

    new_table = df.to_html()
    return new_table

if __name__ == "__main__":
    app.run(debug=True)
