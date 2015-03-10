from django.db import models
from .overwritestorage import OverwriteStorage
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

def content_file_name(instance, filename):
    return '/'.join(['kid_images', str(instance.id) + '.png'])

class Member(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    nickname = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    firstname = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    lastname = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    birthdate = models.DateField(
        null=False,
        blank=False
    )

    dad_name = models.CharField(
        null=True,
        blank=True,
        max_length=300
    )

    mom_name = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    address = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    province = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    gender = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    signup_date = models.DateField(
        null=True,
        blank=True,
        auto_now_add=True
    )

    image = models.ImageField(upload_to = content_file_name, 
        storage=OverwriteStorage(), 
        default = 'kid_images/None/no-img.jpg',
        validators=[validate_image])
    
    facebook_account = models.CharField(
        null=False,
        blank=False,
        max_length=300)

    def __unicode__(self):
        return '%s' % (self.nickname)

    def validate_unique(self, *args, **kwargs):
        super(Member, self).validate_unique(*args, **kwargs)
        if not self.id:
            if self.__class__.objects.filter(nickname=self.nickname, firstname=self.firstname).exists():
                raise ValidationError(
                    {
                        NON_FIELD_ERRORS:
                       ('Person with same ... already exists.',)
                    }
                )

    def save(self, *args, **kwargs):

        self.validate_unique()

        super(Member, self).save(*args, **kwargs)

    def path_and_rename(path):
        def wrapper(instance, filename):
            path = "kid_images"
            format = instance.id + instance.file_extension
            return os.path.join(path, format)

        return wrapper
