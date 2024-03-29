from django.apps import AppConfig
import time

class ForknfindConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forknfind'

    def ready(self): # On startup run the hybrid model

        time.sleep(1) # wait for 1 seconds

        # import the recommendation model
        from .models import HybridRecommender
        from .data import reviewCreator

        # If more reviews are need uncomment
        #reviewCreator()

        # call the recommendation model, as it is a singleton model can just call it using .load()
        #model = HybridRecommender.load()
        # start the recommender using its method .start_recommender()
        #model.start_recommender()
