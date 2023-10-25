from functools import partial
from django.http import JsonResponse
from api.models import DroneStatus, DroneType, Customer, Manager, Owner, CustomerToken, ManagerToken, OwnerToken


def safe_querey(table, **kwargs):
    querey_set = table.objects.filter(**kwargs)
    if not querey_set:
        return None, False

    return querey_set[0], True


CUSTOMER_USER = {
    "user_model": Customer, 
    "token_model": CustomerToken,
    "token_key": "customer-token",
}
MANAGER_USER = {
    "user_model": Manager, 
    "token_model": ManagerToken,
    "token_key": "manager-token",
}
OWNER_USER = {
    "user_model": Owner, 
    "token_model": OwnerToken,
    "token_key": "owner-token",
}


def verify_token(view, user_type):
    def wrapper_verify(*args, **kwargs):
        user_token = args[0].COOKIES.get(user_type["token_key"], False)
        retrieved_token, found = safe_querey(
            user_type["token_model"], token=user_token)
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
        user_type["user_model"], pk=request.POST['username'])
    # susceptible to timing attack
    if not user_found or not check_password(request.POST['password'], user.password_hash):
        return JsonResponse({
            'success': False,
            'message': 'bad login',
        })

    response = JsonResponse({'success': True})
    token = get_random_string(length=128)
    user_type["token_model"](
        token=token,
        user=user
    ).save()
    response.headers["Set-Cookie"] = f"{user_type['token_key']}={token}"

    return response