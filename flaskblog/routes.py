import secrets
import os
import requests
import qrcode
import json
import math
from flask import request, jsonify
from flask import Flask, render_template, url_for, flash, redirect
from flaskblog.models import User
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


posts =[ {
			'author': 'SOMESH SARKAR',
			'title': 'Blog 	Post 1',
			'content': 'First Blog Post',
			'date_posted': 'April 20, 2018'
		}, 
		{
			'author': 'SAMIR SAHA',
			'title': 'Blog 	Post 2',
			'content': 'Second Blog Post',
			'date_posted': 'April 21, 2018'
		}

	]



books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'}
]

location = []
latitude= []
longitude = []
lat1=[]
lang1=[]

URL = "https://geocode.search.hereapi.com/v1/geocode"
api_key = 'S3TCHS5oiquFZXVeAbTdJkAYuqxYjddr_RW2lusbWu8' # Acquire from developer.here.com
PARAMS = {'apikey':api_key,'q':location} 

def loc():
	location = [current_user.pincode]
	for x in location:
		PARAMS = {'apikey':api_key,'q':x}
		r = requests.get(url = URL, params = PARAMS) 
		data = r.json()

		if (data['items']!=[]): 
			lat1.append(data['items'][0]['position']['lat'])
			lang1.append(data['items'][0]['position']['lng'])

	


