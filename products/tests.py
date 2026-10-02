from django.test import TestCase
from products.models import Product, Category, Tag


# Create your tests here.

class ProductSearchTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Categories
        cls.clothes = Category.objects.create(name="Clothes")
        cls.food = Category.objects.create(name="Food")

        # Tags
        cls.vintage = Tag.objects.create(name="Vintage")
        cls.local = Tag.objects.create(name="Local")

        # Products
        cls.pants = Product.objects.create(name="Pants", description="Long pants")
        cls.shorts = Product.objects.create(name="Shorts", description="Navy blue")
        cls.tomato = Product.objects.create(name="Tomato", description="Very big and very red")

        cls.pants.categories.add(cls.clothes)
        cls.pants.tags.add(cls.vintage)
        cls.shorts.categories.add(cls.clothes)
        cls.tomato.categories.add(cls.food)
        cls.tomato.tags.add(cls.local)

    def test_search(self):
        response = self.client.get(
            "/",
            {"q": "pant"},
        )
        self.assertContains(response, "Pants")
        self.assertNotContains(response, "Shorts")

    def test_search_with_no_results(self):
        response = self.client.get(
            "/",
            {"q": "lemon"},
        )
        self.assertContains(response, "No products available.")

    def test_filter_by_category(self):
        response = self.client.get(
            "/",
            {"category": self.clothes.id},
        )
        self.assertContains(response, "Pants")
        self.assertContains(response, "Shorts")
        self.assertNotContains(response, "Tomato")

    def test_filter_by_tag(self):
        response = self.client.get(
            "/",
            {"tag": self.local.id}
        )
        self.assertContains(response, "Tomato")
        self.assertNotContains(response, "Pants")
        self.assertNotContains(response, "Shorts")

    def test_filter_by_category_and_tag(self):
        response = self.client.get(
            "/",
            {"tag": self.vintage.id, "category": self.clothes.id }
        )
        self.assertContains(response, "Pants")
        self.assertNotContains(response, "Shorts")

    def test_filter_by_category_and_tag_with_no_results(self):
        response = self.client.get(
            "/",
            {"tag": self.local.id, "category": self.clothes.id }
        )
        self.assertContains(response, "No products available.")

    def test_search_and_filter_by_category(self):
        response = self.client.get(
            "/",
            {"q": "pant", "category": self.clothes.id},
        )
        self.assertContains(response, "Pants")
        self.assertNotContains(response, "Shorts")

    def test_empty_query(self):
        response = self.client.get(
            "/",
        )
        self.assertContains(response, "Pants")
        self.assertContains(response, "Shorts")
        self.assertContains(response, "Tomato")