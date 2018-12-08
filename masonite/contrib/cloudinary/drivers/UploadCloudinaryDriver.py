"""Cloudinary Upload Driver"""

from masonite.contracts import UploadContract
from masonite.drivers import BaseUploadDriver
from masonite.exceptions import DriverLibraryNotFound
from masonite.helpers import random_string
from masonite.managers import UploadManager

from config import storage


class UploadCloudinaryDriver(BaseUploadDriver, UploadContract):

    def __init__(self, upload: UploadManager):
        """Upload Cloudinary Driver Constructor

        Arguments:
            UploadManager {masonite.managers.UploadManager} -- The Upload Manager object.
        """

        self.upload = upload
        self.config = storage

    def store(self, fileitem, location=None): 
        """Store the file into Cloudinary.

        Arguments:
            fileitem {cgi.Storage} -- Storage object.
        Keyword Arguments:
            location {string} -- The location on disk you would like to store the file. (default: {None})
        Raises:
            DriverLibraryNotFound -- Raises when the cloudinary library is not installed.
        Returns:
            dict -- Returns the dict object of cloudinary api response.
        """

        try:
            import cloudinary
            import cloudinary.uploader
        except ImportError:
            raise DriverLibraryNotFound("Could not find the 'cloudinary' driver")

        cloudinary.config(
            cloud_name=self.config.DRIVERS['cloudinary']['cloud_name'],
            api_key=self.config.DRIVERS['cloudinary']['api_key'],
            api_secret=self.config.DRIVERS['cloudinary']['secret'],
        )

        response = cloudinary.uploader.upload(
            fileitem.file.read(),
            folder=location,
        )
        return response

    def store_prepend(self, fileitem, prepend, location=None):
        """Store the file onto the Cloudinary but with a prepended file name.

        Arguments:
            fileitem {cgi.Storage} -- Storage object.
            prepend {string} -- The prefix you want to prepend to the file name.
        Keyword Arguments:
            location {string} -- The location on disk you would like to store the file. (default: {None})
        Returns:
            string -- Returns the file name just saved.
        """

        fileitem.filename = prepend + fileitem.filename

        return self.store(fileitem, location=location)
