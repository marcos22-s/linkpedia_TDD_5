from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import LinkModel
from core.forms import LinkModelForm

UserModel = get_user_model()

class LinkCRUDTest(TestCase):
    def setUp(self):
        self.user_marcos = UserModel.objects.create_user(
            username='marcos',
            email='marcos@cps.sp.gov.br',
            password='senha_marcos_123'
        )
        
        self.user_isabelle = UserModel.objects.create_user(
            username='isabelle',
            email='isabelle@cps.sp.gov.br',
            password='senha_isabelle_456'
        )
        
        self.user_natalia = UserModel.objects.create_user(
            username='natalia',
            email='natalia@cps.sp.gov.br',
            password='senha_natalia_789'
        )

        self.link_existente = LinkModel.objects.create(
            titulo='Google',
            link='https://www.google.com',
            observacao='Buscador padrão'
        )

    def test_form_has_expected_fields(self):
        form = LinkModelForm()
        expected = ['titulo', 'link', 'observacao']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_link_form_valid_data(self):
        form = self.make_link_form()
        self.assertTrue(form.is_valid())

    def test_link_form_invalid_url(self):
        form = self.make_link_form(link='url_invalida')
        self.assertFalse(form.is_valid())
        self.assertIn('link', form.errors)

    def test_redirect_if_not_logged_in(self):
        urls = [
            reverse('cadastrar_link'),
            reverse('listar_links'),
            reverse('atualizar_link', args=[self.link_existente.id]),
            reverse('remover_link', args=[self.link_existente.id])
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)

    def test_cadastrar_link_via_post_com_marcos(self):
        self.client.force_login(self.user_marcos)
        dados = {'titulo': 'GitHub', 'link': 'https://github.com', 'observacao': 'Dev'}
        response = self.client.post(reverse('cadastrar_link'), data=dados)
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(LinkModel.objects.filter(titulo='GitHub').exists())

    def test_listar_links_view_com_isabelle(self):
        self.client.force_login(self.user_isabelle)
        response = self.client.get(reverse('listar_links'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Google')

    def test_atualizar_link_via_post_com_natalia(self):
        self.client.force_login(self.user_natalia)
        dados = {'titulo': 'Google Atualizado', 'link': 'https://www.google.com.br', 'observacao': 'Alterado'}
        response = self.client.post(reverse('atualizar_link', args=[self.link_existente.id]), data=dados)
        
        self.assertEqual(response.status_code, 302)
        self.link_existente.refresh_from_db()
        self.assertEqual(self.link_existente.titulo, 'Google Atualizado')

    def test_remover_link_via_post_com_marcos(self):
        self.client.force_login(self.user_marcos)
        response = self.client.post(reverse('remover_link', args=[self.link_existente.id]))
        
        self.assertEqual(response.status_code, 302)
        self.assertFalse(LinkModel.objects.filter(id=self.link_existente.id).exists())


    def make_link_form(self, **kwargs):
        valid = dict(titulo='Fatec', link='https://www.fatec.sp.gov.br', observacao='Faculdade')
        data = dict(valid, **kwargs)
        form = LinkModelForm(data=data)
        return form