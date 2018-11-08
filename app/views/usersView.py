from flask import Blueprint, request, Response
from app.models.database import  User, userList

bp = Blueprint("usersView", __name__, url_prefix="/api/v1")

@bp.route("users", methods=["POST"])
def createUser():
    user = User()
    request_data = request.get_json()
    user.name = request_data["name"]
    user.email = request_data["email"]
    user.password = request_data["password"]
    usersData = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "password": user.password
    }
    userList.append(usersData)
    return Response("account for %s created successfully" % user.name, status=201)