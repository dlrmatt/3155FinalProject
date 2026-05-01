from . import orders, order_details, menu_items, resources, users, payments, promotions, reviews

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    users.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)