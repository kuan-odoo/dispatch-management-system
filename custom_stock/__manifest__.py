{
    'name': "Stock transport",
    'version': '1.0',
    'depends': ['stock_picking_batch'],
    'author': "Anil kumawat",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/custom_stock_view.xml',
        
        
    ],
    # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    # 'demo': [
    #     'data/estate_demo.xml',
    # ],
    'installable': True,
    'application': True,
    
}