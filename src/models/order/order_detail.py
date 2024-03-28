from src.models.product.product import Product

class OrderDetail :
    """Class for modeling a detail of order"""
    product_id:int
    quantity: int
    total_weight : float


    def __init__(
            self,
            product_id: int,
            quantity: int,
            total_weight : float,

    ) -> None:
        self.product_id = product_id
        self.quantity = quantity
        self.total_weight = total_weight
