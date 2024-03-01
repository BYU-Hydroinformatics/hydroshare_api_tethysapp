from tethys_sdk.base import TethysAppBase


class HydrosharePython(TethysAppBase):
    """
    Tethys app class for Hydroshare library.
    """

    name = 'HydroShare Python API Demonstration'
    index = 'home'
    icon = 'hydroshare_python/images/icon.gif'
    package = 'hydroshare_python'
    root_url = 'hydroshare-python'
    color = '#008000'
    description = 'A web app to demonstrate the use of hs_restclient and generate operations available in the HydroShare website. This app is more of a tutorial and designed to educate a programmer to learn how Python APIs work.'
    tags = 'Python library, Hydroshare'
    enable_feedback = False
    feedback_emails = []