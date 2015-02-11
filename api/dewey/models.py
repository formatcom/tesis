from django.db import models

class Dewey(models.Model):
	id          = models.CharField(max_length=3, primary_key = True)
	description = models.CharField('Descripcion', max_length=45)

	class Meta:
		verbose_name		= 'Dewey'
		verbose_name_plural	= 'Dewey'
		ordering			= ('id',)

	def __unicode__(self):
		return '%s - %s' % ( self.id, self.description) 