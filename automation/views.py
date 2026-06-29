import os
import time
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from core.orchestrator import run
from core.publisher import publish_content
from django.http import (HttpResponse,JsonResponse)
from bson import ObjectId
from integrations.mongodb import ( get_gridfs,save_user_feedback)
from integrations.media_storage import (upload_image, upload_video)
from automation.image_helper import prepare_instagram_image
from integrations.cloudinary_storage import (upload_image_to_cloudinary,upload_video_to_cloudinary)
from django.contrib import messages
from feedback.regenerate import regenerate_content


def home(request):

    if request.method == "POST":

        topic = request.POST.get("topic", "").strip()

        image = request.FILES.get("image")
        video = request.FILES.get("video")
        # ---------------------------------
        #  Available Platforms
        # ---------------------------------

        available_platforms = []
        if video:
            available_platforms = [
                "Instagram",
                "YouTube",
                "TikTok",
                "Facebook",
                "LinkedIn"
            ]

        elif image:
            available_platforms = [
                "Instagram",
                "Facebook",
                "LinkedIn",
                "Twitter",
                "Threads",
                "Reddit",
                "Telegram",
                "Bluesky"
            ]
        else:
            available_platforms = [
                "LinkedIn",
                "Facebook",
                "Twitter",
                "Threads",
                "Reddit",
                "Telegram",
                "Bluesky",
            ]     



        image_path = None

        if image:

            fs = FileSystemStorage()

            filename = fs.save(image.name, image)
            print("=" * 80)
            print("UPLOADED FILENAME :", filename)
            print("=" * 80)
            
            image_path = fs.path(filename)
            # Convert image into Instagram-compatible JPEG
            image_path = prepare_instagram_image(image_path)
            print("=" * 80)
            print("INSTAGRAM IMAGE PATH :", image_path)
            print("=" * 80)
            with open(image_path, "rb") as f:
                class UploadedFile:
                    pass
                mongo_file = UploadedFile()
                # Use converted JPEG filename
                mongo_file.name = os.path.basename(image_path)
                mongo_file.content_type = "image/jpeg"
                mongo_file.read = lambda: f.read()
                mongo_file_id = upload_image(mongo_file)
                print("=" * 80)
                print("Mongo File ID :", mongo_file_id)
                print("=" * 80)
            # Save MongoDB file id
            request.session["mongo_file_id"] = mongo_file_id  
            # Temporary image URL (we'll improve this later)
            cloudinary_image_url = upload_image_to_cloudinary(image_path)
            request.session["image_url"] = cloudinary_image_url
            print("=" * 80)
            print("CLOUDINARY IMAGE URL")
            print(cloudinary_image_url)
            print("=" * 80)
        else:
            request.session["image_url"] = ""
            request.session["mongo_file_id"] = ""
            image_path = None
        result = run(
            topic=topic,
            image_path=image_path
        )

 

        video_path = None 
        if video:
            fs = FileSystemStorage()
            filename = fs.save(video.name, video)
            video_path = fs.path(filename)
            with open(video_path, "rb") as f:
                class UploadedFile:
                    pass
                mongo_file = UploadedFile()
                mongo_file.name = filename
                mongo_file.content_type = video.content_type
                mongo_file.read = lambda: f.read()
                mongo_file_id = upload_video(mongo_file)
                print("=" * 80)
                print("Mongo Video ID :", mongo_file_id)
                print("=" * 80)
            request.session["mongo_video_id"] = mongo_file_id
            cloudinary_video_url = upload_video_to_cloudinary(video_path)
            request.session["video_url"] = cloudinary_video_url
            print("=" * 80)
            print("CLOUDINARY VIDEO URL")
            print(cloudinary_video_url)
            print("=" * 80) 
        else:
            request.session["video_url"] = ""
            request.session["mongo_video_id"] = ""
            
        request.session["article"] = result["article"]
        request.session["caption"] = result["caption"]
        request.session["hashtags"] = result["hashtags"]
        request.session["platforms"] = result["platform_content"]
        request.session["validation"] = result["validation"]
        request.session["topic"] = topic
        request.session["available_platforms"] = available_platforms

        return redirect("preview")    
    context = {
        "popup_title": request.session.pop(
            "popup_title",""
        ),
        "popup_icon": request.session.pop(
            "popup_icon",""
        ),
        "popup_message": request.session.pop(
            "popup_message",""
        ),
    }

    return render(request, "home.html",context)


