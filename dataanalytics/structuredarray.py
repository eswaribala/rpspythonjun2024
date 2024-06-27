import numpy as np

customers = np.array([('Parameswari', 'Bala', 54),
                      ('Vignesh', 'Bala', 27),
                      ('Bala', 'Manickamuthu', 59)],
                     dtype=[('first_name', (np.str_,50)),
                            ('last_name', (np.str_,50)),
                            ('age', np.int32)])
print("Customer Information\n",customers)
