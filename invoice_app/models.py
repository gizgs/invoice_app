from django.db import models
from django.utils import timezone

class User(models.Model):
	user_is_admin = models.BooleanField(default = False)
	user_id = models.AutoField(primary_key = True)
	user_login = models.CharField(max_length = None)
	user_password = models.CharField(max_length = 50)
	user_mail = models.EmailField(max_length = 254)

	def user_add():
		pass

	def user_del():
		pass

	def user_change():
		pass


class Invoice(models.Model):
	invoice_id = models.AutoField(primary_key = True)
	invoice_user_id = przy każdej fakturze musi być numer id użytkownika który ją dodał
	invoice_date_of_issue = models.DateField()
	invoice_nr = models.CharField(max_length = None)
	invoice_name = models.CharField(max_length = None)
	invoice_netto = models.FloatField()
	invoice_vat = models.FloatField()
	invoice_brutto =models.FloatField()
	invoice_place = wyświetlić w combobox wszystkie miejscowości
	invoice_file = models.FileField()

	def invoice_add(self):
		pass

	def invoice_del(self):
		pass
	
	def invoice_change(self):
		pass

	def invoice_view(self):
		pass

class City(models.Model):
	city_id = models.AutoField(primary_key = True)
	city_name = models.CharField(max_length = None)
	city_is_active = models.BooleanField(default = True)
	