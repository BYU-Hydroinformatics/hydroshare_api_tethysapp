from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import TextInput, DatePicker
from tethys_services.backends.hs_restclient_helper import get_oauth_hs
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from hs_restclient import HydroShare, HydroShareAuthBasic
from hs_restclient.exceptions import HydroShareNotAuthorized, HydroShareHTTPException
from wsgiref.util import FileWrapper
import os
import tempfile
import zipfile
import json
from django.core import serializers
from tethys_sdk.routing import controller
import requests
import base64


@controller
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text="",
        name="save-button",
        icon="bi-floppy",
        style="success",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Save",
        },
    )

    edit_button = Button(
        display_text="",
        name="edit-button",
        icon="bi-pencil-square",
        style="warning",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Edit",
        },
    )

    remove_button = Button(
        display_text="",
        name="remove-button",
        icon="bi-dash-circle",
        style="danger",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Remove",
        },
    )

    previous_button = Button(
        display_text="Previous",
        name="previous-button",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Previous",
        },
    )

    next_button = Button(
        display_text="Next",
        name="next-button",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Next",
        },
    )

    context = {
        "save_button": save_button,
        "edit_button": edit_button,
        "remove_button": remove_button,
        "previous_button": previous_button,
        "next_button": next_button,
    }

    return render(request, "hydroshare_python/home.html", context)


@controller
def loading(request):
    return render(request, "hydroshare_python/loading.html")


@controller
def loading_geoserver_table(request):
    response_object = {}
    url = request.GET.get("url")
    # base64.b64decode

    response = requests.get(base64.b64decode(url).decode("ascii"))
    # breakpoint()
    response_object["content"] = response.content.decode("utf-8")
    return JsonResponse(response_object)


@controller
def tutorial(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text="",
        name="save-button",
        icon="bi-floppy",
        style="success",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Save",
        },
    )

    edit_button = Button(
        display_text="",
        name="edit-button",
        icon="bi-pencil-square",
        style="warning",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Edit",
        },
    )

    remove_button = Button(
        display_text="",
        name="remove-button",
        icon="bi-dash-circle",
        style="danger",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Remove",
        },
    )

    previous_button = Button(
        display_text="Previous",
        name="previous-button",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Previous",
        },
    )

    next_button = Button(
        display_text="Next",
        name="next-button",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Next",
        },
    )

    context = {
        "save_button": save_button,
        "edit_button": edit_button,
        "remove_button": remove_button,
        "previous_button": previous_button,
        "next_button": next_button,
    }

    return render(request, "hydroshare_python/tutorial.html", context)


@controller
def tethys(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text="",
        name="save-button",
        icon="bi-floppy",
        style="success",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Save",
        },
    )

    edit_button = Button(
        display_text="",
        name="edit-button",
        icon="bi-pencil-square",
        style="warning",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Edit",
        },
    )

    remove_button = Button(
        display_text="",
        name="remove-button",
        icon="bi-dash-circle",
        style="danger",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Remove",
        },
    )

    previous_button = Button(
        display_text="Previous",
        name="previous-button",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Previous",
        },
    )

    next_button = Button(
        display_text="Next",
        name="next-button",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Next",
        },
    )

    context = {
        "save_button": save_button,
        "edit_button": edit_button,
        "remove_button": remove_button,
        "previous_button": previous_button,
        "next_button": next_button,
    }

    return render(request, "hydroshare_python/tethys.html", context)


@controller
def featurespage(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text="",
        name="save-button",
        icon="bi-floppy",
        style="success",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Save",
        },
    )

    edit_button = Button(
        display_text="",
        name="edit-button",
        icon="bi-pencil-square",
        style="warning",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Edit",
        },
    )

    remove_button = Button(
        display_text="",
        name="remove-button",
        icon="bi-dash-circle",
        style="danger",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Remove",
        },
    )

    previous_button = Button(
        display_text="Previous",
        name="previous-button",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Previous",
        },
    )

    next_button = Button(
        display_text="Next",
        name="next-button",
        attributes={
            "data-bs-toggle": "tooltip",
            "data-bs-placement": "top",
            "title": "Next",
        },
    )

    context = {
        "save_button": save_button,
        "edit_button": edit_button,
        "remove_button": remove_button,
        "previous_button": previous_button,
        "next_button": next_button,
    }

    return render(request, "hydroshare_python/featurespage.html", context)


@controller
def mapview(request):
    """
    Controller for the app home page.
    """
    username = ""
    password = ""
    resourcev = []
    viewr = ""

    username_error = ""
    password_error = ""
    viewr_error = ""
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass
        # handle exceptions

    # Handle form submission
    print("POST REQUEST RECEIVED")
    if request.POST and not "add-button" in request.POST:
        print("POST REQUEST STARTED")
        # Get values
        has_errors = False
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        viewr = request.POST.get("viewr", None)

        # Validate

        if not viewr:
            has_errors = True
            viewr_error = "Subject is required."
        try:
            # pass in request object
            hs = get_oauth_hs(request)

            # # your logic goes here. For example: list all HydroShare resources
            # for resource in hs.getResourceList():
            #     print(resource)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                hs = HydroShare(auth=auth)

        if not has_errors:
            # Do stuff here
            # hs.setAccessRules(public=True)
            result = hs.resources(subject=viewr)

            resourceList = []
            for resource in result:
                resourceList.append(resource)

            return HttpResponse(json.dumps(resourceList))
            # return {"status": success }

        if has_errors:
            # Utah Municipal resource id
            messages.error(request, "Please fix errors.")

    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    viewr_input = TextInput(
        display_text="Subject", name="viewr", placeholder="Enter your subject"
    )

    add_button = Button(
        display_text="View on Map",
        name="add-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "username_input": username_input,
        "password_input": password_input,
        "viewr_input": viewr_input,
        "add_button": add_button,
        "cancel_button": cancel_button,
        "resourcev": resourcev,
    }

    return render(request, "hydroshare_python/mapview.html", context)