latitude = [22.53793, 22.56063, 52.05991, 22.55989, 22.61576, 22.6145, 53.3306, 22.4859, 22.53825, 22.58029, 20.4298, 22.59344, 51.42669, 22.54436, 22.5689, 22.57849, 22.59145, 22.56063, 22.61285, -37.83291, 22.54271, 22.61576, 22.61252, 22.53797, 22.5417, 22.61252, 22.5219, 22.57969, 51.61958, 7.86804, 22.50836, 22.53496, 22.58204, 22.54615, 22.48256, 22.56063, 22.53184, 22.58069, 22.54615, 29.99209, 22.58191, 22.59323, 22.61865, 22.59816, 22.4558, 22.61665, 22.56059, 22.61576, 22.58193, 22.51562, 22.55249, 22.60819, 22.61344, 22.51079, 22.56973, 22.52393, 22.61576, 22.57315, 22.55008, 22.57623, 22.6215, 22.58886, 45.60332, 23.24591, 22.56453, 52.99123, 22.52463, 22.58558, 22.52487, 26.7127, 22.52581, 22.53955, 22.58495, 22.57814, 22.53955, 22.53792, 22.61252, 22.57658, 22.55211, 22.59052, 22.55025, 22.53198, 22.56063, 22.54292, 22.57553, 22.57371, 22.53376, 22.46688, 22.5499, 22.57472, 22.55028, 22.58663, 22.51658, 22.58962, 22.51027, 22.52899, 22.58928, 22.57191, 52.27094, 20.4298, 22.60454, 22.60461, 22.60461, 22.5917, 26.7127, 22.60446, 22.60427, 22.60427, 22.53532, 22.5417, 22.59705, 22.57346, 22.55577, 22.53748, 22.54127, 22.53516, 22.55465, 22.57978, 22.58212, 22.60292, 22.55581, 22.47693, 22.60871, 22.5233, 22.55129, 22.59554, 22.59497, 22.56824, 22.54917, 22.47783, 31.6568, 28.79805, 13.09952, 22.60384, 22.59074, 22.53655, 22.51864, 22.52757, 22.60292, 22.54131, 22.51291, 22.58235, 22.57782, 22.82793, 22.5739, 22.5397, 20.4298, 22.59235, 22.60293, 29.30547, 22.59162, 22.59712, 22.58937, 22.54282, 22.56013, 22.51534, 22.47924, 22.56541, 22.58945, 22.48106, 11.05035, 22.64492, 22.65747, 22.56195, 22.58307, 22.55183, 22.56792, 22.53588, 22.61402, 22.44645, 22.5572, 22.59242, 22.47868, 22.58166, 26.70725, 22.52197, 22.53788, 22.5791, 22.55922, 50.76755, 22.73104, 22.56819, 22.54742, 22.55648, 22.47607, 22.50474, 40.60135, 22.55508, 22.49122, 22.5551, 22.52664, 22.59142, 22.56829, 22.5925, 22.5894, 22.52121, 22.59237, 22.56782, 22.64186, 22.5416, 22.4753, 22.54845, 22.56819, 9.94594, 22.59599, 41.09363, 22.59333, 22.54619, 22.52722, 22.60184, 22.62077, 22.55193, 22.57102, 30.32568, 22.57842, 22.60485, 21.11648, 22.56925, 22.5687, 22.51677, 22.53213, 22.57053, 22.57053, 23.22609, 22.58702, 22.56891, 22.42097, 22.58404, 22.53256, 22.5789, 22.5796, 22.48032, 22.57053, -24.62677, 22.56835, 22.52273, 22.5464, 25.34058, 22.50969, 22.5947, 22.48345, 22.60711, 22.57861, 22.83632, 22.5693, 22.57297, 22.52031, 23.60107, 22.58599, 22.53476, 22.53476, 40.9213, 29.20167, 22.54407, 22.5766, 22.59092, 22.56088, 22.58846, 22.5418, 22.60197, 22.51768, 22.5113, 22.58563, 22.8597, 22.54971, 22.5291, 22.46843, 22.50298, 29.76455, 22.58694, 22.57839, 22.57956, 22.60635, 22.58117, 22.594, 22.53864, 22.56794, 18.95259, 22.53793, 22.55371, 22.5806, 22.55107, 22.60179, 26.84524, 22.5789, 22.58685, 22.46843, 22.59626, 22.5698, 22.53662, 19.0015, 22.59539, 22.58432, 22.59567, 22.47713, 22.56639, 22.55521, 22.54314, 22.57764, 22.59172, 22.59176, 22.59232, 22.56626, 22.65984, 40.83682, 22.51008, 22.58956, 22.54828, 22.52699, 28.62218, 22.55231, 22.49304, 22.53857, 22.57814, 43.93873, 22.60489, 22.52302, 22.53662, 22.60252, 26.7127, 22.57342, 22.57839, 13.03704, 22.58848, 22.57819, 22.56719, 22.59137, 22.59148, 22.58904, 22.57973, 22.61451, 11.38853, 22.5182, 22.50138, 22.48196, 22.48345, 22.60229, 22.5733, 22.53742, 22.56639, 22.51249, 22.56738, 22.75422, 22.5655, 22.57876, 22.61885, 22.60149, 22.59553, 22.59553, 22.55861, 22.59268, 33.56253, 22.61574, 22.61844, 22.60149, 22.59497, 22.48982, 22.57264, 22.57334, 22.60973, 22.55869, 22.55925, 22.52993, 22.5379, 22.53532, 22.57476, 22.53677, 22.55736, 22.59652, 22.60639, 21.20195, 22.58881, 22.58551, 22.64818, 22.54219, 22.5425, 22.55229, 53.72144, 22.57592]  
longitude = [88.37123, 88.38724, -9.50903, 88.39127, 88.3874, 88.39031, -6.2368, 88.29082, 88.36263, 88.39243, 85.85239, 88.35917, 0.09901, 88.38545, 88.3628, 88.36162, 88.35733, 88.38724, 88.37806, 144.97043, 88.36209, 88.3874, 88.38062, 88.36069, 88.34853, 88.38062, 88.34655, 88.36079, -0.11133, 98.3566, 88.36221, 88.37714, 88.36488, 88.36783, 88.37608, 88.38724, 88.32234, 88.36408, 88.36783, 31.2782, 88.35102, 88.3557, 88.37865, 88.37919, 88.38305, 88.37889, 88.38788, 88.3874, 88.37683, 88.33878, 88.37314, 88.38211, 88.39018, 88.34657, 88.36866, 88.33613, 88.3874, 88.38558, 88.35969, 88.3932, 88.37817, 88.38464, -0.98331, 87.83965, 88.39276, -6.98612, 88.3539, 88.37987, 88.35655, 88.45757, 88.36344, 88.32364, 88.37654, 88.38065, 88.32364, 88.3595, 88.38062, 88.37892, 88.37279, 88.35455, 88.27768, 88.35041, 88.38724, 88.36301, 88.35906, 88.35769, 88.38687, 88.30761, 88.37124, 88.38046, 88.37171, 88.35721, 88.38714, 88.36515, 88.39985, 88.36801, 88.3582, 88.36306, -113.83513, 85.85239, 88.38285, 88.38276, 88.38276, 88.36838, 88.45757, 88.38256, 88.39242, 88.39242, 88.37089, 88.34853, 88.37026, 88.31121, 88.36193, 88.36114, 88.26959, 88.25155, 88.36048, 88.37, 88.37064, 88.36971, 88.37271, 88.34975, 88.3848, 88.3669, 88.36631, 88.3453, 88.36868, 88.36497, 88.28971, 88.39541, 74.7995, 77.14425, 80.21761, 88.36908, 88.35663, 88.35777, 88.36843, 88.3695, 88.36971, 88.28686, 88.37262, 88.3548, 88.32825, 88.40211, 88.36207, 88.36209, 85.85239, 88.32796, 88.37451, 76.32221, 88.36914, 88.33769, 88.36891, 88.31974, 88.35847, 88.32624, 88.31216, 88.36495, 88.35438, 88.28082, 77.02048, 88.3347, 88.40448, 88.37245, 88.37891, 88.36783, 88.30348, 88.37022, 88.38018, 88.28725, 88.37345, 88.3667, 88.23667, 88.33087, 88.3692, 88.4158, 88.36411, 88.36495, 88.37671, 0.28433, 88.31402, 88.32726, 88.36518, 88.38857, 88.30993, 88.30841, -80.33383, 88.37173, 88.26119, 88.37098, 88.35905, 88.37756, 88.36748, 88.36497, 88.40745, 88.36874, 88.36188, 88.35933, 88.3433, 88.28302, 88.40511, 88.28766, 88.32726, 76.33529, 88.37361, -73.92167, 88.36076, 88.32837, 88.35455, 88.36727, 88.35325, 88.38262, 88.36234, 78.01745, 88.32492, 88.34246, 79.05014, 88.35934, 88.36129, 88.37738, 88.31857, 88.37124, 88.37124, 90.65988, 88.37592, 88.35838, 88.41207, 88.35359, 88.34355, 88.33119, 88.36697, 88.39517, 88.37124, 25.91083, 88.35882, 88.37104, 88.36652, 88.72128, 88.32543, 88.36293, 88.28932, 88.33922, 88.32605, 88.36476, 88.36376, 88.34668, 88.34538, 88.22971, 88.37842, 88.27094, 88.27094, -82.93637, 78.95872, 88.36647, 88.37863, 88.3689, 88.31643, 88.37865, 88.36686, 88.34875, 88.36281, 88.34784, 88.36234, 88.35888, 88.28107, 88.33072, 88.38647, 88.34903, -95.24275, 88.33179, 88.33049, 88.35561, 88.38377, 88.36268, 88.3628, 88.28854, 88.36273, 72.8327, 88.37123, 88.35509, 88.3569, 88.3692, 88.37545, 80.93257, 88.33119, 88.37811, 88.38647, 88.36939, 88.36282, 88.29594, 72.81203, 88.37323, 88.35273, 88.33899, 88.30657, 88.36491, 88.36151, 88.32279, 88.34903, 88.36394, 88.3645, 88.35644, 88.35983, 88.39841, -73.29717, 88.30036, 88.35577, 88.28758, 88.35399, 77.33689, 88.26872, 88.16791, 88.36367, 88.38065, -122.84793, 88.37182, 88.35209, 88.29594, 88.37554, 88.45757, 88.36438, 88.32785, 80.22642, 88.37666, 88.37576, 88.36215, 88.36737, 88.36256, 88.3608, 88.3335, 88.3816, 77.8931, 88.35695, 88.32093, 88.31382, 88.28932, 88.37029, 88.35839, 88.36915, 88.36077, 88.38012, 88.36415, 88.34111, 88.36765, 88.36232, 88.37712, 88.34529, 88.37337, 88.37337, 88.35871, 88.36225, 35.36757, 88.31769, 88.39554, 88.34529, 88.3527, 88.38595, 88.35606, 88.36563, 88.38437, 88.3603, 88.37941, 88.34484, 88.36389, 88.37089, 88.35726, 88.38562, 88.35341, 88.3445, 88.34447, 79.08926, 88.37663, 88.36897, 88.19375, 88.32306, 88.32766, 88.26526, -0.13545, 88.37914]

