import requests_mock

def test_itune_album_success(client, requests_mock):
    limit = 100
    requests_mock.get(f'https://itunes.apple.com/us/rss/topalbums/limit={limit}/json', status_code = 200, json = "text")
    response = client.get('/ituneAlbums')
    assert response.status_code == 200


def test_itune_album_with_arguement(client, requests_mock):
    limit = 50
    requests_mock.get(f'https://itunes.apple.com/us/rss/topalbums/limit={limit}/json', status_code = 200, json = "text")
    response =  client.get(f'/ituneAlbums', json= {'limit': 50})
    assert response.status_code == 200

def test_itune_album_limit_exceed(client, requests_mock):
    limit = 101
    requests_mock.get(f'https://itunes.apple.com/us/rss/topalbums/limit={limit}/json', status_code = 200, json = "text")
    response =  client.get(f'/ituneAlbums', json = {"limit": 101})
    assert response.status_code == 401

def test_itune_service_down(client, requests_mock):
    limit = 100
    requests_mock.get(f'https://itunes.apple.com/us/rss/topalbums/limit={limit}/json', status_code = 400, json = "text")
    response =  client.get(f'/ituneAlbums')
    assert response.status_code == 501