@controller
def boundingbox(request):
    """
    Controller for the app home page.
    """
    username = ""
    password = ""
    resourcev = []
    viewr = ""

    username_error = ""
    password_error = ""
    viewr_error = ""
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass

    # Handle form submission
    print("POST REQUEST RECEIVED")
    if request.POST and not "add-button" in request.POST:
        print("POST REQUEST STARTED")
        # Get values
        has_errors = False
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        viewr = request.POST.get("viewr", None)

        # Validate
        if not viewr:
            has_errors = True
            viewr_error = "Subject is required."

        try:
            # pass in request object
            hs = get_oauth_hs(request)

            # # your logic goes here. For example: list all HydroShare resources
            # for resource in hs.getResourceList():
            #     print(resource)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                hs = HydroShare(auth=auth)

        if not has_errors:
            # Do stuff here
            # auth = HydroShareAuthBasic(username= username, password= password)
            # hs = HydroShare(auth=auth)
            # hs.setAccessRules(public=True)
            result = hs.resources(subject=viewr)

            resourceList = []
            for resource in result:
                resourceList.append(resource)

            return HttpResponse(json.dumps(resourceList))
            # return {"status": success }

        if has_errors:
            # Utah Municipal resource id
            messages.error(request, "Please fix errors.")

    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    viewr_input = TextInput(
        display_text="Subject", name="viewr", placeholder="Enter your subject"
    )

    add_button = Button(
        display_text="View on Map",
        name="add-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "username_input": username_input,
        "password_input": password_input,
        "viewr_input": viewr_input,
        "add_button": add_button,
        "cancel_button": cancel_button,
        "resourcev": resourcev,
    }

    return render(request, "hydroshare_python/boundingbox.html", context)


def filtershapefile(in_num):

    return (
        in_num["file_name"].endswith(".shp")
        and in_num["logical_file_type"] == "GeoFeatureLogicalFile"
    )


@controller
def random(request):
    """
    Controller for the app home page.
    """
    # username = ''
    # password = ''

    # title = 'nyu_2451_34514'
    resource = request.GET.get("id", "")
    resourceid = "HS-" + resource

    auth = HydroShareAuthBasic(
        username="abhishekamal18@gmail.com", password="hydro1234"
    )
    hs = HydroShare(auth=auth)
    resource_md = hs.getSystemMetadata(resource)
    print(resource_md)
    # title = resource_md['title']
    bb1 = resource_md["coverages"][0]["value"]["northlimit"]
    bb2 = resource_md["coverages"][0]["value"]["eastlimit"]
    bb3 = resource_md["coverages"][0]["value"]["southlimit"]
    bb4 = resource_md["coverages"][0]["value"]["westlimit"]
    resourcefiles = hs.resource(resource).files.all().content

    print(resourcefiles)

    try:

        # Demonstrating filter() to remove odd numbers
        out_filter = filter(
            filtershapefile, json.loads(resourcefiles.decode("utf-8"))["results"]
        )
        # print(next(out_filter))
        title = next(out_filter, None)["url"].replace(".shp", "")
        titleindex = title.index("data/contents/")
        title = (
            title[title.find("data/contents/") :]
            .replace("data/contents/", "")
            .replace("/", " ")
        )

    except:
        title = " "

    reponse_obj = {
        "bb1": bb1,
        "bb2": bb2,
        "bb3": bb3,
        "bb4": bb4,
        "resourceid": resourceid,
        "title": title,
    }
    # print(context)

    # return render(request, "hydroshare_python/random.html", context)
    return JsonResponse(reponse_obj)


