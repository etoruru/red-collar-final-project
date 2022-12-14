from fastapi import Request, Depends
from sqlalchemy.orm import Session

from database.recipe import RecipesRepo
from database.ingredients import IngredientsRepo





def get_db(request: Request):
    session: Session = request.app.state.session_factory()
    try:
        yield session
    finally:
        session.commit()
        session.close()


def get_recipes_repo(session: Session = Depends(get_db)):
    return RecipesRepo(session)


def get_ingredients_repo(session: Session = Depends(get_db)):
    return IngredientsRepo(session)


