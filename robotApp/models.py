from django.db import models
from django.forms import ModelForm, ModelChoiceField, Select, ValidationError

class Part(models.Model):
    
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
class Chassis(Part):
    weight_capacity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    
class Robot(models.Model):
    name = models.CharField(max_length=50, default="unnamed")
    chassis = models.ForeignKey(
                Chassis,
                limit_choices_to={'type': 'c'},
                default = '2',
                )
    propulsion = models.ForeignKey(
                Part, 
                related_name='propPart',
                limit_choices_to={'type': 'p'},
                default = '7',
                )
    power = models.ForeignKey(
                Part, 
                related_name="powerPart",
                limit_choices_to={'type': 'e'},
                default = '18',
                )
    weapon1 = models.ForeignKey(
                Part, 
                related_name="weapon1Part",
                limit_choices_to={'type': 'w'},
                default = '23'
    )
    weapon2 = models.ForeignKey(
                Part, 
                related_name="weapon2Part",
                limit_choices_to={'type': 'w'},
                default = 32,
    )
    armor = models.ForeignKey(
                Part, 
                related_name="armorPart",
                limit_choices_to={'type': 'a'},
                default = '31',
    )
    
class RobotForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (RobotForm, self).__init__(*args, **kwargs)
        self.fields['chassis'].widget.attrs = {'onchange': 'chassis_script()'}
        self.fields['propulsion'].widget.attrs = {'onchange': 'propulsion_script()'}
        self.fields['power'].widget.attrs = {'onchange': 'power_script()'}
        self.fields['weapon1'].widget.attrs = {'onchange': 'weapon1_script()'}
        self.fields['weapon2'].widget.attrs = {'onchange': 'weapon2_script()'}
        self.fields['armor'].widget.attrs = {'onchange': 'armor_script()'}
        
    def clean(self):
        super (RobotForm, self).clean()
        if (self.cleaned_data['chassis'] and
            self.cleaned_data['propulsion'] and
            self.cleaned_data['power'] and
            self.cleaned_data['weapon1'] and
            self.cleaned_data['weapon2'] and
            self.cleaned_data['armor']):
            
            chas_name = self.cleaned_data['chassis']
            chassis = Part.objects.get(name=chas_name)
            frame = Chassis.objects.get(id=chassis.id)
            weight_limit = frame.weight_capacity
            total_weight = chassis.weight
            total_weight += self.get_weight_from_name(self.cleaned_data['propulsion'])
            total_weight += self.get_weight_from_name(self.cleaned_data['power'])
            total_weight += self.get_weight_from_name(self.cleaned_data['weapon1'])
            total_weight += self.get_weight_from_name(self.cleaned_data['weapon2'])
            total_weight += self.get_weight_from_name(self.cleaned_data['armor'])
            if total_weight > weight_limit:
                raise ValidationError("Robot weight exceeds chassis weight capacity")
        
    def get_weight_from_name(self, name):
        part = Part.objects.get(name=name)
        return part.weight
        
    class Meta:
        model = Robot
        fields = ['name', 'chassis', 'propulsion', 'power', 'weapon1', 'weapon2', 'armor']
        
class RobotDeleteForm(ModelForm):
    class Meta:
        model = Robot
        fields = [] # just the id