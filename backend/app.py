from backend.recommender import recommend
from backend.performance import load_user_progress, save_user_progress

def get_next_recommendation(user_id: int):
    # Load progress of this user (from JSON DB)
    progress = load_user_progress(user_id)

    # Decide what to recommend next
    next_material = recommend(progress)

    # Store progress back in DB
    save_user_progress(user_id, next_material)

    # Return recommended material string
    return next_material
