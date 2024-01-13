from django.apps import AppConfig
import time

class ForknfindConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forknfind'

    def ready(self): # On startup run the hybrid model

        time.sleep(1) # wait for 1 seconds

        from .models import HybridRecommender

        model = HybridRecommender.load()
        model.start_recommender()
        model.query_content_recommender(151)

