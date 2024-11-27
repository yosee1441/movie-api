from models.movie import Movie 
from dtos import MovieCreateDto, MovieUpdateDto

class MovieService():
    def __init__(self, db) -> None:
        self.db = db

    def find_all(self):
        movies = self.db.query(Movie).all()
        return movies

    def find_one(self, id: int): 
        movie = self.db.query(Movie).filter(Movie.id == id).first()
        return movie
    
    def find_by_category(self, category: str):
        movies = self.db.query(Movie).filter(Movie.category == category).all()
        return movies
    
    def create(self, movie: MovieCreateDto):
        new_movie = Movie(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        self.db.refresh(new_movie)
        return new_movie
    
    def update(self, id: int, dto: MovieUpdateDto):
        movie = self.find_one(id)

        movie.title = dto.title
        movie.overview = dto.overview
        movie.year = dto.year
        movie.rating = dto.rating
        movie.category = dto.category

        self.db.commit()
        self.db.refresh(movie)

        return movie
    
    def delete(self, id: int):
        self.db.query(Movie).filter(Movie.id == id).delete()
        self.db.commit()
        return





    
