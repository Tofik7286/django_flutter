from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from django.contrib import messages


@api_view(['POST'])
def signup(request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user = user_serializer.save()

        UserProfile.objects.create(user=user, gender=request.data.get(
            'gender', 'O'), hobbies=request.data.get('hobbies', ''))

        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])  
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user:
        profile = UserProfile.objects.get(user=user)
        return Response(UserProfileSerializer(profile).data, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
def get_profile(request, user_id):
    try:
        profile = UserProfile.objects.get(user_id=user_id)
        return Response(UserProfileSerializer(profile).data)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)




@api_view(['PUT'])
def update_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        profile = UserProfile.objects.get(user=user)
    except (User.DoesNotExist, UserProfile.DoesNotExist):
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    user_serializer = UserSerializer(user, data=request.data, partial=True)
    profile_serializer = UserProfileSerializer(
        profile, data=request.data, partial=True)

    if user_serializer.is_valid() and profile_serializer.is_valid():
        user_serializer.save()
        profile_serializer.save()
        return Response(profile_serializer.data)

    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)






def user_list_view(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})



def user_create_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        hobbies = request.POST.get('hobbies')
        profile_pic = request.FILES.get('profile_pic')

        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Choose another!")
            return redirect('user_create')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('user_create')

        
        user = User.objects.create_user(
            username=username, password=password, first_name=first_name, last_name=last_name, email=email)

        UserProfile.objects.create(
            user=user, gender=gender, hobbies=hobbies, profile_pic=profile_pic)

        messages.success(request, "User created successfully!")
        return redirect('user_list')

    return render(request, 'user_create.html')




def user_update_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile, created = UserProfile.objects.get_or_create(
        user=user)  

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        profile.gender = request.POST.get('gender')
        profile.hobbies = request.POST.get('hobbies')

        
        if request.FILES.get('profile_pic'):
            profile.profile_pic = request.FILES.get('profile_pic')

        user.save()
        profile.save()

        messages.success(request, "User updated successfully!")
        return redirect('user_list')

    return render(request, 'user_update.html', {'user': user, 'profile': profile})



def user_delete_view(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect('user_list')

    return render(request, 'user_delete.html', {'user': user})
