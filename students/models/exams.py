from django.db import models


class Exam(models.Model):

    """Exam Model"""

    class Meta(object):
        verbose_name = u"Екзамен"
        verbose_name_plural = u"Екзамени"

    title = models.CharField(max_length=256,
                             blank=False,
                             verbose_name=u"Назва")

    date = models.DateField(verbose_name=u'Дата',
                            blank=False)

    teacher = models.CharField(max_length=256,
                               blank=False,
                               verbose_name=u"Викладач")

    exam_group = models.ForeignKey('Group',
                                   verbose_name=u'Група',
                                   blank=False)

    def __str__(self):
        return u"%s - %s (%s)" % (self.title, self.exam_group, self.teacher)
