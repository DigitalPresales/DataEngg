# This code goes on Ubuntu (Seller machine). Pl. make sure to have python and below libraries installed. You can refer to google for help to install those.
import os, sys
#You can capture logged in user by using $USER and similarly email and phone details from database in real time scenario. For demo , we are hardcoding it to below details.
#str = os.system('echo "$USER"')
#str2 = sys.argv
file_object = open('<File path of output file here>/o2.csv', 'a')
file_object.write('Buyer Name- Senthil Balaji')
file_object.write('Contact details - Email - Senthilb@gmail.com, Phone-408 453 54456')
file_object.close()


