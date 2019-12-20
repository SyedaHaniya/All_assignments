#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Car:
    def __init__(self,name, company, model, color, rating):
        self.company = company
        self.name = name
        self.model = model
        self.color = color
        self.rating = rating
    
    def Color(self):
        print("The color of your car is " + self.color)
        
    def Rating(self):
        print("Weight of your car is " + self.weight)
        
    def Name_Model(self):
        print("Name: " + self.name + " Model: " + self.model)
        

Object1 = Car("Accord", "Honda", "2009", "Red", "4")
Object2 = Car("Alto", "Suzuki", "2009", "Blue", "4")
Object3 = Car("Indus", "Corolla", "2012", "White", "5")
Object4 = Car("GLI", "Corolla", "2015", "Black", "5")
Object5 = Car("XLI", "Corolla", "2014", "Black", "4")
Object1.Name_Model()
Object2.Name_Model()
Object3.Name_Model()
Object4.Name_Model()
Object5.Name_Model()

        


# In[ ]:




