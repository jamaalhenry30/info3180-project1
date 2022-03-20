"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from distutils.log import debug
from app import app
from flask import render_template, request, redirect, send_from_directory, url_for, flash
from .models import UserProperty
from .forms import PropertyForm
from . import db
from werkzeug.utils import secure_filename
import os


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods = ['GET','POST'])
def create():
    form = PropertyForm()
    if request.method=="GET":
       
        return render_template('property.html',form=form)
    if request.method=="POST" and form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        numroom = form.numroom.data
        numbath = form.numbath.data
        price = form.price.data
        property_type = form.property_type.data
        location = form.location.data
        photo = form.photo.data

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


        #file.
        
        propertyfile = UserProperty(title=title,description=description,numroom=numroom,numbath=numbath,price=price,property_type=property_type,location=location,filename=filename)
        db.session.add(propertyfile)
        db.session.commit()
        flash('Property successfully uploaded!','success')
        return redirect(url_for('listprops'))  
    return render_template('property.html',form=form)
###
# The functions below should be applicable to all Flask apps.
###



@app.route('/properties')
def listprops():
    filename = get_uploaded_images()
    rootdir = "uploads/"
    return render_template('properties.html',filename=filename, propertydata = get_all_info(), rootdir=rootdir)

def get_all_info():
    propertydata = UserProperty.query.all()
    return propertydata

@app.route('/properties/<int:id>')
def propertyid(id):
    rootdir = "uploads/"
    propid = UserProperty.query.get(id)
    return render_template('propertyid.html', propid = propid, rootdir = rootdir)

def get_uploaded_images():
    rootdir = os.getcwd()
    lst = []
    for subdir, dirs, files in os.walk("app/static/uploads"):
        for file in files:
            lst.append(os.path.join(subdir,file))
    return lst

@app.route('/properties/create/<filename>')
def get_image(filename):
    rootdir = os.getcwd()
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']),filename)

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
