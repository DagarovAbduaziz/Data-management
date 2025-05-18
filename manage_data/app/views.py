from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Patient, Disease, Staff
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Disease
from .forms import PatientForm, DiseaseForm, StaffForm
from django.contrib.auth import logout

@login_required
def profile(request):
    return render(request, 'profile.html')





def patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})

def patient_add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PatientForm()
    return render(request, 'patients/form.html', {'form': form, 'title': 'Add New Patient'})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patients/detail.html', {'patient': patient})

def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/form.html', {'form': form, 'title': 'Edit Patient'})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('dashboard')
    return render(request, 'patients/delete.html', {'patient': patient})

@login_required
def dashboard(request):
    patients = Patient.objects.all()
    staff = Staff.objects.all()
    diseases = Disease.objects.all()

    # Prepare charts (optional dummy example)
    disease_labels = [d.name for d in diseases][:10]
    disease_counts = [Patient.objects.filter(disease=d).count() for d in diseases][:10]

    age_groups = ['0-18', '19-35', '36-60', '61+']
    age_counts = [
        Patient.objects.filter(age__lte=18).count(),
        Patient.objects.filter(age__gt=18, age__lte=35).count(),
        Patient.objects.filter(age__gt=35, age__lte=60).count(),
        Patient.objects.filter(age__gt=60).count(),
    ]

    return render(request, 'dashboard.html', {
        'patients': patients,
        'staff': staff,
        'diseases': diseases,
        'disease_labels': disease_labels,
        'disease_counts': disease_counts,
        'age_groups': age_groups,
        'age_counts': age_counts,
    })

def staff(request):
    staff = Staff.objects.all()
    return render(request, 'staff.html', {'staff': staff})

def staff_add(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff')
    else:
        form = StaffForm()
    return render(request, 'staff/form.html', {'form': form, 'title': 'Add New Staff Member'})
def staff_edit(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff/form.html', {'form': form, 'title': 'Edit Staff Member'})
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff')
    return render(request, 'staff/delete.html', {'staff': staff})
def staff_detail(request, pk): 
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff/detail.html', {'staff': staff})


def diseases(request):
    diseases = Disease.objects.all()
    return render(request, 'diseases.html', {'diseases': diseases})
def disease_add(request):
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diseases')
    else:
        form = DiseaseForm()
    return render(request, 'diseases/form.html', {'form': form, 'title': 'Add New Disease'})
def disease_edit(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    if request.method == 'POST':
        form = DiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('diseases')
    else:
        form = DiseaseForm(instance=disease)
    return render(request, 'diseases/form.html', {'form': form, 'title': 'Edit Disease'})
def disease_delete(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    if request.method == 'POST':
        disease.delete()
        return redirect('disease')
    return render(request, 'diseases/delete.html', {'disease': disease})
def disease_detail(request, pk):    
    disease = get_object_or_404(Disease, pk=pk)
    return render(request, 'diseases/detail.html', {'disease': disease})