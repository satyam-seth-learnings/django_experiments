from datetime import timedelta

from django.utils import timezone
from typing import Optional, Type

from django.db import connection, models
from django.test import TransactionTestCase
from core.models import BaseCreatedModifiedModel

# Create your tests here.


class AbstractModelMixinTestCase(TransactionTestCase):
    """
    A test case that dynamically creates a model class based on the provided mixin
    and runs tests with that model
    """

    # mixin and model can initially be None, but will later be assigned a model class
    mixin: Optional[Type[models.Model]] = None
    model: Optional[Type[models.Model]] = None

    @classmethod
    def setUpClass(cls) -> None:
        # Ensure mixin is not None before attempting to create a model
        if cls.mixin is None:
            raise ValueError("Mixin class has not been set.")

        # Dynamically create a model by using the mixin as the base class
        cls.model = type(
            "TestModel" + cls.mixin.__name__,
            (cls.mixin,),  # Use the mixin as the base class
            {"__module__": cls.mixin.__module__},
        )

        # Create the model in the database schema
        with connection.schema_editor() as editor:
            editor.create_model(cls.model)

        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

        # Delete the dynamically created model from the schema, if model is not None
        if cls.model:
            with connection.schema_editor() as editor:
                editor.delete_model(cls.model)

        # Close the connection
        connection.close()


class TestBaseCreatedModifiedModel(AbstractModelMixinTestCase):
    """Test Base created modified Model"""

    mixin = BaseCreatedModifiedModel


    def test_creation(self) -> None:
        """Test creation of a model instance"""

       # Get current datetime
        now = timezone.now()
        
        # create model instance
        obj = self.model.objects.create()

        # Assert timestamps are close to the current time
        self.assertAlmostEqual(obj.created_on, now, delta=timedelta(seconds=1))
        self.assertAlmostEqual(obj.modified_on, now, delta=timedelta(seconds=1))
