from rest_framework import serializers

from .models import Specifications, ProductImage, Product, Store, Review, Category

from ..accounts.models import Seller


class FilterReviewListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
        extra_kwargs = {
            'parent': {'required': False}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['name'] = user.get_full_name() or user.username
        validated_data['email'] = user.email
        review = Review.objects.create(**validated_data)
        return review


class ReviewSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("id", "name", "text", "children")


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'children',
        )


class SpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specifications
        fields = (
            'id',
            'name',
            'value',
        )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'id',
            'image',
        )


class StoreSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    class Meta:
        model = Store
        fields = (
            'id',
            'name',
            'address',
            'description',
            'seller',
        )


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)
    specifications = SpecificationsSerializer(many=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'quantity',
            'images',
            'specifications',
            'reviews',
            'category',
            'store'
        )

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        specifications_data = validated_data.pop('specifications', [])

        product = Product.objects.create(**validated_data)

        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)

        for spec_data in specifications_data:
            Specifications.objects.create(product=product, **spec_data)

        return product




