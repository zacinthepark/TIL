# API

## Requests: HTTP for Humans

- [Requests Docs](https://requests.readthedocs.io/en/latest/)
- import requests
    - 에러가 뜨지 않으면 이미 설치되어 있는 것
    - 없다면 pip를 통해 설치

---

## TMDB API Project

- Get Popular API
    - [Get Popular API](https://developers.themoviedb.org/3/movies/get-popular-movies)
- Search Movies API
    - [Search Movies API](https://developers.themoviedb.org/3/search/search-movies)
- Get Recommendations API
    - [Get Recommendations API](https://developers.themoviedb.org/3/movies/get-movie-recommendations)
- Get Credits API
    - [Get Credits API](https://developers.themoviedb.org/3/movies/get-movie-credits)
```python
import requests

def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=512acd9151aae945ad5408b2647daba0&language=ko&page=1'
    movie_json_data = requests.get(URL).json()
    results = movie_json_data.get('results')
    popular_movies_count = len(results)
    return popular_movies_count
```
```python
import requests
from pprint import pprint

def vote_average_movies():
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=512acd9151aae945ad5408b2647daba0&language=ko&page=1'
    movie_json_data = requests.get(URL).json()
    results = movie_json_data.get('results')
    movies_over_eight = []
    for movie in results:
        if movie.get('vote_average') >= 8.0:
            movies_over_eight.append(movie)
    return movies_over_eight
```
```python
import requests
from pprint import pprint

def ranking():
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=512acd9151aae945ad5408b2647daba0&language=ko&page=1'
    movie_json_data = requests.get(URL).json()
    results = movie_json_data.get('results')
    vote_average_list = []
    for movie in results:
        vote_average_list.append(movie.get('vote_average'))
    vote_average_list.sort(reverse = True)
    results_by_ranking = []
    for vote_average in vote_average_list:
        for movie in results:
            if movie.get('vote_average') == vote_average:
                results_by_ranking.append(movie)
    return results_by_ranking
```
```python
import requests
from pprint import pprint

def recommendation(title):
    # title을 기반으로 search한 영화의 id값 구하기
    title_param = {'query': title}
    search_base_URL = 'https://api.themoviedb.org/3/search/movie?api_key=512acd9151aae945ad5408b2647daba0&language=ko&page=1&include_adult=false'
    movie_search_data = requests.get(search_base_URL, params = title_param).json()
    search_results = movie_search_data.get('results')
    searched_movie = dict()
    for movie in search_results:
        if title == movie.get('title'):
            searched_movie = movie
    searched_movie_id = searched_movie.get('id')
    # 받아온 id를 기반으로 추천 영화 리스트 반환
    recommendation_URL = f'https://api.themoviedb.org/3/movie/{searched_movie_id}/recommendations?api_key=512acd9151aae945ad5408b2647daba0&language=ko&page=1'
    recommendation_data = requests.get(recommendation_URL).json()
    recommendation_results = recommendation_data.get('results')
    recommendation_list = []
    if recommendation_results:
        for movie in recommendation_results:
            recommendation_list.append(movie.get('title'))
    else:
        return None
    return recommendation_list
```
```python
import requests
from pprint import pprint

def credits(title):
    # title을 기반으로 search한 영화의 id값 구하기
    title_param = {'query': title}
    search_base_URL = 'https://api.themoviedb.org/3/search/movie?api_key=512acd9151aae945ad5408b2647daba0&language=ko&page=1&include_adult=false'
    movie_search_data = requests.get(search_base_URL, params = title_param).json()
    search_results = movie_search_data.get('results')
    if search_results == []:
        return None
    searched_movie = search_results[0]
    searched_movie_id = searched_movie.get('id')

    # credits에 해당하는 캐스팅 인원과 크루 인원에 대한 정보 받아오기
    credits_URL = f'https://api.themoviedb.org/3/movie/{searched_movie_id}/credits?api_key=512acd9151aae945ad5408b2647daba0&language=ko'
    credits_data = requests.get(credits_URL).json()
    casts = credits_data.get('cast')
    crews = credits_data.get('crew')

    # 'cast_id'가 10 미만인 캐스팅 인원, 'department'가 Directing인 인원 걸러내어 반환
    casts_top_10 = []
    crews_directing_department = []
    for cast in casts:
        if cast.get('cast_id') < 10:
            casts_top_10.append(cast.get('name'))
    for crew in crews:
        if crew.get('department') == 'Directing':
            crews_directing_department.append(crew.get('name'))
    return {'cast': casts_top_10, 'directing': crews_directing_department}

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
```
- 마찬가지로 search해서 id값 받아준다
- 해당 id값을 바탕으로 Get Credits API를 통해 출연진과 스태프들 데이터를 받아온다
- 검색 결과가 없는 경우 None을 반환하도록 중간에 예외 처리를 해준다
```
if search_results == []:
        return None
    searched_movie = search_results[0]
    searched_movie_id = searched_movie.get('id')
```
---