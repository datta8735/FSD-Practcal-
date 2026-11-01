from flask import Flask

app = Flask(__name__)

@app.route("/product/<int:product_id>")
def product(product_id):
    return f"Product ID: {product_id}<br>Product Name: IPhone<br>Product Price:250000"

if __name__=="__main__":
    app.run(debug=True)