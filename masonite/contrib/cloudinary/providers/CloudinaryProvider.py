""" Cloudinary Service Provider """

from config import storage

from masonite.provider import ServiceProvider

from ..drivers import UploadCloudinaryDriver


class CloudinaryProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('UploadCloudinaryDriver', UploadCloudinaryDriver)

    def boot(self):
        pass