def check():
	for i in range (0, len(latitude)):
		if (lat1 == latitude[i] and lang1 == longitude[i]):
			current_user.contaminated = 'contaminated'
		elif (lat1 != latitude[i] and lang1 != longitude[i]):
			current_user.contaminated = 'safe'



def uniqueNo(id1, times):
	n = (id1*id1)+(times*times)
	# id1 = n-times
	return n


def qr_code(state, id1, times, username):
		n = uniqueNo(id1, times)
		n1 = username+"@"+ str(n)
		url = 'http://127.0.0.1:5000/api/' + n1
		qr = qrcode.make(url)
		# qr.save(username+'.png')
		return qr

# ps = qr_code(1,3,1, 'sam')
# print (ps)


def save_picture():
	form_picture = qr_code(current_user.state, current_user.id, current_user.times, current_user.username)
	random_hex = secrets.token_hex(8)
	picture_fn = random_hex + '.png'
	picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
	form_picture.save(picture_path)

	return picture_fn

@app.route('/')
@app.route('/home')
@login_required
def hello_home():
	if current_user.times == 1:
		picture_file = save_picture()
		current_user.image_file = picture_file
		image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
		current_user.prev = 1
		check()
		db.session.commit()
		return render_template('index.html', current_user=current_user, image_file=image_file)
	elif current_user.prev == 0:
		picture_file = save_picture()
		current_user.image_file = picture_file
		image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
		if current_user.times > 100:
			current_user.times = 1
		current_user.prev = 1
		check()
		db.session.commit()
		return render_template('index.html', current_user=current_user, image_file=image_file)
    	# return render_template('landing.html')
	elif current_user.prev == 1:
		image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
		check()
		db.session.commit()
		return render_template('index.html', current_user=current_user, image_file=image_file)





