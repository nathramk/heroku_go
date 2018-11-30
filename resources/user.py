from flask_restful import Resource, reqparse
from models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    'email',
    type=str,
    required=True,
    help="cannot be blank"
)
_user_parser.add_argument(
    'password',
    type=str,
    required=True,
    help="Cannot be blank"
)

class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()
        print("tttttttttt:  {}".format(data))
        if UserModel.fin_by_email(data['email']):
            return {'message':'este email: {} ya existe'.format(data['email'])}, 400
        user = UserModel(**data)
        user.save_to_db()

        return {'message':'user created'}, 201


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message':'User not found.'}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message':'User not exist.'}, 404
        user.delete_from_db()
        return {'message':'user deleted'}, 200



class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = _user_parser.parse_args()
        user = UserModel.fin_by_email(data['email'])

        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token},200
        return {'message':'invalid credentials'}, 401
        