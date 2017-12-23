#
# script for various ORM models for project
#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import ForeignKey


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boatdb.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost/boatappdb'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.BigInteger, primary_key=True)
    nickname = db.Column(db.String(60), unique=True)
    # email = db.Column(db.String(60), unique=True)
    phone = db.Column(db.String(20), unique=True)
    town = db.Column(db.String(60))
    district = db.Column(db.String(16))
    dob = db.Column(db.String(64))
    boatinfo = db.Column(db.String(120))
    value = db.Column(db.Integer)

    # todo - work on picture feature of profile later !!!!!
    # pic =

    # verification code
    vcode = db.Column(db.String(6))

    # verification done
    vdone = db.Column(db.Boolean, default=False)

    # timestamp
    ts = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)

    def __init__(self, phone, vcode):
        self.phone = phone
        self.vcode = vcode

    # def __init__(self, nickname, town, district, dob, boatinfo, value):
    #     self.nickname = nickname
    #     self.town = town
    #     self.district = district
    #     self.dob = dob
    #     self.boatinfo = boatinfo
    #     self.value = value

    def __repr__(self):
        return '<User:  #%r>' % self.id

    @property
    def serialize(self):
        """ Return object data in easily serializeable format """

        return {
            'id': self.id,
            'phone': self.phone,
            'vcode': self.vcode
        }

    @property
    def serializes(self):
        """Return object data in easily serializeable format"""

        return {
            'nickname': self.nickname,
            'town': self.town,
            'district': self.district,
            'dob': self.dob,
            'boatinfo': self.boatinfo
        }


class Boat(db.Model):
    """
    model for police boat
    """
    __tablename__ = 'boat'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(60), unique=True)

    # Boat type can be undercover cop or waterPolice boat
    btype = db.Column(db.Integer)

    # timestamp
    ts = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)

    def __init__(self, name, btype):
        self.name = name
        self.btype = btype

    def __repr__(self):
        return '<Boat:  #%r>' % self.name


class Report(db.Model):
    """
    model for police boat location
    """
    __tablename__ = 'report'

    id = db.Column(db.BigInteger, primary_key=True)
    # boat = db.Column(db.BigInteger, ForeignKey('boat.id'))
    boat_name = db.Column(db.String(60))
    boat_type = db.Column(db.Integer)
    lat = db.Column(db.Float, unique=True)
    lng = db.Column(db.Float, unique=True)
    user = db.Column(db.BigInteger, ForeignKey('user.id'))

    # timestamp
    ts = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)

    def __init__(self, boat_name, boat_type, lat, lng, user):
        self.boat_name = boat_name
        self.boat_type = boat_type
        self.lat = lat
        self.lng = lng
        self.user = user

    def __repr__(self):
        return '<Report:  #%r>' % self.id

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {
           'report_id': self.id,
           'boat_name': self.boat_name,
           'boat_type': self.boat_type,
           'lat': self.lat,
           'lng': self.lng,
           'user': self.user,
           'ts': str(self.ts)
        }


class Likes(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.BigInteger, primary_key=True)
    report = db.Column(db.BigInteger, ForeignKey('report.id'))
    user = db.Column(db.BigInteger, ForeignKey('user.id'))
    value = db.Column(db.Integer)
    flag = db.Column(db.Integer)

    # timestamp
    ts = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)

    def __init__(self, report, user, value, flag):
        self.report = report
        self.user = user
        self.value = value
        self.flag = flag

    def __repr__(self):
        return '<Likes:  #%r>' % self.id


class Thanks(db.Model):
    __tablename__ = 'thanks'

    id = db.Column(db.BigInteger, primary_key=True)
    report = db.Column(db.BigInteger, ForeignKey('report.id'))
    user = db.Column(db.BigInteger, ForeignKey('user.id'))
    value = db.Column(db.Integer)

    # timestamp
    ts = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)

    def __init__(self, report, user, value):
        self.report = report
        self.user = user
        self.value = value

    def __repr__(self):
        return '<Thanks:  #%r>' % self.id


################################
#                              #
#       SOME QUICK TESTS       #
#                              #
################################
if __name__ == "__main__":

    try:
        db.create_all()
        print ("================================= create_all ===================================")
    except Exception as exp:
        print '[Models] Got Exception: %s' % exp
    """
    user = User("77777777", "abc123")
    db.session.add(user)
    db.session.commit()
    """
    # print ("Users:",  User.query.all())
