from . import (orders,
               order_details,
               menu_items,
               promotions,
               payments,
               users,
               resources,
               reviews,
               sales_data,
               customer_feedback,
               system_training_material)


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(menu_items.router)
    app.include_router(promotions.router)
    app.include_router(payments.router)
    app.include_router(users.router)
    app.include_router(resources.router)
    app.include_router(reviews.router)
    app.include_router(sales_data.router)
    app.include_router(customer_feedback.router)
    app.include_router(system_training_material.router)