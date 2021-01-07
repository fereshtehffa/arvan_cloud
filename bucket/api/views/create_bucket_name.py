import json
from django.views.decorators.http import require_http_methods
from helpers.validate_params import validate_params
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.models import User
from bucket.models import Bucket,NameException
from django.db.models import Q
SCHEMA = {
    "username": {"type": "string", "required": True, "empty": False},
    "name": {"type": "string", "required": True, "empty": False},
    "prefix": {"type": "string", "required": True, "empty": False, "regex": r"(^[a-zA-Z0-9_.+-]{3,}$)"},
}
@require_http_methods(["POST"])
@validate_params(SCHEMA)
def create_bucket_name(request: HttpRequest) -> JsonResponse:

    request_body = request.body.decode("utf-8")
    data = json.loads(request_body)
    username = data.get("username")
    prefix = data.get("prefix")
    name = data.get("name")

    try:
        if not name.startswith(prefix):
            return JsonResponse(data={"message": "The name is not valid"}, status=404)

        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse(data={"message": "User Not Found"}, status=404)

    if NameException.objects.filter(name=prefix).exists():
        return JsonResponse(data={"message": "This prefix is not valid"}, status=404)

    for item in Bucket.objects.filter(~Q(user__username=username)):
        if prefix.startswith(item.prefix):
            return JsonResponse(data={"message": "This prefix is not valid because it is assigned to someone else!"}, status=404)
    if not Bucket.objects.filter(prefix=prefix, user=user).exists():
        Bucket.objects.create(prefix=prefix, user=user)
    return JsonResponse(data={"message": "created"}, status=201)


