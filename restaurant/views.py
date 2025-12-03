from django.shortcuts import render
from .models import MenuItem, Order

def restaurant_index(request):
    # Step 5: Fetch all items for the menu
    menu_items = MenuItem.objects.all()

    if request.method == 'POST':
        # Step 7: Handle the POST request
        
        # Get list of selected IDs (returns a list of strings like ['1', '3'])
        selected_ids = request.POST.getlist('selected_items')
        
        # Query the DB for these specific items
        # This acts as a security check; we only trust IDs, not prices sent from HTML
        selected_objects = MenuItem.objects.filter(id__in=selected_ids)
        
        if selected_objects:
            # Calculate Total
            total = sum(item.price for item in selected_objects)
            
            # Step 8: Save Order to Database
            new_order = Order.objects.create(total_price=total)
            new_order.items.set(selected_objects) # Set ManyToMany relationship
            new_order.save()
            
            # Step 9: Render Bill
            return render(request, 'restaurant/bill.html', {'order': new_order})

    # Render the menu by default (GET request)
    return render(request, 'restaurant/menu.html', {'menu_items': menu_items})