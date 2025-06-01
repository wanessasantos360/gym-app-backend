# Importar esquemas para facilitar o acesso
from .user_schema import User, UserCreate, UserBase
from .token_schema import Token, TokenData
from .exercise_definition_schema import ExerciseDefinition, ExerciseDefinitionCreate, ExerciseDefinitionBase
from .workout_schema import (
    ExerciseSet, ExerciseSetCreate, ExerciseSetBase,
    WorkoutExercise, WorkoutExerciseCreate, WorkoutExerciseBase,
    WorkoutLog, WorkoutLogCreate, WorkoutLogBase
)