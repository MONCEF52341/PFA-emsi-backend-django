from django.test import TestCase
from .models import LieuTravail
from django.urls import resolve

class LieuTravailTestCase(TestCase):
    def setUp(self):
        # Créer des objets de test ici si nécessaire
        LieuTravail.objects.create(
            designation="OpenSpaceTest",
            description="Ceci est un test d'OpenSpace",
            type="OpenSpace",
            capacite=20
        )

    def test_lieu_travail(self):
        # Récupérer l'objet créé dans setUp()
        lieu_travail_test = LieuTravail.objects.get(designation="OpenSpaceTest")
        # Vérifier si les attributs de l'objet sont corrects
        self.assertEqual(lieu_travail_test.description, "Ceci est un test d'OpenSpace")
        self.assertEqual(lieu_travail_test.type, "OpenSpace")
        self.assertEqual(lieu_travail_test.capacite, 20)


class URLTestCase(TestCase):
    def test_all_urls_return_200(self):
        for url_pattern in urlpatterns:
            # Vérifie si l'élément de urlpatterns est une URL
            if hasattr(url_pattern, 'pattern'):
                # Obtient l'URL à partir du pattern
                url = url_pattern.pattern.regex.pattern
                # Effectue une requête GET à l'URL
                response = self.client.get(url)
                # Vérifie que la réponse est 200 OK
                self.assertEqual(response.status_code, 200, f"{url} a retourné un code de statut différent de 200")