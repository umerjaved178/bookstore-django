from django.test import SimpleTestCase
from django.urls import reverse,resolve

from .views import HomePageView, AboutPageView
# Create your tests here.

class HomeTest(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_home_status(self):
      
        self.assertEqual(self.response.status_code,200)
        
   # def test_home_url(self):
    #    response = self.client.get(reverse('home'))
     #   self.assertEqual(sresponse.status_code, 200)
        
    def test_homTemplateUSed(self):
        self.assertTemplateUsed(self.response,'home.html')
        
    def test_correctHTML(self):
        self.assertContains(self.response, 'Homepage')
        
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
    
class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url=reverse('about')
        self.response=self.client.get(url)
        
    def test_about_statuscode(self):
        self.assertEqual(self.response.status_code, 200)
        
        
    def test_about_correcthtml(self):
        self.assertContains(self.response, 'About Page')
        
    def test_about_Notcontin(self):
        self.assertNotContains(self.response,'Hi there it was pafe')
        
    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
        view.func.__name__,
        AboutPageView.as_view().__name__
        )
        
    