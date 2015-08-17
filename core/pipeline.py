def save_profile(backend, response, user, *args, **kwargs):
  if not user:
    return
  pic = response.get('profile')
  if pic:
    user.profile.pic = pic
    user.profile.save()
