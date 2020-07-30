from django.db import models

# Create your models here.
class Poll(models.Model):
    owner_id = models.CharField('Owner\'s id', max_length=100)
    title = models.CharField('Title', max_length=50)
    option1 = models.CharField('1_st option', max_length=25)
    option2 = models.CharField('2_nd option', max_length=25)
    option3 = models.CharField('3_d option', max_length=25)
    votes1 = models.IntegerField('1_st votes', max_length=300, default=0)
    votes2 = models.IntegerField('2_nd votes', max_length=300, default=0)
    votes3 = models.IntegerField('3_d votes', max_length=300, default=0)
    total = models.IntegerField('total_votes', max_length=300, default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Poll"
        verbose_name_plural = "Polls"