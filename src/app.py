from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [{'ID': 1, 'Title': 'Data Scientist', 'Location': 'Johannesburg, RSA', 'Salary': 'R 850 000 pa'},{'ID': 2, 'Title': 'Software Engineer', 'Location': 'New York, USA', 'Salary': '$ 120 000 pa'}, {'ID': 3, 'Title': 'Business Analyst', 'Location': 'London, UK', 'Salary': '£ 110 000 pa'},{'ID': 4, 'Title': 'Cloud Engineer', 'Location': 'Cape Town, RSA','Salary': 'R 950 000 pa'}]


@app.route("/")
def root_page():
    return render_template('root.html')

@app.route("/about")
def home_page():
    return render_template('about.html')


@app.route("/products")
def product_data():
    return render_template('products.html')


@app.route("/careers")
def careers_data():
    return render_template('careers.html', jobs=JOBS)


@app.route("/raw")
def raw_data():
    return jsonify(JOBS)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)