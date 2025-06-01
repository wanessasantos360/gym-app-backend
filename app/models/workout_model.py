from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float, func
from sqlalchemy.orm import relationship
from app.db.database import Base # Importar Base de database.py
# Importar User e ExerciseDefinition para ForeignKey e relationship type hints
# from .user_model import User # Já importado implicitamente via __init__.py para Alembic
# from .exercise_definition_model import ExerciseDefinition

class WorkoutLog(Base):
    __tablename__ = "workout_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date_performed = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=True)
    end_time = Column(DateTime(timezone=True), nullable=True)
    notes = Column(Text, nullable=True)

    user = relationship("User", back_populates="workout_logs")
    exercises = relationship("WorkoutExercise", back_populates="workout_log", cascade="all, delete-orphan")

class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id = Column(Integer, primary_key=True, index=True)
    workout_log_id = Column(Integer, ForeignKey("workout_logs.id"), nullable=False)
    exercise_definition_id = Column(Integer, ForeignKey("exercise_definitions.id"), nullable=False)
    order_in_workout = Column(Integer, nullable=True) # Ordem do exercício no treino

    workout_log = relationship("WorkoutLog", back_populates="exercises")
    exercise_definition = relationship("ExerciseDefinition") # Um WorkoutExercise tem uma ExerciseDefinition
    sets = relationship("ExerciseSet", back_populates="workout_exercise", cascade="all, delete-orphan")

class ExerciseSet(Base):
    __tablename__ = "exercise_sets"

    id = Column(Integer, primary_key=True, index=True)
    workout_exercise_id = Column(Integer, ForeignKey("workout_exercises.id"), nullable=False)
    set_number = Column(Integer, nullable=False) # Ex: 1ª série, 2ª série
    repetitions = Column(Integer, nullable=True) # Número de repetições realizadas
    weight_lifted = Column(Float, nullable=True) # Peso levantado (ex: 50.5 kg)
    rest_time_seconds = Column(Integer, nullable=True) # Tempo de descanso após esta série

    workout_exercise = relationship("WorkoutExercise", back_populates="sets")