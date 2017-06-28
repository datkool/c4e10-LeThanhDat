from flask import *
import mlab
import os
from werkzeug.utils import secure_filename
from mongoengine import *
app = Flask(__name__)

mlab.connect()

app.config["IMG_PATH"] = os.path.join(app.root_path, "images")

class PVC(Document):
    image = StringField()
    title = StringField()
    price = FloatField()

# pvc1 = PVC(image="http://cuuam.gosu.vn/home/static/uploads/phong-vat-chi/vu-khi/cack-phongvatchi.png",
#            title="Đồ Long Đao",
#            price=2000000)
#
# pvc2 = PVC(image="http://cuuam.gosu.vn/home/static/uploads/phong-vat-chi/vu-khi/cack-phongvatchi-038.png",
#            title="Phá Thiên Đao",
#            price=2000000)
#
# pvc3 = PVC(image="http://cuuam.gosu.vn/home/static/uploads/phong-vat-chi/vu-khi/cack-phongvatchi-102.png",
#            title="Mặc Tử Kiếm",
#            price=1000000)
#
# pvc4 = PVC(image="http://cuuam.gosu.vn/home/static/uploads/phong-vat-chi/vu-khi/cack-phongvatchi-012.png",
#            title="Chân Võ Kiếm",
#            price=1000000)
# pvc5 = PVC(image="http://cuuam.gosu.vn/home/static/uploads/phong-vat-chi/vu-khi/cack-phongvatchi-004.png",
#            title="Kim Xà Kiếm",
#            price=1500000)
#
# pvc6 = PVC(image="http://cuuam.gosu.vn/home/static/uploads/phong-vat-chi/vu-khi/cack-pvc-244.jpg",
#            title="Trầm Hương Song Đao",
#            price=850000)
#
# pvc7 = PVC(image="http://cuuam.gosu.vn/home/static/uploads/phong-vat-chi/vu-khi/cack-phongvatchi-032.png",
#            title="Hỏa Long Bổng",
#            price=950000)
#
# pvc8 = PVC(image="htp://cuuam.gosu.vn/home/static/uploads/phong-vat-chi/vu-khi/cack1425.jpg",
#            title="Cửu Cung Song Kiếm",
#            price=1350000)
#
# pvc9 = PVC(image="http://cuuam.gosu.vn/home/static/uploads/phong-vat-chi/vu-khi/cack-phongvatchi-065.png",
#            title="Dao Thiến",
#            price=500000000)
#
# pvc1.save()
# pvc2.save()
# pvc3.save()
# pvc4.save()
# pvc5.save()
# pvc6.save()
# pvc7.save()
# pvc8.save()
# pvc9.save()

@app.route('/')
def index():
    return render_template("index.html", pvcs=PVC.objects())

@app.route("/images/<image_name>")
def image(image_name):
    return send_from_directory(app.config["IMG_PATH"], image_name)

@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    if request.method == "GET":
        return render_template("add_item.html")

    elif request.method == "POST":
        form = request.form
        title = form["title"]
        price = form["price"]
        image = request.files["image"]

        filename = secure_filename(image.filename)

        image.save(os.path.join(app.config["IMG_PATH"], filename))

        new_item = PVC(title=title,
                       image="/images/{0}".format(filename),
                       price=price)

        new_item.save()
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()
