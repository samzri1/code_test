from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(5, 15) # temps d'attente entre les requêtes

    @task(1)
    def index(self):
        self.client.get("/")



#Dans ce code, une classe MyUser est définie en tant qu'utilisateur simulé qui effectue des requêtes. La méthode wait_time est définie pour indiquer le temps d'attente entre les requêtes, qui est défini comme étant entre 5 et 15 secondes dans ce cas. La méthode index est annotée avec @task(1) pour indiquer qu'elle est une tâche que l'utilisateur simulé peut effectuer, qui consiste à effectuer une requête GET sur la racine du site ("/").

#Le code semble donc correct, mais il est possible de l'adapter en fonction de vos besoins spécifiques. Vous pouvez ajouter d'autres tâches en définissant d'autres méthodes annotées avec @task, et vous pouvez également modifier le temps d'attente entre les requêtes en modifiant les valeurs dans la méthode wait_time.