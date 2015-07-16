def serialize(user):
    username = user.username
    profile_picture = user.profile_picture
    full_name = user.full_name
    id_ = user.id
    return {'username': username, 'profile_picture': profile_picture, 'full_name': full_name, 'id': id_}
