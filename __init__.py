import os

from flask import Flask,request, make_response, session, render_template, url_for, redirect, render_template_string


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskproj.sqlite'),
    )
    from . import db
    db.init_app(app)
    from . import auth
    app.register_blueprint(auth.bp)
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/admin')
    def admin():
        app.logger.info(request.cookies)
        return """<form action="%s" method='post'>
            <input type="text" name="username" required>
            <input type="password" name="password" required>
            <input type="submit" value="Submit">
            </form>"""%url_for("admin2")

    @app.route("/admin2", methods=['POST'])
    def admin2():
        username = request.form.get("username")
        password = request.form.get("password")
        if username.strip():
            if username!="admin" or password!=app.secret_key:
                return "login failed"
            db = get_db()
        
            user = db.execute(
                'SELECT * FROM user WHERE username = ?', (username,)
            ).fetchone()
            session.clear()
            session['user_id'] = user['id']
            return redirect("http://127.0.0.1:5000/", code=302)
        else:
            return "login failed"

    return app
