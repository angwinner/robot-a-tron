from django.shortcuts import render
from django.template import Context, RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from robotApp.models import Robot, Part, Chassis, RobotForm, RobotDeleteForm

def robot_index(request):
    robots = Robot.objects.all().order_by('name')
    t = loader.get_template('index.tmpl')
    c = RequestContext(request, {'robots': robots})
    return HttpResponse(t.render(c))

def add_robot(request):
    if request.method == 'POST':
        form = RobotForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/robot/')
    else:
        form = RobotForm()
        parts = Part.objects.all().order_by('id')
        chassis_list = Chassis.objects.all().order_by('id')
        t = loader.get_template('robot_edit.tmpl')
        c = RequestContext(request, {'form': form, 
                                     'parts': parts, 
                                     "chassis_list": chassis_list,
                                     "action": 'add',
        })
        return HttpResponse(t.render(c))

def edit_robot(request, pk):
    if request.method == 'POST':
        robot = Robot.objects.get(id=pk)
        form = RobotForm(request.POST, instance=robot)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/robot/')
    else:
        robot = Robot.objects.get(id=pk)
        form = RobotForm(instance=robot)
        parts = Part.objects.all().order_by('id')
        chassis_list = Chassis.objects.all().order_by('id')
        t = loader.get_template('robot_edit.tmpl')
        c = RequestContext(request, {'form': form,
                                     'parts': parts,
                                     "chassis_list": chassis_list,
                                     "action": pk + '/edit',
        })
        return HttpResponse(t.render(c))
    
def delete_robot(request, pk):
    robot = Robot.objects.get(id=pk)
    # RobotForm(instance=robot) does not bind the
    # robot data to the form, so it won't validate
    # you must give the form a data dictionary instead
    form = RobotDeleteForm({'id': pk,})
    if request.method == 'POST':
        if form.is_valid(): # checks CSRF
            robot.delete()
            return HttpResponseRedirect('/robot/')
        else:
            return HttpResponseRedirect('/robot/')
    