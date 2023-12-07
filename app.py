import pandas as pd
import matplotlib.pyplot as plt
from flask import render_template, Flask
import base64
from io import BytesIO


app = Flask(__name__)

def generate_plot1():
    data_frame= pd.read_csv('data.csv')
    plt.plot(data_frame)
    plt.xlabel('Durata')
    plt.ylabel('Puls')
    plt.title('Graficul 1- Puls=f(Durata)')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    return image_base64

def generate_plot3():
    data_frame= pd.read_csv('data.csv', usecols=["Durata", "Puls"])
    data_frame = data_frame.tail(5)
    plt.plot(data_frame)
    plt.xlabel('Durata')
    plt.ylabel('Puls')
    plt.title('Graficul 3- Puls=f(Durata) pentru ultimele 5 valori')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    return image_base64

def generate_plot2():
    data_frame = pd.read_csv('data.csv')
    data_frame = data_frame.head(4)
    plt.plot(data_frame)
    plt.xlabel('Durata')
    plt.ylabel('Puls')
    plt.title('Graficul 2- Puls=f(Durata) pentru primele 4 valori')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    return image_base64

@app.route('/')
def index():
    plot_image= generate_plot1()
    plot_image1=generate_plot2()
    plot_image2=generate_plot3()
    return render_template("index.html", plot_image=plot_image, plot_image1=plot_image1, plot_image2=plot_image2)

if __name__ == '__main__':
    app.run(debug=True)