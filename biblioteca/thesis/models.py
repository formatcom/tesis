#!/usr/bin/python
# -*- coding: utf-8 -*-
from .validators import validate_file_extension, validate_file_image


from django.db        import models
from author.models    import Author


class Careers(models.Model):
	name = models.CharField('Carrera', max_length=100, unique=True)

	class Meta:
		verbose_name		= 'Carrera'
		verbose_name_plural	= 'Carreras'

	def __unicode__(self):
		return '%s' % self.name


class Line(models.Model):
	name = models.CharField('Línea de investigación', max_length=100, unique=True)

	class Meta:
		verbose_name		= 'Línea de investigación'
		verbose_name_plural	= 'Línea de investigación'

	def __unicode__(self):
		return '%s' % self.name


class Thesis(models.Model):
	id           = models.AutoField       ( 'Registro',                              primary_key = True                         )
	title        = models.CharField       ( 'Titulo',                 max_length=100                                            )
	author       = models.ManyToManyField (                Author,                   verbose_name='Autores'                     )
	career       = models.ManyToManyField (                Careers,                  verbose_name='Carreras'                    )
	line         = models.ForeignKey      (                Line,                     verbose_name='línea de investigación'   )
	year         = models.IntegerField    ( 'Año'                                                                               )
	cover        = models.FileField       ( 'Portada',     upload_to='cover/%Y/%m/%d',     validators=[validate_file_image]     )
	thesis_pdf   = models.FileField       ( 'Tesis pdf',   upload_to='documents/%Y/%m/%d', validators=[validate_file_extension] )
	abstract_pdf = models.FileField       ( 'Resumen pdf', upload_to='documents/%Y/%m/%d', validators=[validate_file_extension] )
	note         = models.TextField       ( 'Nota',        blank=True                                                           )
	public       = models.BooleanField    ( 'Público',     default=False                                                        )

	class Meta:
		verbose_name		= 'Tesis'
		verbose_name_plural	= 'Tesis'

	def portada(self):
		if self.public:
			link = self.thesis_pdf.url
		else:
			link = self.abstract_pdf.url

		return """
			<a href="%s" target="_blank"><img src="%s" width="90" height="120" /></a>
		""" % (link, self.cover.url)

	portada.allow_tags = True

	def __unicode__(self):
		return '%s' % self.title