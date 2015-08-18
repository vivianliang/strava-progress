import requests


def _header(user):
  return {'Authorization': 'Bearer %s' % user.social_auth.first().extra_data['access_token']}


def _get(url, user, params=None):
  response_data = requests.get(url, headers=_header(user), params=params).json()
  if len(response_data) == 30:
    response_data['more'] = True
  return response_data


def get_starred_segments(user):
  url = 'https://www.strava.com/api/v3/segments/starred'
  return _get(url, user)


