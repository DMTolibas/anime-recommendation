from import_export import resources
from .models import AnimeImport

#Bridge between model and ImportExportlibrary
""" class AnimeImportResource(resources.ModelResource):
    class Meta:
        model = AnimeImport """

    

class AnimeImportResource(resources.ModelResource):
    class Meta:
        model = AnimeImport
        skip_unchanged = True
        use_transactions = False  # Prevent huge single transaction

    def import_data(self, dataset, dry_run=False, raise_errors=False, **kwargs):
        if dry_run:
            return super().import_data(dataset, dry_run, raise_errors, **kwargs)

        instances = []
        for row in dataset.dict:
            instance = AnimeImport(
                user_id=row.get("user_id"),
                rating=row.get("rating"),
                name=row.get("name")
            )
            instances.append(instance)

        AnimeImport.objects.bulk_create(instances, batch_size=1000)

        # Done. Skip super().import_data()
        # You can optionally return None or a custom result object
        return None