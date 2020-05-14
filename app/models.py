from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db
from flask import current_app


class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER, primary_key=True)
    email = db.Column(db.String(256), unique=True, index=True)
    name = db.Column(db.String(10), nullable=False, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    password_hash = db.Column(db.String(256))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.name

    def __init__(self, **kwargs):
        super.__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(permission=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()




class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)

    users = db.relationship('User', backref='role')
    """
    一个名叫backref的参数,叫做反向关系,我们将其设置成'role'
    它会像User模型中添加一个名叫做role的属性,这个属性可以替代role_id访问Role模型,但是它获取的是Role模型的对象,而非Role模型对应的id的值。
    """

    def __repr__(self):
        return '<Role %r>' % self.name

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW |
                     Permission.COMMENT |
                     Permission.WRITE_ARTICLES, True),
            'Moderator': (Permission.FOLLOW |
                          Permission.COMMENT |
                          Permission.WRITE_ARTICLES |
                          Permission.MODERATE_COMMENTS, False),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()



