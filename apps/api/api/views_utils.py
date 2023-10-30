from functools import partial
from django.http import JsonResponse as DjJsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.utils.crypto import get_random_string
from api.models import DroneStatus, DroneType, Customer, Manager, Owner, CustomerToken, ManagerToken, OwnerToken

class JsonResponse(DjJsonResponse):
    def __init__(self, *args, **kwargs):
        super(JsonResponse, self).__init__(*args, **kwargs)
        self.headers["Access-Control-Allow-Origin"] = "*"


def safe_querey(table, **kwargs):
    querey_set = table.objects.filter(**kwargs)
    if not querey_set:
        return None, False

    return querey_set[0], True

class UserType:
    def __init__(self, user_model, token_model, token_key):
        self.user_model = user_model
        self.token_model = token_model
        self.token_key = token_key

CUSTOMER_USER = UserType(Customer, CustomerToken, "customer-token")
MANAGER_USER = UserType(Manager, ManagerToken, "manager-token")
OWNER_USER = UserType(Owner, OwnerToken,"owner-token")


def verify_token(view, user_type):
    def wrapper_verify(*args, **kwargs):
        user_token = args[0].COOKIES.get(user_type.token_key, False)
        retrieved_token, found = safe_querey(
            user_type.token_model, token=user_token)
        if not found: 
            return JsonResponse({'success': False, 'message': 'bad token'})

        return view(*args, user=retrieved_token.user, **kwargs)
    
    return wrapper_verify


verify_customer_token = partial(verify_token, user_type=CUSTOMER_USER)
verify_manager_token = partial(verify_token, user_type=MANAGER_USER)
verify_owner_token = partial(verify_token, user_type=OWNER_USER)



def user_login(request, user_type):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required.',
        })

    user, user_found = safe_querey(
        user_type.user_model, pk=request.POST['username'])
    # susceptible to timing attack
    if not user_found or not check_password(request.POST['password'], user.password_hash):
        return JsonResponse({
            'success': False,
            'message': 'bad login',
        })

    response = JsonResponse({'success': True})
    token = get_random_string(length=128)
    user_type.token_model(
        token=token,
        user=user
    ).save()
    response.headers["Set-Cookie"] = f"{user_type.token_key}={token}"

    return response


def new_user(request, user_type):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required. Do not use these credentials.'
        })

    _, username_taken = safe_querey(user_type.user_model, pk=request.POST['username'])
    if username_taken:
        return JsonResponse({
            'success': False,
            'message': 'username taken'
        })
    
    user_type.user_model(
        username=request.POST['username'],
        password_hash=make_password(request.POST['password']),
        first_name=request.POST['firstName'],
        last_name=request.POST['lastName'],
    ).save()

    return JsonResponse({'success': True})