@app.route('/trig/<user1>', methods=['POST','GET'])
def trig_func(user1):
	data1 = request.get_json()
	s1 = data1["s1"]
	d1 = data1["d1"]
	# hashed_username = bcrypt.generate_password_hash(user1).decode('utf-8')
	if (bcrypt.check_password_hash(user1, 'som')):
		user = User.query.filter_by(username='som').first()
		user.s1 = s1
		user.d1 = d1
		db.session.commit()
		return jsonify({"s1": s1, "d1": d1})
	else:
		return jsonify({"response": "Not Success"})






@app.route('/api/<name>')
def my_view_func(name):
	name1 = name.split("@")
	user = User.query.filter_by(username=name1[0]).first()
	name1_id = int((int(name1[1])-(user.times*user.times)))
	if (name1_id < 0):
		h = '<h1>'+'Not verified. Please generate another QR'+'</h1>'
		return render_template('status_un.html')

	else:
		name1_id = int(math.sqrt(name1_id))
		if (user.id == name1_id):
			h = '<h1>'+'Verified '+ str(name1_id) +str(user.state)+"</h1>"
			# user.email = "hello123@gmail.com"
			user.times = user.times+1
			user.prev = 0
			db.session.commit()
			if user.state == 0:
				state = 'LOW RISK'
			elif user.state == 1:
				state = 'MEDIUM RISK'
			else:
				state = 'HIGH RISK'
			return render_template('status.html', user=user, state=state)
		else:
			h = '<h1>'+'Not verified. Please generate another QR'+'</h1>'
			return render_template('status_un.html')


@app.route('/risk')
@login_required
def risk():
	return render_template('risk_form.html', current_user=current_user)





@app.route('/receiver', methods = ['POST'])
def my_function():
	data = request.get_json()

	result1 = data["name"]
	result2 = data["id"]
	print(result1)
	print(result2)

	user = User.query.filter_by(username=result2).first()

	
	if(result1 == 50):
		user.state = 1
		db.session.commit()	
	elif(result1<50):
		user.state = 0
		db.session.commit()	
	else:
		user.state = 2
		db.session.commit()

	return jsonify({"response": "Success", "result":result1})

	
	
	



@app.route('/api')
def hello_api():
	return jsonify(books)

@app.route('/map')
@login_required
def hello_map():
	loc();
	return render_template('map.html',apikey=api_key,latitude=latitude,longitude=longitude, current_user=current_user,lat1=lat1, lang1=lang1 )




@app.route('/about')
def hello_about(): 
    return '<h1>About Page</h1>'

@app.route('/register', methods=['GET','POST'])
def hello_register():
	if current_user.is_authenticated:
		return redirect(url_for('hello_home'))

	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, email = form.email.data, pincode = form.pincode.data ,password = hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account Created for { form.username.data }! and you can login', 'success')
		return redirect(url_for('hello_login'))
	return render_template ('Registration.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def hello_login():
	if current_user.is_authenticated:
		return redirect(url_for('hello_home'))

	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember = form.remember.data)
			return redirect(url_for('hello_home'))
		else:
			flash('Check Your Username and Password', 'danger')

	return render_template ('Login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('hello_login'))

