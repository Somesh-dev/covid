
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	prev = db.Column(db.Integer, nullable=False, default=0)
	times = db.Column(db.Integer, nullable=False, default=1)
	state = db.Column(db.Integer, nullable=False, default=0)
	username = db.Column(db.String(20), unique=True, nullable=False)
	pincode = db.Column(db.Integer, unique=False, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.png')
	password = db.Column(db.String(60), nullable=False)
	contaminated = db.Column(db.String(14), nullable=False, default='contaminated')
	s1 = db.Column(db.Integer, nullable=False, default=0)
	d1 = db.Column(db.Integer, nullable=False, default=0)

	def __repr__(self):
		return "User('{u}','{e}','{i}','{id}','{s}','{t}', '{p}', '{c}', '{s1}', '{d1}')".format(u=self.username, e=self.email, i=self.image_file, id=self.id, s=self.state, t=self.times, p=self.pincode, c=self.contaminated, s1=self.s1 ,d1=self.d1)
