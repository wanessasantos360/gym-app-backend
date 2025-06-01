from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Esquemas para ExerciseSet
class ExerciseSetBase(BaseModel):
    set_number: int
    repetitions: Optional[int] = None
    weight_lifted: Optional[float] = None
    rest_time_seconds: Optional[int] = None

class ExerciseSetCreate(ExerciseSetBase):
    pass

class ExerciseSet(ExerciseSetBase):
    id: int
    # workout_exercise_id: int # Opcional, dependendo se quer expor no schema de resposta

    class Config:
        from_attributes = True

# Esquemas para WorkoutExercise
class WorkoutExerciseBase(BaseModel):
    exercise_definition_id: int
    order_in_workout: Optional[int] = None

class WorkoutExerciseCreate(WorkoutExerciseBase):
    sets: List[ExerciseSetCreate] = []

class WorkoutExercise(WorkoutExerciseBase):
    id: int
    # workout_log_id: int # Opcional
    exercise_definition: Optional[ExerciseDefinition] = None # Para incluir detalhes do exercício
    sets: List[ExerciseSet] = []

    class Config:
        from_attributes = True

# Esquemas para WorkoutLog
class WorkoutLogBase(BaseModel):
    date_performed: Optional[datetime] = None # Permitir default no backend ou definir no frontend
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    notes: Optional[str] = None

class WorkoutLogCreate(WorkoutLogBase):
    # user_id será obtido do utilizador autenticado no backend
    exercises: List[WorkoutExerciseCreate] = []

class WorkoutLog(WorkoutLogBase):
    id: int
    user_id: int
    exercises: List[WorkoutExercise] = []

    class Config:
        from_attributes = True