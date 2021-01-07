import json
import boto3
from django.views.decorators.http import require_http_methods
from helpers.validate_params import validate_params
from django.http import HttpRequest, JsonResponse
from bucket.models import Bucket
from ArvanCloud.settings import endpoint,access_key,secret_key
SCHEMA = {
    "bucket_name": {"type": "string", "required": True, "empty": False},
    "username": {"type": "string", "required": True, "empty": False},

}

@require_http_methods(["POST"])
@validate_params(SCHEMA)
def create_bucket(request: HttpRequest) -> JsonResponse:

    request_body = request.body.decode("utf-8")
    data = json.loads(request_body)
    bucket_name = data.get("bucket_name")
    username = data.get("username")

    flag = False
    for item in Bucket.objects.filter(user__username=username):
        if bucket_name.startswith(item.prefix):
            flag = True
            break
    if not flag:
        return JsonResponse(data={"message": "This bucket name is not valid"}, status=404)
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        endpoint_url=endpoint,
    )
    response = s3_client.list_buckets()
    if bucket_name in [item["Name"] for item in response["Buckets"]]:
        return JsonResponse(data={"message": "This bucket  is already exists!"}, status=404)
    s3_client.create_bucket(Bucket=bucket_name)
    return JsonResponse(data={"message": "bucket created"}, status=201)




