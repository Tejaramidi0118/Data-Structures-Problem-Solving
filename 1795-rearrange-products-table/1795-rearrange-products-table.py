import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    result = products.melt(id_vars='product_id', 
                           value_vars=['store1', 'store2', 'store3'], 
                           var_name='store', 
                           value_name='price')
    
    result = result.dropna(subset=['price'])
    
    result['price'] = result['price'].astype(int)
    
    return result[['product_id', 'store', 'price']]