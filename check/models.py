from django.db import models
from django.utils import timezone

class item(models.Model):
    no = models.CharField(max_length=20)
    group = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    slot = models.CharField(max_length=20)
    oldNo = models.CharField(max_length=20)
    groupText = models.CharField(max_length=20)
    safetyAmount = models.CharField(max_length=4, default='0')
    amount = models.IntegerField(default=0)
    buyAmount = models.CharField(max_length=4, default='0')
    totalAmount = models.CharField(max_length=4, default='0')
    itemType = models.CharField(max_length=2)
    BUn = models.CharField(max_length=10)
    price = models.FloatField(default=0)
    totalPrice = models.FloatField(default=0)
    Pe = models.CharField(max_length=5, default='0')
    Plnt = models.CharField(max_length=5, default='0')
    Sloc = models.CharField(max_length=5, default='0')
    itemGroup = models.CharField(max_length=5, default='0')
    itemUsage = models.TextField(default='none')
    updateDate = models.DateField(auto_now_add=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "%s %s %s %d %s" % (self.no, self.name, self.description, self.amount, self.updateDate)

class itemcheck(models.Model):
    no = models.ForeignKey('item')
    amount = models.IntegerField(default=0)
    realAmount = models.IntegerField(default='none')
    updateDate = models.DateField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.no    
