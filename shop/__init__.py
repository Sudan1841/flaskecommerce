from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from flask_msearch import Search
from flask_login import LoginManager
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # replace with your URI
app.config['SECRET_KEY'] = 'hfouewhfoiwefoquw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)

# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
#patch_request_class(app)

migrate = Migrate(app, db)
with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'customerLogin'
login_manager.needs_refresh_message_category = 'danger'
login_manager.login_message = u"Please login first"

# Import routes and register blueprints
from shop.products import routes as product_routes
from shop.admin import routes as admin_routes
from shop.carts import carts
from shop.customers import routes as customer_routes

app.register_blueprint(product_routes)
app.register_blueprint(admin_routes)
app.register_blueprint(carts)
app.register_blueprint(customer_routes)

if __name__ == "__main__":
    app.run(debug=True)


# #from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_bcrypt import Bcrypt
# # from flask_msearch import Search
# # from flask_login import LoginManager
# # from flask_migrate import Migrate
# # import os

# # basedir = os.path.abspath(os.path.dirname(__file__))

# # # Initialize Flask app
# # app = Flask(__name__)
# # app.config['SECRET_KEY'] = 'hfouewhfoiwefoquw'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'

# # # Initialize extensions
# # db = SQLAlchemy(app)  # Initialize SQLAlchemy with the Flask app
# # bcrypt = Bcrypt(app)
# # search = Search()
# # search.init_app(app)
# # migrate = Migrate(app, db)  # Initialize Flask-Migrate with the Flask app
# # login_manager = LoginManager()
# # login_manager.init_app(app)
# # login_manager.login_view = 'customerLogin'
# # login_manager.needs_refresh_message_category = 'danger'
# # login_manager.login_message = u"Please login first"

# # # Import routes and register blueprints
# # from shop.products import routes as product_routes
# # from shop.admin import routes as admin_routes
# # from shop.customers import routes as customer_routes
# # app.register_blueprint(product_routes)
# # app.register_blueprint(admin_routes)
# # app.register_blueprint(customer_routes)

# # # Run the app if executed directly
# # if __name__ == "__main__":
#  #   app.run(debug=True)

# # from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_bcrypt import Bcrypt
# # import os
# # from flask_msearch import Search
# # from flask_login import LoginManager
# # from flask_migrate import Migrate

# # basedir = os.path.abspath(os.path.dirname(__file__))

# # app = Flask(__name__)
# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# # app.config['SECRET_KEY'] = 'hfouewhfoiwefoquw'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')


# # from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_msearch import Search

# # db = SQLAlchemy()
# # search = Search()

# # def create_app():
# #     app = Flask(__name__)
# #     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # replace with your URI
# #     db.init_app(app)
# #     search.init_app(app)
# #     return app
# # # myapplication/myapplication/__init__.py

# # # from flask import Flask
# # # from flask_sqlalchemy import SQLAlchemy

# # # db = SQLAlchemy()

# # # def create_app():
# # #     app = Flask(__name__)
# # #     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # replace with your URI
# # #     db.init_app(app)
# # #     return app


# # # # Configure SQLAlchemy
# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, but recommended
# # # db = SQLAlchemy(app)


# # bcrypt = Bcrypt(app)
# # search = Search()
# # search.init_app(app)

# # migrate = Migrate(app, db)
# # with app.app_context():
# #     if db.engine.url.drivername == "sqlite":
# #         migrate.init_app(app, db, render_as_batch=True)
# #     else:
# #         migrate.init_app(app, db)

# # login_manager = LoginManager()
# # login_manager.init_app(app)
# # login_manager.login_view = 'customerLogin'
# # login_manager.needs_refresh_message_category = 'danger'
# # login_manager.login_message = u"Please login first"

# # from shop.products import routes
# # from shop.admin import routes
# # from shop.carts import carts
# # from shop.customers import routes

# # if __name__ == "__main__":
# #     app.run(debug=True)

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
# import os

# from flask_msearch import Search
# from flask_login import LoginManager
# from flask_migrate import Migrate

# basedir = os.path.abspath(os.path.dirname(__file__))


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # replace with your URI
# db = SQLAlchemy(app)
# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SECRET_KEY']='hfouewhfoiwefoquw'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app)


# from flask_msearch import MSearch

# msearch = MSearch()


# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
# search = Search()
# search.init_app(app)

# migrate = Migrate(app, db)
# with app.app_context():
#     if db.engine.url.drivername == "sqlite":
#         migrate.init_app(app, db, render_as_batch=True)
#     else:
#         migrate.init_app(app, db)


# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view='customerLogin'
# login_manager.needs_refresh_message_category='danger'
# login_manager.login_message = u"Please login first"


# from shop.products import routes
# from shop.admin import routes
# from shop.carts import carts
# from shop.customers import routes


# from shop import app
# if __name__ =="__main__":
#     app.run(debug=True)