@controller
def geoserver(request):
    """
    Controller for the app home page.
    """
    username = ""
    password = ""
    resourcev = []
    viewr = ""
    bb1 = ""
    bb2 = ""
    bb3 = ""
    resourceid = ""

    username_error = ""
    password_error = ""
    viewr_error = ""
    bb1_error = ""
    bb2_error = ""
    bb3_error = ""
    bb4_error = ""
    resourceid_error = ""
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass

    # Handle form submission
    print("POST REQUEST RECEIVED")
    if request.POST and not "add-button" in request.POST:
        print("POST REQUEST STARTED")
        # Get values
        has_errors = False
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        viewr = request.POST.get("viewr", None)
        bb1 = request.POST.get("bb1", None)
        bb2 = request.POST.get("bb2", None)
        bb3 = request.POST.get("bb3", None)
        bb4 = request.POST.get("bb4", None)
        resourceid_error = request.POST.get("resourceid", None)
        # Validate

        if not viewr:
            has_errors = True
            viewr_error = "Subject is required."

        try:
            # pass in request object
            hs = get_oauth_hs(request)

            # # your logic goes here. For example: list all HydroShare resources
            # for resource in hs.getResourceList():
            #     print(resource)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                hs = HydroShare(auth=auth)

        if not bb1:
            has_errors = True
            bb1_error = "bb1 is required."

        if not bb2:
            has_errors = True
            bb2_error = "bb2 is required."

        if not bb3:
            has_errors = True
            bb3_error = "bb3 is required."

        if not bb4:
            has_errors = True
            bb4_error = "bb4 is required."

        if not resourceid:
            has_errors = True
            resourceid_error = "resourceid is required."

        if not has_errors:
            # Do stuff here
            # auth = HydroShareAuthBasic(username= username, password= password)
            # hs = HydroShare(auth=auth)
            # hs.setAccessRules(public=True)
            result = hs.resources(subject=viewr)

            resourceList = []
            for resource in result:
                resourceList.append(resource)

            return HttpResponse(json.dumps(resourceList))
            # return {"status": success }

        if has_errors:
            # Utah Municipal resource id
            messages.error(request, "Please fix errors.")

    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    bb1_input = TextInput(
        display_text="bb1",
        name="bb1",
        placeholder="Enter your bounding box co-ordinate 1",
    )
    bb2_input = TextInput(
        display_text="bb2",
        name="bb2",
        placeholder="Enter your bounding box co-ordinate 2",
    )
    bb3_input = TextInput(
        display_text="bb3",
        name="bb3",
        placeholder="Enter your bounding box co-ordinate 3",
    )
    bb4_input = TextInput(
        display_text="bb4",
        name="bb4",
        placeholder="Enter your bounding box co-ordinate 4",
    )
    resourceid_input = TextInput(
        display_text="Resource ID",
        name="resourceid",
        placeholder="Enter the resource id",
    )

    add_button = Button(
        display_text="View on Map",
        name="add-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "bb1_input": bb1_input,
        "bb2_input": bb2_input,
        "bb3_input": bb3_input,
        "bb4_input": bb4_input,
        "resourceid_input": resourceid_input,
        "username_input": username_input,
        "password_input": password_input,
        "add_button": add_button,
        "cancel_button": cancel_button,
        "resourcev": resourcev,
    }

    return redirect(request, "hydroshare_python/geoserver.html", context)


# def create_regions():


