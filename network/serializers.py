from rest_framework import serializers
from .models import Contact, Product, NetworkNode


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'country', 'city', 'street', 'house_number']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'model', 'release_date']


class NetworkNodeSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = NetworkNode
        fields = ['id', 'name', 'contacts', 'products', 'supplier', 'debt', 'level', 'created_at']
        read_only_fields = ['debt']  # Запретить обновление поля 'debt'

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        products_data = validated_data.pop('products')
        contact = Contact.objects.create(**contacts_data)
        network_node = NetworkNode.objects.create(contacts=contact, **validated_data)
        for product_data in products_data:
            product, _ = Product.objects.get_or_create(**product_data)
            network_node.products.add(product)
        return network_node

    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('contacts', None)
        products_data = validated_data.pop('products', None)

        if contacts_data:
            for attr, value in contacts_data.items():
                setattr(instance.contacts, attr, value)
            instance.contacts.save()

        if products_data:
            instance.products.clear()
            for product_data in products_data:
                product, _ = Product.objects.get_or_create(**product_data)
                instance.products.add(product)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
