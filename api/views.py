# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from datetime import datetime

# ------------------------------
# Register pages
# ------------------------------
def register_page(request):
    return render(request, "api/register.html")

def register_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        college_id = request.POST.get("id")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmpassword")

        if password != confirm_password:
            return HttpResponse("Passwords do not match!")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )

        return HttpResponse("Registration Successful!")

    return HttpResponse("Invalid Request")

# ------------------------------
# Complaint pages
# ------------------------------
def complaint_page(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        complaint_details = request.POST.get('complaint_details')
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        branch = request.POST.get('branch')
        year = request.POST.get('year')

        print(f"Complaint submitted: {topic}, {name}, {rollno}")

        return redirect('complaint_success')

    return render(request, 'api/complaint.html')

def complaint_success(request):
    return render(request, 'api/success.html')

# ------------------------------
# Lost and Found
# ------------------------------
def lost_and_found(request):
    matches = []
    searched = False

    if request.method == "POST":
        searched = True

        lost_desc = request.POST.get("lost_desc", "").lower()
        lost_cat = request.POST.get("lost_cat", "").lower()
        lost_date = request.POST.get("lost_date")

        found_desc = request.POST.get("found_desc", "").lower().split(";")
        found_cat = request.POST.get("found_cat", "").lower().split(";")
        found_date = request.POST.get("found_date", "").split(";")

        lost_words = lost_desc.split()

        for i in range(len(found_desc)):
            if i < len(found_cat) and i < len(found_date):
                if lost_cat == found_cat[i].strip():
                    if any(word in found_desc[i] for word in lost_words):
                        d1 = datetime.fromisoformat(lost_date)
                        d2 = datetime.fromisoformat(found_date[i].strip())

                        if abs((d1 - d2).days) <= 7:
                            matches.append({
                                "category": found_cat[i],
                                "date": found_date[i],
                                "description": found_desc[i]
                            })

    return render(request, "api/lostandfound.html", {
        "matches": matches,
        "searched": searched
    })

# ------------------------------
# Admin Dashboard
# ------------------------------
def admin_dashboard(request):
    if request.method == "POST":
        pdf = request.FILES.get("timetable_pdf")
        if pdf:
            return HttpResponse("Timetable PDF uploaded successfully")
    return render(request, "api/admin_dashboard.html")

# ------------------------------
# Know Your Teacher
# ------------------------------
def know_your_teacher(request):
    if request.method == "POST":
        year = request.POST.get("year")
        branch = request.POST.get("branch")
        section = request.POST.get("section")
        print(year, branch, section)
    return render(request, "api/know_your_teacher.html")

# ------------------------------
# Index / Home pages
# ------------------------------
def home(request):
    if request.method == "POST":
        year = request.POST.get("year")
        branch = request.POST.get("branch")
        semester = request.POST.get("semester")
        day = request.POST.get("day")
        print(year, branch, semester, day)
    return render(request, "api/home.html")

def about(request):
    return render(request, "api/about.html")

def faq(request):
    return render(request, "api/faq.html")

def login_view(request):
    return render(request, "api/login.html")

def register(request):
    return render(request, "api/register.html")

def complaint(request):
    return render(request, "api/complaint.html")

def know_teacher(request):
    return render(request, "api/know_your_teacher.html")

def lost_found(request):
    return render(request, "api/lostandfound.html")

# ------------------------------
# Simple Login API (No DRF)
# ------------------------------
def login_api(request):
    """
    Simple login API using POST method.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return JsonResponse({"error": "Username and password are required"}, status=400)

        user = authenticate(username=username, password=password)
        if user:
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)

    return JsonResponse({"error": "Invalid request"}, status=400)