@controller
def get_file(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    title = ""
    owner = "Reclamation"
    username = ""
    password = ""
    date_built = ""
    author = ""

    # Errors
    title_error = ""
    owner_error = ""
    username_error = ""
    password_error = ""
    # river_error = ''
    date_error = ""
    author_error = ""
    loggedin = False
    # breakpoint()

    # Handle form submission
    if request.POST and "create-button" in request.POST:
        print(request.POST)
        # Get values
        has_errors = False
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        owner = request.POST.get("owner", None)
        # river = request.POST.get('river', None)
        date_built = request.POST.get("date-built", None)
        author = request.POST.get("author", None)
        coauthor = author.split(",")
        authorsObj = ""
        for i, author in enumerate(coauthor):
            separator = "," if i > 0 else ""
            authorsObj = (
                authorsObj + separator + '{"creator":{"name":"' + author.strip() + '"}}'
            )
        title = request.POST.get("title", None)
        print(dict(request.FILES))
        uploaded_file = request.FILES["uploadedfile"]
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_zip_path = os.path.join(temp_dir, uploaded_file.name)
            print(temp_zip_path)

            # Use with statements to ensure opened files are closed when done
            with open(temp_zip_path, "wb") as temp_zip:
                for chunk in uploaded_file.chunks():
                    temp_zip.write(chunk)

            # Validate
            if not title:
                has_errors = True
                title_error = "Title is required."

            if not owner:
                has_errors = True
                owner_error = "Owner is required."

            try:
                # pass in request object
                hs = get_oauth_hs(request)

            # your logic goes here. For example: list all HydroShare resources
            # for resource in hs.getResourceList():
            #     print(resource)

            except Exception as e:
                # handle exceptions

                if not username:
                    has_errors = True
                    username_error = "Username is required."

                elif not password:
                    has_errors = True
                    password_error = "Password is required."

                else:
                    auth = HydroShareAuthBasic(username=username, password=password)
                    hs = HydroShare(auth=auth)

            if not date_built:
                has_errors = True
                date_error = "Date Built is required."

            if not author:
                has_errors = True
                river_error = "Author is required."

            if not has_errors:
                # auth = HydroShareAuthBasic(username= username, password= password)
                # hs = HydroShare(auth=auth)
                abstract = date_built
                keywords = owner.split(", ")
                rtype = "CompositeResource"
                fpath = temp_zip_path  # fpath = 'tethysapp/geocode/workspaces/app_workspace/output.txt'
                metadata = (
                    '[{"coverage":{"type":"period", "value":{"start":"01/01/2000", "end":"12/12/2010"}}}, '
                    + authorsObj
                    + "]"
                )
                extra_metadata = '{"key-1": "value-1", "key-2": "value-2"}'
                # breakpoint()
                try:

                    hs.createResource(
                        rtype,
                        title,
                        resource_file=fpath,
                        keywords=keywords,
                        abstract=abstract,
                        metadata=metadata,
                        extra_metadata=extra_metadata,
                    )
                    messages.success(request, "Resource created successfully")

                except Exception as e:
                    messages.error(request, f"{e}")
                # return {"status": success }
            if has_errors:
                # Utah Municipal resource id
                messages.error(request, "Please fix errors.")

    # Define form gizmos
    title_input = TextInput(
        display_text="Title",
        name="title",
        placeholder="Enter the name of your resource",
    )

    owner_input = TextInput(
        display_text="Keywords",
        name="owner",
        placeholder="eg: shapefiles, datasets, etc..",
    )

    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    date_built = TextInput(
        display_text="Abstract",
        name="date-built",
        placeholder="Type in your abstract here",
    )

    author_input = TextInput(
        display_text="Author/Co-authors",
        name="author",
        placeholder="Enter the name of the Author and Co-authors",
    )

    create_button = Button(
        display_text="Create",
        name="create-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-resource-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )
    context = {
        "loggedin": loggedin,
        "title_input": title_input,
        "owner_input": owner_input,
        "username_input": username_input,
        "password_input": password_input,
        "date_built_input": date_built,
        "author_input": author_input,
        "create_button": create_button,
        "cancel_button": cancel_button,
    }
    print(context)

    return render(request, "hydroshare_python/get_file.html", context)


@controller
def add_file(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    username = ""
    password = ""
    resourcein = ""

    # Errors
    username_error = ""
    password_error = ""
    resourcein_error = ""
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass
        # handle exceptions

    # Handle form submission
    if request.POST and "add-button" in request.POST:
        # Get values
        has_errors = False
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        resourcein = request.POST.get("resourcein", None)
        print(dict(request.FILES))
        uploaded_file = request.FILES["addfile"]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_zip_path = os.path.join(temp_dir, uploaded_file.name)
            print(temp_zip_path)

            # Use with statements to ensure opened files are closed when done
            with open(temp_zip_path, "wb") as temp_zip:
                for chunk in uploaded_file.chunks():
                    temp_zip.write(chunk)

            # Validate
            try:
                # pass in request object
                hs = get_oauth_hs(request)

                # your logic goes here. For example: list all HydroShare resources
                # for resource in hs.getResourceList():
                #     print(resource)

            except Exception as e:
                # handle exceptions
                if not username:
                    has_errors = True
                    username_error = "Username is required."

                elif not password:
                    has_errors = True
                    password_error = "Password is required."

                else:
                    auth = HydroShareAuthBasic(username=username, password=password)
                    hs = HydroShare(auth=auth)

            if not resourcein:
                has_errors = True
                resourcein_error = "Resource is required."

            if not has_errors:
                fpath = temp_zip_path
                resource_id = hs.addResourceFile(resourcein, fpath)
                messages.success(request, "File added successfully")
            if has_errors:
                messages.error(request, "Please fix errors.")

    # Define form gizmos
    resourcein_input = TextInput(
        display_text="Resource ID",
        name="resourcein",
        placeholder="Enter id here eg: 08c6e88adaa647cd9bb28e5d619178e0 ",
    )

    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    add_button = Button(
        display_text="Add",
        name="add-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "resourcein_input": resourcein_input,
        "username_input": username_input,
        "password_input": password_input,
        "add_button": add_button,
        "cancel_button": cancel_button,
    }

    return render(request, "hydroshare_python/add_file.html", context)


@controller
def delete_resource(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    username = ""
    password = ""
    # filename = ''
    resourcein = ""
    # owner = 'Reclamation'
    # river = ''
    # date_built = ''

    # Errors
    username_error = ""
    password_error = ""
    # filename_error = ''
    resourcein_error = ""
    # owner_error = ''
    # river_error = ''
    # date_error = ''
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass
        # handle exceptions

    # Handle form submission
    if request.POST and "delete-button" in request.POST:
        # Get values
        has_errors = False
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        resourcein = request.POST.get("resourcein", None)

        # Validate

        if not resourcein:
            has_errors = True
            resourcein_error = "Resource ID is required."

        try:
            # pass in request object
            hs = get_oauth_hs(request)

            # your logic goes here. For example: list all HydroShare resources
            # for resource in hs.getResourceList():
            #     print(resource)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                hs = HydroShare(auth=auth)
        # if not river:
        #     has_errors = True
        #     river_error = 'River is required.'

        if not has_errors:
            # Do stuff here
            hs.deleteResource(resourcein)
            messages.success(request, "Resource deleted successfully")
        if has_errors:
            messages.error(request, "Please fix errors.")

    # Define form gizmos
    resourcein_input = TextInput(
        display_text="Resource ID",
        name="resourcein",
        placeholder="Enter the Resource ID here",
    )

    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    delete_button = Button(
        display_text="Delete Resource",
        name="delete-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "resourcein_input": resourcein_input,
        "username_input": username_input,
        "password_input": password_input,
        "delete_button": delete_button,
        "cancel_button": cancel_button,
    }

    return render(request, "hydroshare_python/delete_resource.html", context)


@controller
def filev(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    username = ""
    password = ""
    resourcein = ""

    # Handle form submission
    if request.POST:
        # Get values
        has_errors = False
        resourcein = request.POST.get("resourcein", None)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        try:
            # pass in request object
            hs = get_oauth_hs(request)

        except Exception as e:
            auth = HydroShareAuthBasic(username=username, password=password)
            hs = HydroShare(auth=auth)

            try:

                resourcefiles = hs.resource(resourcein).files.all()
                status_code = resourcefiles.__dict__.get("status_code")
                if status_code == 404:
                    messages.error(
                        request,
                        f"No Files found for the resource id: {resourcein}",
                    )
                    return redirect("hydroshare_python:getfile_metadata")
                else:
                    return HttpResponse(resourcefiles.content)

            # resource id is invalid
            except HydroShareNotAuthorized as e:
                print("here")
                messages.error(
                    request,
                    f"{e}",
                )
                return redirect("hydroshare_python:getfile_metadata")

            # authetication is invalid
            except HydroShareHTTPException as e:
                print("here22")

                messages.error(
                    request,
                    f"{json.loads(e.__dict__.get('status_msg','')).get('detail','No error')}",
                )
                return redirect("hydroshare_python:getfile_metadata")

        # return HttpResponse("")


@controller
def download_file(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    title = ""
    # filename = ''
    username = ""
    password = ""
    resourcein = ""
    filev = []
    # owner = 'Reclamation'
    # river = ''
    # date_built = ''

    # Errors
    title_error = ""
    # filename_error = ''
    resourcein_error = ""
    username_error = ""
    password_error = ""
    # date_error = ''
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass

    # Handle form submission
    if request.POST and "download-button" in request.POST:
        # Get values
        has_errors = False
        # filename = request.POST.get('filename', None)
        resourcein = request.POST.get("resourcein", None)
        title = request.POST.get("title_input", None)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        # Validate

        if not resourcein:
            has_errors = True
            resourcein_error = "Resource ID is required."

        if not title:
            has_errors = True
            title_error = "Title is required."

        try:
            # pass in request object
            hs = get_oauth_hs(request)

            # your logic goes here. For example: list all HydroShare resources
            # for resource in hs.getResourceList():
            #     print(resource)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                hs = HydroShare(auth=auth)

        # if not river:
        #     has_errors = True
        #     river_error = 'River is required.'

        if not has_errors:
            # Do stuff here
            # auth = HydroShareAuthBasic(username= username, password= password)
            # hs = HydroShare(auth=auth)
            fname = title
            fpath = hs.getResourceFile(resourcein, fname, destination="/tmp")
            # response = HttpResponse( content_type='application/force-download')
            # response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(fname)
            # response['X-Sendfile'] = smart_str('/tmp')
            # return response
            fpath = "/tmp/%s" % title
            # hs.getResource(title, destination='/tmp')
            # response = HttpResponse( content_type='application/force-download')
            # response['Content-Disposition'] = 'attachment; filename=%s.zip' % smart_str(title)
            # response['X-Sendfile'] = smart_str('/tmp')
            # response['Content-Length'] = os.path.getsize(fpath)
            # print(os.path.getsize(fpath))

            wrapper = FileWrapper(open(os.path.abspath(fpath), "rb"))
            response = HttpResponse(wrapper, content_type="text/plain")
            response["Content-Disposition"] = (
                "attachment; filename=%s" % os.path.basename(fpath)
            )
            response["Content-Length"] = os.path.getsize(fpath)
            return response
        if has_errors:
            # Utah Municipal resource id
            messages.error(request, "Please fix errors.")

    # Define form gizmos
    resourcein_input = TextInput(display_text="Resource ID", name="resourcein")

    title_input = TextInput(
        display_text="Name of the file you want to download including the extension",
        name="title",
        placeholder="eg: filename.shp or filename.txt",
    )

    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    add_button = Button(
        display_text="Download",
        name="download-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "resourcein_input": resourcein_input,
        "title_input": title_input,
        "username_input": username_input,
        "password_input": password_input,
        "add_button": add_button,
        "cancel_button": cancel_button,
        "filev": filev,
    }

    return render(request, "hydroshare_python/download_file.html", context)


@controller
def delete_file(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    title = ""
    # filename = ''
    username = ""
    password = ""
    resourcein = ""
    filev = []
    # owner = 'Reclamation'
    # river = ''
    # date_built = ''

    # Errors
    title_error = ""
    # filename_error = ''
    resourcein_error = ""
    username_error = ""
    password_error = ""
    # date_error = ''
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass
        # handle exceptions

    # Handle form submission
    if request.POST and "delete-button" in request.POST:
        # Get values
        has_errors = False
        # filename = request.POST.get('filename', None)
        resourcein = request.POST.get("resourcein", None)
        title = request.POST.get("title_input", None)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        # Validate

        if not resourcein:
            has_errors = True
            resourcein_error = "Resource ID is required."

        try:
            # pass in request object
            hs = get_oauth_hs(request)

            # your logic goes here. For example: list all HydroShare resources
            # for resource in hs.getResourceList():
            #     print(resource)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                hs = HydroShare(auth=auth)

        # if not river:
        #     has_errors = True
        #     river_error = 'River is required.'

        if not has_errors:
            # Do stuff here
            # auth = HydroShareAuthBasic(username= username, password= password)
            # hs = HydroShare(auth=auth)
            resource_id = hs.deleteResourceFile(resourcein, title)
            messages.success(request, "File deleted successfully")
        if has_errors:
            # Utah Municipal resource id
            messages.error(request, "Please fix errors.")

    # Define form gizmos
    resourcein_input = TextInput(
        display_text="Resource ID",
        name="resourcein",
        placeholder="Enter the Resource ID here",
    )

    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    delete_button = Button(
        display_text="Delete File",
        name="delete-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "resourcein_input": resourcein_input,
        "username_input": username_input,
        "password_input": password_input,
        "delete_button": delete_button,
        "cancel_button": cancel_button,
        "filev": filev,
    }

    return render(request, "hydroshare_python/delete_file.html", context)


@controller
def getfile_metadata(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    title = ""
    # filename = ''
    username = ""
    password = ""
    resourcein = ""
    filev = []

    # Errors
    title_error = ""
    # filename_error = ''
    resourcein_error = ""
    username_error = ""
    password_error = ""
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass
        # handle exceptions

    # Handle form submission
    if request.POST:
        # Get values
        has_errors = False
        # filename = request.POST.get('filename', None)
        resourcein = request.POST.get("resourcein", None)
        title = request.POST.get("title_input", None)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        # Validate

        if not resourcein:
            has_errors = True
            resourcein_error = "Resource ID is required."

        if not title:
            has_errors = True
            title_error = "Title is required."

        try:
            # pass in request object
            hs = get_oauth_hs(request)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                hs = HydroShare(auth=auth)

        if not has_errors:
            # Do stuff here
            try:
                response = hs.resource(resourcein).files.metadata(title).content

            # resource id is invalid
            except HydroShareNotAuthorized as e:
                messages.error(
                    request,
                    f"{e}",
                )
            # authetication is invalid
            except HydroShareHTTPException as e:
                messages.error(
                    request,
                    f"{json.loads(e.__dict__.get('status_msg','')).get('detail','No error')}",
                )

            return HttpResponse(response.decode("utf-8"))

        if has_errors:
            # Utah Municipal resource id
            messages.error(request, "Please fix errors.")

    # Define form gizmos
    resourcein_input = TextInput(
        display_text="Resource ID", name="resourcein", error=resourcein_error
    )

    title_input = TextInput(
        display_text="Name of the file you want to download including the extension",
        name="title",
        placeholder="eg: filename.shp or filename.txt",
        error=title_error,
    )

    username_input = TextInput(
        display_text="Username",
        name="username",
        placeholder="Enter your username",
        error=username_error,
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
        error=password_error,
    )

    add_button = Button(
        display_text="Download",
        name="download-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "resourcein_input": resourcein_input,
        "title_input": title_input,
        "username_input": username_input,
        "password_input": password_input,
        "add_button": add_button,
        "cancel_button": cancel_button,
        "filev": filev,
    }

    return render(request, "hydroshare_python/getfile_metadata.html", context)


@controller
def metadata(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    username = ""
    password = ""
    creator1 = ""
    creator2 = ""
    organization = ""
    Email = ""
    Address = ""
    Phone = ""
    detail1 = ""
    detail2 = ""
    resourcein = ""

    # Errors
    username_error = ""
    password_error = ""
    # filename_error = ''
    resourcein_error = ""
    creator1_error = ""
    creator2_error = ""
    organization_error = ""
    Email_error = ""
    Address_error = ""
    Phone_error = ""
    detail1_error = ""
    detail2_error = ""
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass

    # Handle form submission
    if request.POST and "add-button" in request.POST:
        # Get values
        has_errors = False
        # filename = request.POST.get('filename', None)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        creator1 = request.POST.get("creator1", None)
        creator2 = request.POST.get("creator2", None)
        coauthor = creator2.split(",")
        organization = request.POST.get("organization", None)
        Email = request.POST.get("Email", None)
        Address = request.POST.get("Address", None)
        Phone = request.POST.get("Phone", None)
        detail1 = request.POST.get("detail1", None)
        detail2 = request.POST.get("detail2", None)
        resourcein = request.POST.get("resourcein", None)

        # Validate
        if not creator1:
            has_errors = True
            creator1_error = "creator1 is required."

        try:
            # pass in request object
            hs = get_oauth_hs(request)

        except Exception as e:
            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                try:
                    hs = HydroShare(auth=auth)
                except Exception as e:
                    has_errors = True
                    messages.error(request, f"{e}")

        if not organization:
            has_errors = True
            password_error = "organization is required."

        if not Email:
            has_errors = True
            Email_error = "Email is required."

        if not Address:
            has_errors = True
            Address_error = "Address is required."

        if not Phone:
            has_errors = True
            Phone_error = "Phone is required."

        if not detail1:
            has_errors = True
            detail1_error = "detail1 is required."

        if not detail2:
            has_errors = True
            detail2_error = "detail2 is required."

        if not resourcein:
            has_errors = True
            resourcein_error = "Resource is required."

        if not has_errors:
            metadata = {
                "coverages": [
                    {"type": "period", "value": {"start": detail1, "end": detail2}}
                ],
                "creators": [
                    {
                        "name": creator1,
                        "organization": organization,
                        "email": Email,
                        "address": Address,
                        "phone": Phone,
                    },
                ],
            }

            for i, author in enumerate(coauthor):
                metadata["creators"].append({"name": author.strip()})

            try:
                hs.updateScienceMetadata(resourcein, metadata=metadata)
                messages.success(request, "Metadata added successfully")

            # resource id is invalid
            except HydroShareNotAuthorized as e:
                messages.error(
                    request,
                    f"{e}",
                )
            # authetication is invalid
            except HydroShareHTTPException as e:
                messages.error(
                    request,
                    f"{json.loads(e.__dict__.get('status_msg','')).get('detail','No error')}",
                )

        if has_errors:
            messages.error(request, "Please fix errors.")

    # Define form gizmos
    resourcein_input = TextInput(
        display_text="Resource ID",
        name="resourcein",
        placeholder="Enter id here eg: 08c6e88adaa647cd9bb28e5d619178e0 ",
        error=resourcein_error,
    )

    username_input = TextInput(
        display_text="Username",
        name="username",
        placeholder="Enter your username",
        error=username_error,
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
        error=password_error,
    )

    creator1_input = TextInput(
        display_text="Author(s) and/ or Chief Contributor(s)",
        name="creator1",
        placeholder="Enter the name of the Author(s) and/ or Chief Contributor(s)",
        error=creator1_error,
    )

    creator2_input = TextInput(
        display_text="Co-authors",
        name="creator2",
        placeholder="Enter the name of other contributors to the resource",
        error=creator2_error,
    )

    organization_input = TextInput(
        display_text="Organization",
        name="organization",
        placeholder="Enter your organization",
        error=organization_error,
    )

    Email_input = TextInput(
        display_text="Email",
        name="Email",
        placeholder="Enter your Email",
        error=Email_error,
    )

    Address_input = TextInput(
        display_text="Address",
        name="Address",
        placeholder="Enter your Address",
        error=Address_error,
    )

    Phone_input = TextInput(
        display_text="Phone",
        name="Phone",
        placeholder="Enter your Phone",
        error=Phone_error,
    )

    detail1_input = DatePicker(
        name="detail1",
        display_text="Start date",
        autoclose=True,
        format="MM d, yyyy",
        start_view="decade",
        today_button=True,
        initial=detail1,
        error=detail1_error,
    )

    detail2_input = DatePicker(
        name="detail2",
        display_text="End date",
        autoclose=True,
        format="MM d, yyyy",
        start_view="decade",
        today_button=True,
        initial=detail2,
        error=detail2_error,
    )

    add_button = Button(
        display_text="Submit",
        name="add-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "resourcein_input": resourcein_input,
        "username_input": username_input,
        "password_input": password_input,
        "creator1_input": creator1_input,
        "creator2_input": creator2_input,
        "organization_input": organization_input,
        "Email_input": Email_input,
        "Address_input": Address_input,
        "Phone_input": Phone_input,
        "detail1_input": detail1_input,
        "detail2_input": detail2_input,
        "add_button": add_button,
        "cancel_button": cancel_button,
    }

    return render(request, "hydroshare_python/metadata.html", context)


@controller
def viewer(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values

    username = ""
    password = ""
    viewr = ""

    # Errors
    username_error = ""
    password_error = ""
    viewr_error = ""
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass

    # Handle form submission
    if request.POST and not "fetch_button" in request.POST:
        print("POST REQUEST STARTED")
        # Get values
        has_errors = False
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        password = request.POST.get("password", None)
        viewr = request.POST.get("viewr", None)

        # Validate
        #
        if not viewr:
            has_errors = True
            viewr_error = "Subject is required."
        try:
            # pass in request object
            hs = get_oauth_hs(request)

        # # your logic goes here. For example: list all HydroShare resources
        #     for resource in hs.getResourceList():
        #         print(resource)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."
                messages.error(request, username_error)
            if not password:
                has_errors = True
                password_error = "Password is required."

            auth = HydroShareAuthBasic(username=username, password=password)
            hs = HydroShare(auth=auth)

        if not has_errors:
            # Do stuff here

            result = hs.resources(subject=viewr)

            resourceList = []
            for resource in result:
                resourceList.append(resource)

            return HttpResponse(json.dumps(resourceList))

        if has_errors:
            print("hey")
            messages.error(request, "Please fix errors.")

    username_input = TextInput(
        display_text="Username",
        name="username",
        placeholder="Enter your username",
        error=username_error,
    )

    viewr_input = TextInput(
        display_text="Subject",
        name="viewr",
        placeholder="Enter your subject",
        error=viewr_error,
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
        error=password_error,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "username_input": username_input,
        "password_input": password_input,
        "viewr_input": viewr_input,
        "cancel_button": cancel_button,
    }

    return render(request, "hydroshare_python/find_resource.html", context)


@controller
def download_resource(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    title = ""
    username = ""
    password = ""

    # Errors
    title_error = ""
    username_error = ""
    password_error = ""
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass

    # Handle form submission
    if request.POST and "download-button" in request.POST:
        # Get values
        has_errors = False
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        title = request.POST.get("title", None)

        # Validate
        if not title:
            has_errors = True
            title_error = "Title is required."

        try:
            # pass in request object
            hs = get_oauth_hs(request)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                hs = HydroShare(auth=auth)

        if not has_errors:

            fpath = "/tmp/%s.zip" % title
            hs.getResource(title, destination="/tmp")
            wrapper = FileWrapper(open(os.path.abspath(fpath), "rb"))
            response = HttpResponse(wrapper, content_type="text/plain")
            response["Content-Disposition"] = (
                "attachment; filename=%s" % os.path.basename(fpath)
            )
            response["Content-Length"] = os.path.getsize(fpath)
            return response
            # hs.setAccessRules(public=True)

        if has_errors:
            # Utah Municipal resource id
            messages.error(request, "Please fix errors.")

    # Define form gizmos
    title_input = TextInput(
        display_text="Enter your resource ID of the Resource",
        name="title",
        placeholder="Ex: decbdccf486d4df4b1d18031a4e63aa3",
    )

    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    # river_input = TextInput(
    #     display_text='Name of Creator',
    #     name='river',
    #     placeholder='e.g: John Smith'
    # )

    download_button = Button(
        display_text="Download",
        name="download-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "title_input": title_input,
        "username_input": username_input,
        "password_input": password_input,
        "download_button": download_button,
        "cancel_button": cancel_button,
    }

    return render(request, "hydroshare_python/download_resource.html", context)


@controller
def create_folder(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    username = ""
    password = ""
    # river = ''
    resourcein = ""
    foldername = ""

    # Errors
    username_error = ""
    password_error = ""
    # river_error = ''
    resourcein_error = ""
    foldername_error = ""
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass

    # Handle form submission
    if request.POST and "create-button" in request.POST:
        # Get values
        has_errors = False
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # river = request.POST.get('river', None)
        resourcein = request.POST.get("resourcein", None)
        foldername = request.POST.get("foldername", None)

        # Validate
        if not resourcein:
            has_errors = True
            resourcein_error = "resourcein is required."

        try:
            # pass in request object
            hs = get_oauth_hs(request)

        # # your logic goes here. For example: list all HydroShare resources
        #     for resource in hs.getResourceList():
        #         print(resource)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                hs = HydroShare(auth=auth)

        if not foldername:
            has_errors = True
            foldername_error = "Folder name is required."

        if not has_errors:
            # Do stuff here
            # auth = HydroShareAuthBasic(username= username, password= password)
            # hs = HydroShare(auth=auth)
            folder_to_create = foldername
            response_json = hs.createResourceFolder(
                resourcein, pathname=folder_to_create
            )
            messages.success(request, "Folder created successfully")
        if has_errors:
            messages.error(request, "Please fix errors.")

    # Define form gizmos
    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    foldername_input = TextInput(
        display_text="Name of the Folder",
        name="foldername",
        placeholder="Enter the name of the folder",
    )

    resourcein_input = TextInput(
        display_text="Resource ID",
        name="resourcein",
        placeholder="Enter the Resource ID",
    )

    create_button = Button(
        display_text="Create Folder",
        name="create-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "username_input": username_input,
        "password_input": password_input,
        "resourcein_input": resourcein_input,
        "create_button": create_button,
        "cancel_button": cancel_button,
        "foldername_input": foldername_input,
    }

    return render(request, "hydroshare_python/create_folder.html", context)


@controller
def deletefolder(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    username = ""
    password = ""
    # river = ''
    resourcein = ""
    foldername = ""

    # Errors
    username_error = ""
    password_error = ""
    # river_error = ''
    resourcein_error = ""
    foldername_error = ""
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass

    # Handle form submission
    if request.POST and "create-button" in request.POST:
        # Get values
        has_errors = False
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # river = request.POST.get('river', None)
        resourcein = request.POST.get("resourcein", None)
        foldername = request.POST.get("foldername", None)

        # Validate
        if not resourcein:
            has_errors = True
            resourcein_error = "resourcein is required."

        try:
            # pass in request object
            hs = get_oauth_hs(request)

        # your logic goes here. For example: list all HydroShare resources
        # for resource in hs.getResourceList():
        #     print(resource)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                hs = HydroShare(auth=auth)

        if not foldername:
            has_errors = True
            foldername_error = "Folder name is required."

        if not has_errors:
            # Do stuff here
            # auth = HydroShareAuthBasic(username= username, password= password)
            # hs = HydroShare(auth=auth)
            folder_to_create = foldername
            response_json = hs.deleteResourceFolder(
                resourcein, pathname=folder_to_create
            )
            messages.success(request, "Folder deleted successfully")
        if has_errors:
            messages.error(request, "Please fix errors.")

    # Define form gizmos
    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    foldername_input = TextInput(
        display_text="Name of the Folder",
        name="foldername",
        placeholder="Enter the name of the folder",
    )

    resourcein_input = TextInput(
        display_text="Resource ID",
        name="resourcein",
        placeholder="Enter the Resource ID",
    )

    create_button = Button(
        display_text="Delete Folder",
        name="create-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "username_input": username_input,
        "password_input": password_input,
        "resourcein_input": resourcein_input,
        "create_button": create_button,
        "cancel_button": cancel_button,
        "foldername_input": foldername_input,
    }

    return render(request, "hydroshare_python/deletefolder.html", context)


@controller
def change_public(request):
    """
    Controller for the Add Dam page.
    """
    # Default Values
    title = ""
    username = ""
    password = ""

    # Errors
    title_error = ""
    username_error = ""
    password_error = ""
    loggedin = False
    try:
        # pass in request object
        hs = get_oauth_hs(request)
        loggedin = True

    except Exception as e:
        pass

    # Handle form submission
    if request.POST and "public-button" in request.POST:
        # Get values
        has_errors = False
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        title = request.POST.get("title", None)

        # Validate
        if not title:
            has_errors = True
            title_error = "Title is required."

        try:
            # pass in request object
            hs = get_oauth_hs(request)

        # your logic goes here. For example: list all HydroShare resources
        # for resource in hs.getResourceList():
        #     print(resource)

        except Exception as e:
            # handle exceptions

            if not username:
                has_errors = True
                username_error = "Username is required."

            elif not password:
                has_errors = True
                password_error = "Password is required."

            else:
                auth = HydroShareAuthBasic(username=username, password=password)
                hs = HydroShare(auth=auth)

        if not has_errors:
            # Do stuff here
            # auth = HydroShareAuthBasic(username= username, password= password)
            # hs = HydroShare(auth=auth)
            hs.setAccessRules(title, public=True)
            messages.success(request, "Resource is now public")
            # hs.setAccessRules(public=True)

        if has_errors:
            # Utah Municipal resource id
            messages.error(request, "Please fix errors.")

    # Define form gizmos
    title_input = TextInput(
        display_text="Enter your resource ID of the Resource",
        name="title",
        placeholder="Ex: decbdccf486d4df4b1d18031a4e63aa3",
    )

    username_input = TextInput(
        display_text="Username", name="username", placeholder="Enter your username"
    )

    password_input = TextInput(
        display_text="Password",
        name="password",
        attributes={"type": "password"},
        placeholder="Enter your password",
    )

    # river_input = TextInput(
    #     display_text='Name of Creator',
    #     name='river',
    #     placeholder='e.g: John Smith'
    # )

    public_button = Button(
        display_text="Change to Public",
        name="public-button",
        icon="bi-plus",
        style="success",
        attributes={"form": "add-dam-form"},
        submit=True,
    )

    cancel_button = Button(
        display_text="Cancel",
        name="cancel-button",
        href=reverse("hydroshare_python:home"),
    )

    context = {
        "loggedin": loggedin,
        "title_input": title_input,
        "username_input": username_input,
        "password_input": password_input,
        "public_button": public_button,
        "cancel_button": cancel_button,
    }

    return render(request, "hydroshare_python/change_public.html", context)
