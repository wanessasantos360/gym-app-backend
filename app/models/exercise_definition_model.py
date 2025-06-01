from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.database import Base # Importar Base de database.py

class ExerciseDefinition(Base):
    __tablename__ = "exercise_definitions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False, unique=True)
    muscle_group = Column(String, index=True, nullable=True)
    description = Column(Text, nullable=True)
    image_url = Column(String, nullable=True) # URL para uma imagem ou GIF do exercício

    # Relacionamento: Um tipo de exercício pode estar em vários exercícios de treino
    # workout_exercises = relationship("WorkoutExercise", back_populates="exercise_definition")