from app.db.database import Base # Importar Base para que os modelos possam herdá-la

# Importar modelos para facilitar o acesso e para que o Alembic os detete.
from .user_model import User
from .exercise_definition_model import ExerciseDefinition
from .workout_model import WorkoutLog, WorkoutExercise, ExerciseSet