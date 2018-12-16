from mongoengine import fields
import mongoengine_goodjson as gj

# Docuementos almacenados en colecciones propias
class Localidad(gj.Document):
    nombre = fields.StringField(max_length=50)

# Documentos que no requieren su propia colección
class Superpoder(gj.EmbeddedDocument):
    nombre = fields.StringField(max_length=100, required=True)
    descripcion = fields.StringField(max_length=300, required=False)

#Documentos con documentos adentro
class Heroe(gj.Document):
    nombre = fields.StringField(max_length=50, required=True)

    superpoder = fields.EmbeddedDocumentField(Superpoder, required=False)

    # File fields!
    historia = fields.FileField(required=False)


# We have to go deeper
class Liga(gj.Document):
    nombre = fields.StringField(max_length=100)

    lugar = fields.ReferenceField(Localidad, requered=False)

    integrantes = fields.ListField(
        fields.ReferenceField(Heroe),
        required=False
    )
