{
    'name': "Stock transport",
    'version': '1.0',
    'depends': ['base', 'stock_picking_batch','fleet','stock_delivery'],
    'author': "Anil kumawat",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/inherite_fleet_view.xml',
        'views/model_inherite_inventory.xml',
        
        
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