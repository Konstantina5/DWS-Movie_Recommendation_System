import requests


class Recommendation:
    @staticmethod
    def get_reviews_for_movie(movies, movie):
        for i in movie['similar_movie_indices']:
            id = movies.iloc[i]['id']
            access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNTkzNzZlMzA4ZjhmZWM4ZTY2YjFlNGU1MmU1MGFlZCIsIm5iZiI6MTcyMjE1NDE4NC4wNDQ5NTMsInN1YiI6IjY2YTVmMjY3Yjg5NTNmYTAyMDcyMjQ5OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2ZY1JKdQ3KhzbIHUimEaNlAT7up3XM7MZukzhSe27TA'
            url = f'https://api.themoviedb.org/3/movie/{id}/reviews?language=en-US&page=1'

            headers = {
                "accept": "application/json",
                "Authorization": f'Bearer {access_token}'
            }

            response = requests.get(url, headers=headers)
            movie_rev = []
            for item in response.json()['results']:
                movie_rev.append(item['content'])

            return movie_rev