def preview(request):

    if request.method == "POST":

        action = request.POST.get("action")
        selected_platforms = request.POST.getlist("platforms")

        # -------------------------------------------------
        # REGENERATE CONTENT
        # -------------------------------------------------

        if action == "regenerate":

            feedback = request.POST.get("feedback", "").strip()

            if feedback:

                regenerated = regenerate_content(
                    topic=request.session.get("topic"),
                    article=request.session.get("article"),
                    caption=request.session.get("caption"),
                    hashtags=request.session.get("hashtags"),
                    feedback=feedback
                )

                if regenerated.get("article"):
                    request.session["article"] = regenerated["article"]

                if regenerated.get("caption"):
                    request.session["caption"] = regenerated["caption"]

                if regenerated.get("hashtags"):
                    request.session["hashtags"] = regenerated["hashtags"]

                request.session["feedback"] = ""

            return redirect("preview")

        # -------------------------------------------------
        # PUBLISH CONTENT
        # -------------------------------------------------

        start = time.time()

        response = publish_content(
            article=request.session.get("article"),
            caption=request.session.get("caption"),
            hashtags=request.session.get("hashtags"),
            image=request.session.get("image_url"),
            video=request.session.get("video_url"),
            selected_platforms=selected_platforms,
        )

        end = time.time()

        print("=" * 80)
        print(f"PUBLISH TOOK: {end - start:.2f} seconds")
        print("=" * 80)

        success = True
        message = ""

        for platform, result in response.items():

            if result["status"] == "success":

                message += (
                    f"✅ {platform.title()} published successfully.<br>"
                )

            else:

                success = False

                message += (
                    f"❌ <b>{platform.title()}</b><br>"
                    f"{result['message']}<br><br>"
                )

        request.session["popup_title"] = (
            "Publishing Completed"
            if success
            else "Publishing Failed"
        )

        request.session["popup_icon"] = (
            "success"
            if success
            else "error"
        )

        request.session["popup_message"] = message

        return redirect("home")

    context = {

        "available_platforms": request.session.get(
            "available_platforms",
            []
        ),

        "article": request.session.get(
            "article",
            ""
        ),

        "caption": request.session.get(
            "caption",
            ""
        ),

        "hashtags": request.session.get(
            "hashtags",
            ""
        ),

        "feedback": request.session.pop(
            "feedback",
            ""
        ),

        "platforms": request.session.get(
            "platforms",
            {}
        ),

        "validation": request.session.get(
            "validation",
            {}
        ),

        "topic": request.session.get(
            "topic",
            ""
        ),

        "image_url": request.session.get(
            "image_url",
            ""
        ),

        "video_url": request.session.get(
            "video_url",
            ""
        ),

    }

    return render(
        request,
        "preview.html",
        context
    )

def serve_media(request, file_id):

    print("=" * 80)
    print("FILE ID RECEIVED :", repr(file_id))
    print("=" * 80)

    fs = get_gridfs()

    try:
        file = fs.get(ObjectId(file_id))

        print("FOUND FILE")
        print("Filename:", file.filename)
        print("Content-Type:", file.content_type)
        print("=" * 80)

        response = HttpResponse(
            file.read(),
            content_type=file.content_type
        )

        response["Content-Disposition"] = f'inline; filename="{file.filename}"'
        response["Cache-Control"] = "public, max-age=86400"
        response["Accept-Ranges"] = "bytes"

        return response

    except Exception as e:

        print("=" * 80)
        print("GRIDFS ERROR")
        print(e)
        print("=" * 80)

        return HttpResponse(
            str(e),
            status=404
        )
    

from django.http import JsonResponse


def submit_feedback(request):

    if request.method == "POST":

        rating = request.POST.get("rating")
        feedback = request.POST.get("feedback")

        if not rating or not feedback:

            return JsonResponse({
                "status": "error",
                "message": "Please provide both rating and feedback."
            })

        try:

            save_user_feedback(
                rating=rating,
                feedback=feedback
            )

            return JsonResponse({
                "status": "success",
                "message": "Thank you for your feedback!"
            })

        except Exception as e:

            print(e)

            return JsonResponse({
                "status": "error",
                "message": "Unable to save feedback."
            })

    return JsonResponse({
        "status": "error",
        "message": "Invalid request."
    })