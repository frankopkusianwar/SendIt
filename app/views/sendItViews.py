from flask import Blueprint, request, Response, json, jsonify
from app.models.database import  User, userList, Parcel, ParcelList

bp = Blueprint("sendItViews", __name__, url_prefix="/api/v1")

@bp.route("users", methods=["POST"])
def createUser():
    user = User()
    request_data = request.get_json()
    user.name = request_data["name"]
    user.email = request_data["email"]
    user.password = request_data["password"]
    if type(user.name) != str:
        return jsonify({'message':'please enter string input for name and email '})
    else:
        usersData = {
            "user.id": user.user_id,
            "name": user.name,
            "email": user.email,
            "password": user.password
        }
        userList.append(usersData)
        return Response("account for %s created successfully" % user.name, status=201)

@bp.route("parcels", methods=["POST"])
def create_parcel_delivery_order():
    parcel = Parcel()
    request_data = request.get_json()
    parcel.pick_up_location = request_data["pick_up_location"]
    parcel.destination = request_data["destination"]
    parcel.contact = request_data["contact"]
    parcel.weight = request_data["weight"]
    parceldata = {
        "parcel_id": parcel.parcel_id,
        "pick_up_location": parcel.pick_up_location,
        "destination": parcel.destination,
        "contact": parcel.contact,
        "weight": parcel.weight
    }
    ParcelList.append(parceldata)
    return Response("parcel being sent to %s created successfully" % parcel.destination, status=201)


    