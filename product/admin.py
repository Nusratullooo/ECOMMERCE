from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from mptt.admin import DraggableMPTTAdmin
from product.models import Category, Product, Images, Comment


class CategoryAdmin(TranslationAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['title']


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductAdmin(TranslationAdmin):
    list_display = ['title', 'category', 'image_tag', 'old_price', 'sell_price', 'status']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'email', 'message', 'ip', 'product']
    list_display = ['name', 'email', 'message', 'create_at']


class CategoryAdmin2(DraggableMPTTAdmin):
    list_display = ('tree_actions',
                    'indented_title',
                    'related_products_count',
                    'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    mptt_indent_field = "title"

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True
        )

        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_count',
            cumulative=False
        )
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Product)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Images)
