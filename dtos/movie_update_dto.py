from .movie_create_dto import MovieCreateDto

class MovieUpdateDto(MovieCreateDto):
    id: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripcion de la pelicula",
                "year": 2021,
                "rating": 9.8,
                "category": "Acción",
            }
        }
    }
