from django.db import models

# Create your models here.
#We’ve created a class called Topic which inherits from Model a parent class included in Django that defines the basic 
#functionality of a model.

class Topic(models.Model):         #a model called Topic with fields called text and data_added
    text = models.CharField(max_length = 200)
    data_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):   #The __str__ method is a special method that returns a human-readable string representation of the model instance
        return self.text

#A foreign key is a database term; it’s a reference to another record in the database.
#When Django needs to establish a connection between two pieces of data, it uses the key associated with each piece of information.

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    #def __str__(self) -> str:
        #if len(self.text) > 50:
            #return f"{self.text[:50]}..."
        #else:
            #return self.text 

class Meta:
    verbose_name_plural = 'entries'
    def __str__(self):
        if len(self.text) > 50 :
            return self.text[:50] + "..."    #using text[:50] as the string representation for each entry
        else:
            return self.text